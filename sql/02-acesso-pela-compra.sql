-- ============================================================
-- P5P Prospecta: acesso liberado pela compra do Método P5P (Hotmart)
-- Rode UMA VEZ depois do schema.sql. Pode rodar de novo sem estragar nada.
--
-- Como funciona:
--   - O webhook da Hotmart (função hotmart-webhook) grava o e-mail de quem
--     comprou em "acessos" (ativo) e bloqueia em reembolso ou chargeback.
--   - Quem já tinha conta antes desta mudança continua entrando (conta_existente).
--   - perfis e leads só abrem para o dono E com acesso ativo. Sem acesso, a conta
--     existe, mas não lê nem grava nada. O painel avisa pelo tem_acesso().
-- ============================================================

create table if not exists public.acessos (
  email text primary key,
  status text not null default 'ativo' check (status in ('ativo', 'bloqueado')),
  origem text not null default 'hotmart',
  produto_id text,
  transacao text,
  ultimo_evento text,
  criado_em timestamptz not null default now(),
  atualizado_em timestamptz not null default now()
);
alter table public.acessos enable row level security;
-- Sem políticas de propósito: só o webhook (service role) lê e grava.

create table if not exists public.hotmart_eventos (
  id bigint generated always as identity primary key,
  recebido_em timestamptz not null default now(),
  evento text,
  email text,
  produto_id text,
  transacao text,
  resultado text,
  payload jsonb
);
alter table public.hotmart_eventos enable row level security;

-- O aluno logado tem acesso? (e-mail do login, sem diferença de maiúsculas)
create or replace function public.tem_acesso()
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1
    from public.acessos a
    where a.email = lower(trim(coalesce(auth.jwt() ->> 'email', '')))
      and a.status = 'ativo'
  );
$$;
revoke all on function public.tem_acesso() from public;
revoke all on function public.tem_acesso() from anon;
grant execute on function public.tem_acesso() to authenticated;

-- Quem já tem conta hoje continua entrando.
insert into public.acessos (email, origem)
select lower(trim(u.email)), 'conta_existente'
from auth.users u
where u.email is not null and trim(u.email) <> ''
on conflict (email) do nothing;

-- Troca todas as políticas de perfis e leads pelas novas (dono + acesso ativo).
do $$
declare p record;
begin
  for p in
    select policyname, tablename from pg_policies
    where schemaname = 'public' and tablename in ('perfis', 'leads')
  loop
    execute format('drop policy %I on public.%I', p.policyname, p.tablename);
  end loop;
end $$;

alter table public.perfis enable row level security;
alter table public.leads enable row level security;

create policy "perfis_select_own" on public.perfis
  for select to authenticated
  using ((select auth.uid()) = user_id and (select public.tem_acesso()));
create policy "perfis_insert_own" on public.perfis
  for insert to authenticated
  with check ((select auth.uid()) = user_id and (select public.tem_acesso()));
create policy "perfis_update_own" on public.perfis
  for update to authenticated
  using ((select auth.uid()) = user_id and (select public.tem_acesso()))
  with check ((select auth.uid()) = user_id and (select public.tem_acesso()));

create policy "leads_select_own" on public.leads
  for select to authenticated
  using ((select auth.uid()) = user_id and (select public.tem_acesso()));
create policy "leads_insert_own" on public.leads
  for insert to authenticated
  with check ((select auth.uid()) = user_id and (select public.tem_acesso()));
create policy "leads_update_own" on public.leads
  for update to authenticated
  using ((select auth.uid()) = user_id and (select public.tem_acesso()))
  with check ((select auth.uid()) = user_id and (select public.tem_acesso()));
create policy "leads_delete_own" on public.leads
  for delete to authenticated
  using ((select auth.uid()) = user_id and (select public.tem_acesso()));
