# BD POKEAPI

Este projeto é uma aplicação Flask que expõe uma API REST para operações de cadastro de consulta da Pokelista MVP
![image](https://github.com/dreamkatana/mvc_pode_bd2/assets/7691411/a51fb788-f869-4882-98c3-c05b95936cc1)

## Instalação

### Requisitos
- Python 3.7+
- Flask 1.1.2+
- Flask-Smorest 0.31.0+
- SQLAlchemy 1.3.23+

### Instruções DOCKER
docker build -t mvc_bd . 
Cadastrar o mesmo nome do docker_compose da aplicação frontend `https://github.com/dreamkatana/mvc_poke_front`.


### Instruções

1. Clone o repositório para sua máquina local usando `[https://github.com/dreamkatana/mvc_pode_bd2/yourrepository.git](https://github.com/dreamkatana/mvc_pode_bd2.git)`.

2. Navegue até o diretório do projeto: `cd yourrepository`

3. Crie um ambiente virtual Python: `python3 -m venv venv`

4. Ative o ambiente virtual: 
    - Linux/macOS: `source venv/bin/activate`
    - Windows: `venv\Scripts\activate`

5. Instale as dependências: `pip install -r requirements.txt`

## Utilização

1. Para iniciar o servidor, execute: `flask run`

2. A API estará disponível em `http://localhost:5000`.

3. Você pode interagir com a API usando uma ferramenta como cURL, Postman ou um navegador web.

## Endpoints

-GET
/searches/{id}


PUT
/searches/{id}


DELETE
/searches/{id}


GET
/searches


POST
/searches

## Contribuição

Contribuições são sempre bem-vindas! Por favor, veja o arquivo `CONTRIBUTING.md` para mais detalhes.

## Suporte

Se você encontrar um bug ou tiver alguma sugestão, por favor, abra uma issue no GitHub.

## Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo `LICENSE.md` para mais detalhes.
