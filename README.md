# Alura Challenge Back End #5

API REST desenvolvida durante o Challenge Back End #5 da Alura.

A API está disponível em:

https://api-aluraflix-rodrigofmeneses.herokuapp.com/videos/free/


## Considerações

Neste desafio decidi usar Python em conjunto ao microframework web Flask. 
Utilizei algumas das principais extensões do flask para lidar com banco de dados e serialização. Além de cobrir todas as rotas com testes de integração.

## Funcionalidades

Essa API implementa as seguintes especificações:
 - Rotas no padrão REST.
 - Validações feitas conforme as regras de negócio.
 - Banco de dados para a persistência de informações.
 - Autenticação via JWT.

## Rotas implementadas

Exceto as rotas de autenticação `/auth/register`, `/auth/login` e a rota `/videos/free` todas as rotas são protegidas. Para acessa-las é necessário em cada request enviar um token de autenticação no header:

`{'Authorization': 'token'}` 

Para obter esse token basta acessar a rota `/auth/login` enviando no body da requisição das credenciais de um usuário cadastrado no sistema: 

```
{
    'username': 'rodrigo',
    'password': '123456'
}
```

Essa rota fornecerá uma mensagem se o login foi efetuado com sucesso ou não e um token válido por 60 segundos. Após esse tempo é necessário obter um novo token.

Para cadastrar um funcionário, semelhante a etapa de login, deve-se enviar as credenciais de um novo usuário para a rota `/auth/register`, nesse instante já receberá um token válido.


### Rotas Livres

| Method | Route | Body Param. | Response.|
|--------|-------|-----|---------------|
| GET | /videos/free | - | - |
| POST | /auth/register | {'username', 'password'} | {'message', 'token'} |
| POST | /auth/login | {'username', 'password'} | {'message', 'token'} |

### Rotas Protegidas

| Method | Route | Body Param. | Query Param.|
|--------|-------|-----|---------------|
| GET | /videos | - | - |
| GET | /videos/?search={title} | - | título do vídeo |
| GET | /videos/{id} | - | id do vídeo |
| POST | /videos | {'title', 'description', 'url', 'category_id'} | - |
| PUT | /videos/{id} | {'title', 'description', 'url', 'category_id'} | id do vídeo |
| PATCH | /videos/{id} | {'title', 'description', 'url', 'category_id'} | id do vídeo |
| DELETE | /videos/{id} | - | id do vídeo |
| GET | /categories | - | - |
| GET | /categories/{id} | - | id da categoria |
| POST | /categories | {'title', 'color'} | - |
| PUT | /categories/{id} | {'title', 'color'} | id da categoria |
| PATCH | /categories/{id} | {'title', 'color'} | id da categoria |
| DELETE | /categories/{id} | - | id da categoria |

## Pré-requisitos
 - Python 3.10.8
 - Flask 2.2.2
 - SQLite (Caso queira mudar o sgbd, basta trocar as credenciais no SQLAlchemy)

## Principais Bibliotecas

|  | |
| ----------------  | --------------------------------- |
| Flask             |
| Flask SQLAlchemy  | Modelos e buscar no Banco de Dados       |
| Flask Migrate     | Migrações no Banco de Dados       |
| Flask Marshmalow  | Serialização e Validação de JSON |
| Python dotenv| Lidar com variáveis de ambiente |
| Pytest            | Testes automatizados              |


## Como rodar a aplicação

### Variáveis de Ambiente

Para rodas este projeto, voce precisará adicionar as seguintes variáveis de ambiente. As que usei estão disponíveis como referência, mas fique a vontade para modificar o arquivo `.env`. Por padrão usei o SQLite para desenvolvimento.

Observe também que há o arquiv `.env.test`, por padrão o banco de dados de teste é um SQLite na memória.

<!-- To run this project, you will need to add the following environment variables to your .env file -->

`SQLALCHEMY_DATABASE_URI` = Conexão com o banco de dados.

`SECRET_KEY` = Necessário para autenticação via JWT.

### Configuração do ambiente e instalação de dependências

Após baixar e entrar na raiz do projeto, crie um ambiente virtual e ative-o:

```
python -m venv venv
venv/scripts/activate # Windows
source venv/bin/activate # Linux
```
Em seguida instale as dependências:
```
pip install -r requirements.txt
```

### Criação do banco de dados

Primeiramente fazer as migrações com auxílio a biblioteca flask_migrate:

```
flask db init
flask db migrate
flask db upgrade
```

Em seguida basta criar e popular o banco de dados:

```
flask create-db
flask populate-db
```

Caso queira apagar o banco de dados:

```
flask drop-db
```

Esses comandos podem ser customizados em ```app\ext\commands.py```.

### Inicializando a aplicação

```
flask run
```

No terminal deve apresentar:

```
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 792-992-212
```

## Como rodar os testes

Para rodar os testes:

```
pytest
```
A saída esperada:
```
platform ~ -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: ~\api-aluraflix, configfile: pytest.ini
collected 47 items                                                                                                                                                                                 

tests/test_auth.py .......................[ 12%]
tests/test_categories.py .................[ 48%]
tests/test_users.py ......................[ 55%]
tests/test_videos.py .....................[100%]
```


## Cronograma

### Semana 1

- [x] Modelo e CRUD para videos.
- [x] Testes unitários para videos.

### Semana 2

- [x] Modelo e CRUD para categories.
- [x] Testes unitários para categories
- [x] Filtro para videos por query string.
- [x] Testes de integração.

### Semana 3 e 4

- [x] Paginação
- [x] Autenticação
- [x] Deploy
