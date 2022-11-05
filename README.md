# Alura Challenge Back End #5

API REST desenvolvida durante o Challenge Back End #5 da Alura.

## Considerações

Neste desafio decidi usar Python em conjunto ao microframework web Flask. 
Utilizei algumas das principais extensões do flask para lidar com banco de dados, serialização e configurações. Além de cobrir todas as rotas com testes unitários.

## Funcionalidades

Essa API implementa as seguintes especificações:
 - Rotas no padrão REST.
 - Validações feitas conforme as regras de negócio.
 - Banco de dados para a persistência de informações.

## Rotas implementadas

| Method | Route | Body Param. | Query Param.|
|--------|-------|-----|---------------|
| GET | /videos | - | - |
| GET | /videos/?search={titulo} | - | titulo do vídeo |
| GET | /videos/{id} | - | id do vídeo |
| POST | /videos | {'titulo', 'descricao', 'url', 'categoria_id'} | - |
| PUT | /videos/{id} | {'titulo', 'descricao', 'url', 'categoria_id'} | id do vídeo |
| PATCH | /videos/{id} | {'titulo', 'descricao', 'url', 'categoria_id'} | id do vídeo |
| DELETE | /videos/{id} | - | id do vídeo |
| GET | /categorias | - | - |
| GET | /categorias/{id} | - | id da categoria |
| POST | /categorias | {'titulo', 'cor'} | - |
| PUT | /categorias/{id} | {'titulo', 'cor'} | id da categoria |
| PATCH | /categorias/{id} | {'titulo', 'cor'} | id da categoria |
| DELETE | /categorias/{id} | - | id da categoria |


## Pré-requisitos
 - Python 3.10.8
 - Flask 2.2.2

## Principais Bibliotecas

|  | |
| ----------------  | --------------------------------- |
| Flask             |
| Flask SQLAlchemy  | Modelos e buscar no Banco de Dados       |
| Flask Migrate     | Migrações no Banco de Dados       |
| Flask Marshmalow  | Serialização e Validação de JSON |
| Dynaconf          | Auxiliar com as configurações     |
| Pytest            | Testes automatizados              |


## Como rodar a aplicação

### Configuração do ambiente e instalação de dependências

Após baixar e entrar na raiz do projeto, crie um ambiente virtual e ative-o:

```
$ python -m venv venv
$ venv/scripts/activate # Windows
$ source venv/bin/activate # Linux
```
Em seguida instale as dependências:
```
$ pip install -r requirements.txt
```

### Criação do banco de dados

Para criar e popular o banco de dados:

```
$ flask create-db
$ flask populate-db
```

Caso queira apagar todos os dados:

```
$ flask drop-db
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
$ pytest
```
A saída esperada:
```
platform ~ -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: ~\api-aluraflix, configfile: pytest.ini
collected 37 items                                                                                                   

tests\test_categorias.py ................. [ 45%] 
tests\test_videos.py ....................  [100%]
```


## Cronograma

### Semana 1

- [x] Modelo e CRUD para videos.
- [x] Testes unitários para videos.

### Semana 2

- [x] Modelo e CRUD para categorias.
- [x] Testes unitários para categorias
- [x] Filtro para videos por query string.
- [ ] Testes de integração.
