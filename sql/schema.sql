-- ============================================================
-- Prospector de Sites — schema do Supabase
-- Rode isto UMA VEZ em: Supabase → SQL Editor → New query → Run
-- ============================================================

create extension if not exists pgcrypto;

-- ------------------------------------------------------------
-- PERFIS: dados de cada aluno (o que hoje era prospector-config.json)
-- ------------------------------------------------------------
create table if not exists public.perfis (
  user_id uuid primary key references auth.users(id) on delete cascade,
  nome text,
  apresentacao text,
  whatsapp text,
  nichos text[] default array['nutricionistas','psicologos','advogados','psiquiatras'],
  cidade text,
  leads_por_busca int default 10,
  envio_modo text default 'rascunho',
  github_usuario text,
  github_token text,
  github_privado boolean default false,
  criado_em timestamptz default now(),
  atualizado_em timestamptz default now()
);

alter table public.perfis enable row level security;

drop policy if exists "perfis_select_own" on public.perfis;
create policy "perfis_select_own" on public.perfis
  for select using (auth.uid() = user_id);

drop policy if exists "perfis_insert_own" on public.perfis;
create policy "perfis_insert_own" on public.perfis
  for insert with check (auth.uid() = user_id);

drop policy if exists "perfis_update_own" on public.perfis;
create policy "perfis_update_own" on public.perfis
  for update using (auth.uid() = user_id);

-- ------------------------------------------------------------
-- LEADS: os clientes prospectados de cada aluno (o que hoje era leads.md + prospector.db)
-- ------------------------------------------------------------
create table if not exists public.leads (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  slug text not null,
  nome text,
  nicho text,
  cidade text,
  nota numeric,
  avaliacoes int,
  email text,
  telefone text,
  whatsapp text,
  site_antigo text,
  motivo text,
  status text default 'novo',   -- novo | redesenhado | publicado | proposta | respondeu | fechado | descartado
  url_nova text,
  data_proposta date,
  valor numeric,
  obs text,
  contrato_status text default 'pendente',  -- pendente | enviado | assinado
  contrato_em date,
  manutencao numeric,
  pago boolean default false,
  doc_cliente text,
  end_cliente text,
  criado_em timestamptz default now(),
  atualizado_em timestamptz default now(),
  unique (user_id, slug)
);

alter table public.leads enable row level security;

drop policy if exists "leads_select_own" on public.leads;
create policy "leads_select_own" on public.leads
  for select using (auth.uid() = user_id);

drop policy if exists "leads_insert_own" on public.leads;
create policy "leads_insert_own" on public.leads
  for insert with check (auth.uid() = user_id);

drop policy if exists "leads_update_own" on public.leads;
create policy "leads_update_own" on public.leads
  for update using (auth.uid() = user_id);

drop policy if exists "leads_delete_own" on public.leads;
create policy "leads_delete_own" on public.leads
  for delete using (auth.uid() = user_id);

-- ------------------------------------------------------------
-- Mantém atualizado_em sempre em dia sozinho
-- ------------------------------------------------------------
create or replace function public.marcar_atualizado()
returns trigger as $$
begin
  new.atualizado_em = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists trg_perfis_atualizado on public.perfis;
create trigger trg_perfis_atualizado
  before update on public.perfis
  for each row execute function public.marcar_atualizado();

drop trigger if exists trg_leads_atualizado on public.leads;
create trigger trg_leads_atualizado
  before update on public.leads
  for each row execute function public.marcar_atualizado();
