import { createClient } from 'https://esm.sh/@supabase/supabase-js@2.45.4'

// ─────────────────────────────────────────────────────────────────────────
// Webhook da Hotmart (versão 2.0.0): libera o P5P Prospecta para o e-mail de
// quem comprou o Método P5P, e bloqueia em reembolso ou chargeback.
//
// Configuração:
//   - Secret HOTMART_HOTTOK no Supabase (Edge Functions > Secrets) com o "Hottok"
//     da tela de webhooks da Hotmart. Sem ele, nada é aceito.
//   - Secret opcional HOTMART_PRODUTOS: ids dos produtos que liberam acesso,
//     separados por vírgula (padrão: 8355172, o Método P5P).
//   - Roda sem login do Supabase (verify_jwt = false); quem prova que é a
//     Hotmart é o Hottok.
// O e-mail de boas-vindas sai pelo webhook da Fábrica de Copy (mesma compra),
// então aqui não se manda e-mail. Tudo que chega fica em hotmart_eventos.
// ─────────────────────────────────────────────────────────────────────────

const LIBERA = new Set(['PURCHASE_APPROVED', 'PURCHASE_COMPLETE'])
const BLOQUEIA = new Set(['PURCHASE_REFUNDED', 'PURCHASE_CHARGEBACK'])
const PRODUTOS_PADRAO = '8355172'

function json(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

// Comparação em tempo constante, para não vazar o Hottok pela demora da resposta.
function mesmoToken(a: string, b: string): boolean {
  const ea = new TextEncoder().encode(a)
  const eb = new TextEncoder().encode(b)
  let diff = ea.length ^ eb.length
  for (let i = 0; i < Math.max(ea.length, eb.length); i++) {
    diff |= (ea[i] ?? 0) ^ (eb[i] ?? 0)
  }
  return diff === 0
}

Deno.serve(async (req) => {
  if (req.method !== 'POST') {
    return json({ error: 'Method not allowed' }, 405)
  }

  const hottokEsperado = Deno.env.get('HOTMART_HOTTOK')
  if (!hottokEsperado) {
    console.error('HOTMART_HOTTOK não configurado nos secrets do Supabase')
    return json({ error: 'Webhook não configurado' }, 500)
  }

  // deno-lint-ignore no-explicit-any
  let payload: any
  try {
    payload = await req.json()
  } catch {
    return json({ error: 'JSON inválido' }, 400)
  }

  const hottokRecebido = req.headers.get('x-hotmart-hottok') ?? payload?.hottok ?? ''
  if (!mesmoToken(String(hottokRecebido), hottokEsperado)) {
    return json({ error: 'Não autorizado' }, 401)
  }

  const evento = String(payload?.event ?? '')
  const email = String(payload?.data?.buyer?.email ?? '').trim().toLowerCase()
  const produtoId = String(payload?.data?.product?.id ?? '')
  const transacao = String(payload?.data?.purchase?.transaction ?? '')
  const produtosQueLiberam = (Deno.env.get('HOTMART_PRODUTOS') ?? PRODUTOS_PADRAO)
    .split(',')
    .map((id) => id.trim())
    .filter(Boolean)

  const admin = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!)
  let resultado = 'ignorado'

  if (!email || !email.includes('@')) {
    resultado = 'sem e-mail'
  } else if (!produtosQueLiberam.includes(produtoId)) {
    resultado = 'outro produto'
  } else if (LIBERA.has(evento) || BLOQUEIA.has(evento)) {
    const status = LIBERA.has(evento) ? 'ativo' : 'bloqueado'
    const { error } = await admin.from('acessos').upsert(
      {
        email,
        status,
        origem: 'hotmart',
        produto_id: produtoId,
        transacao,
        ultimo_evento: evento,
        atualizado_em: new Date().toISOString(),
      },
      { onConflict: 'email' },
    )
    if (error) {
      console.error('Erro ao gravar acesso', error)
      resultado = 'erro'
    } else {
      resultado = status === 'ativo' ? 'liberado' : 'bloqueado'
    }
  }

  const { error: logError } = await admin.from('hotmart_eventos').insert({
    evento,
    email: email || null,
    produto_id: produtoId || null,
    transacao: transacao || null,
    resultado,
    payload,
  })
  if (logError) {
    console.error('Erro ao gravar hotmart_eventos', logError)
  }

  // Erro de banco devolve 500 para a Hotmart tentar de novo; o resto é 200.
  if (resultado === 'erro') {
    return json({ ok: false }, 500)
  }
  return json({ ok: true, resultado })
})
