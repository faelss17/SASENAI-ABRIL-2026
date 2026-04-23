# Barbearia do TL

Sistema web em **Django** para gerenciamento de barbearia, criado para portfólio. O projeto atende aos requisitos de autenticação, páginas protegidas, CRUD via interface web, CRUD via API, mensagens de feedback, herança de templates e organização em camadas, com interface responsiva em Bootstrap.

## Funcionalidades

- Login e logout com autenticação do Django
- Dashboard protegido
- Cadastro de clientes, barbeiros, serviços e agendamentos
- CRUD completo pela interface web
- CRUD completo pela API REST
- Mensagens de sucesso e erro
- Rotas protegidas para usuários autenticados
- Template base com menu de navegação responsivo
- Interface modernizada com Bootstrap 5
- Validações de formulário e de regras de negócio

## Visual

- Navbar com menu responsivo
- Dashboard com cards e atalhos rápidos
- Listagens com tabelas responsivas
- Formulários estilizados com Bootstrap
- Layout preparado para desktop e mobile

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- SQLite3
- Bootstrap 5

## Models do projeto

- `Cliente`
- `Barbeiro`
- `Servico`
- `Agendamento`

## Requisitos atendidos da atividade

- Página de login
- Pelo menos 3 páginas protegidas por autenticação
- Pelo menos 3 models diferentes
- CRUD via interface web
- API em rotas separadas
- CRUD via API
- Mensagens de feedback
- `base.html` com herança de templates
- Menu funcional de navegação
- README e `.gitignore`

## Como executar

### 1. Criar ambiente virtual

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Aplicar migrações

```bash
python manage.py migrate
```

### 4. Criar superusuário

```bash
python manage.py createsuperuser
```

### 5. Rodar o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

- Sistema web: `http://127.0.0.1:8000/`
- Admin Django: `http://127.0.0.1:8000/admin/`

## Executando os testes básicos do projeto

```bash
python manage.py test
```

## Rotas web

- `/login/`
- `/logout/`
- `/`
- `/clientes/`
- `/barbeiros/`
- `/servicos/`
- `/agendamentos/`

## Rotas da API

Todas as rotas da API exigem autenticação, conforme configuração do Django REST Framework.

- `/api/clientes/`
- `/api/barbeiros/`
- `/api/servicos/`
- `/api/agendamentos/`

Exemplos de operações:

- `GET /api/clientes/` → listar
- `POST /api/clientes/` → criar
- `GET /api/clientes/1/` → detalhar
- `PUT /api/clientes/1/` → atualizar
- `DELETE /api/clientes/1/` → excluir

## Exemplos de JSON

### Cliente
```json
{
  "nome": "Carlos Silva",
  "telefone": "31999999999",
  "email": "carlos@email.com"
}
```

### Barbeiro
```json
{
  "nome": "João",
  "especialidade": "Degradê",
  "telefone": "31988888888",
  "ativo": true
}
```

### Serviço
```json
{
  "nome": "Corte Tradicional",
  "descricao": "Corte masculino tradicional",
  "preco": "35.00",
  "duracao_estimada": 45
}
```

### Agendamento
```json
{
  "cliente": 1,
  "barbeiro": 1,
  "servico": 1,
  "data": "2026-05-10",
  "horario": "14:30:00",
  "observacoes": "Cliente prefere atendimento rápido",
  "status": "agendado"
}
```

## Sugestão de commits

```bash
git init
git add .
git commit -m "feat: cria estrutura inicial do projeto"
git commit -m "feat: adiciona autenticação e páginas protegidas"
git commit -m "feat: implementa CRUD web de clientes, barbeiros e serviços"
git commit -m "feat: implementa CRUD de agendamentos e API REST"
git commit -m "docs: adiciona README do projeto"
```

## Observações importantes

- O sistema utiliza `ModelSerializer` para serialização da API.
- As rotas protegidas usam autenticação do Django.
- Os formulários impedem dados inválidos por meio das validações do Django e da regra de negócio do model `Agendamento`.
- Registros inexistentes retornam erro 404 automaticamente nas views genéricas e na API.
- As mensagens de feedback são exibidas após criação, edição e exclusão.
