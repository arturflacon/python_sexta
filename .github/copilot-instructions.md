<!-- Instruções para agentes de código (AI) trabalhando neste repositório -->
# Copilot / Agente — Guia Rápido (resumo do projeto)

Projeto Django minimal: projeto raiz `naes2026` com dois apps principais: `website` e `aluguel`.

- Estrutura chave:
  - `manage.py` — comandos Django.
  - `naes2026/settings.py` — configurações (DB por `DATABASE_URL`, templates em `BASE_DIR / "templates"`).
  - `website/models.py` — modelos principais (Cliente, Administrador, Chacara, Reserva).
  - `website/views.py` — usa `CreateView`/`TemplateView`; observe que as `CreateView` omitiram o campo `usuario`.
  - `website/templates/website/` — templates de app; arquivos de formulário devem ser adicionados aqui (`cliente_form.html`, etc.).
  - `static/` — assets estáticos (ex.: `static/css/estilo.css`).

Por que isso importa
- `naes2026/settings.py` está preparado para um banco Postgres via `DATABASE_URL` (Neon). Há um bloco comentado para sqlite local — para desenvolvimento local, prefira habilitar o bloco sqlite e executar `migrate`.
- `Cliente.usuario` e `Administrador.usuario` são `OneToOneField` para `auth.User` (não-null). As `CreateView` em `website/views.py` não incluem `usuario`: garanta que um `User` exista antes de criar `Cliente`/`Administrador` ou ajuste a view/formulário para associar o usuário.

Comandos úteis (locais)

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
pip install django==5.2.11
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py test
```

Padrões e convenções do repositório
- Views: preferência por class-based views (`CreateView`, `TemplateView`) — ver `website/views.py`.
- Modelos: usam `verbose_name` e `help_text` extensivamente — siga este estilo em novos campos.
- Templates: coloque templates por app em `website/templates/website/` ou no diretório global `templates/` (configurado em `TEMPLATES['DIRS']`).
- Static: assets em `static/`; `STATICFILES_DIRS` aponta para `BASE_DIR / "static"`.

Integrações externas
- Banco de dados: `DATABASE_URL` (Postgres); o código faz `urlparse` e `parse_qsl` para popular `DATABASES`.

Problemas a observar (prioridade)
- Secret key e DEBUG: `SECRET_KEY` está no arquivo — não inclua chaves reais em PRs públicos.
- Inconsistência de formulário/relacionamento: `Cliente`/`Administrador` exigem `usuario` — revisar fluxos de criação.

Onde olhar primeiro
- `naes2026/settings.py` — configuração de DB e templates.
- `website/models.py` e `website/views.py` — exemplos de modelo / view que determinam formulários e templates esperados.
- `website/templates/website/` — localização de templates existentes (`modelo.html`, `sobre.html`, etc.).

Checklist rápido para mudanças/prs
- Inclua migrations geradas quando alterar modelos.
- Não exponha `SECRET_KEY` em commits.
- Garanta que a criação de `Cliente`/`Administrador` associe um `auth.User` válido.
- Rode `python manage.py migrate` e `python manage.py test` antes de abrir PR.

Se algo estiver ambíguo
- Pergunte qual DB usar (local sqlite vs `DATABASE_URL`).
- Se houver dúvidas sobre usuários, verifique se há um fluxo de cadastro de `User` separado — o repositório espera isso.

Fim.
