# Demanda 1  

<!-- - Escolhi linguagem Python pela familiaridade (versao 3.11.2)
- Decidindo entre os frameworks mais conhecidos (fastapi e flask) (https://www.netguru.com/blog/python-flask-versus-fastapi, https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
- Já tinha usado Django REST Framework mas preeri escolher outro pois a documentação do DRF é pobre

- Escolhi flask por ser mais bem estabelecido (mais antigo) com recursos de segurança mais robustos e mais simples de começar

flask_api/ 
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── extensions.py # Apenas se preferir testar localmente antes do Docker. 
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env -->
Desenvolvida em ambiente WSL com Ubuntu 22.04.4 LTS e executada localmente utilizando o IP da máquina obtido com o comando ```ip a```.  

## **Como executar o projeto**  

1. Clone o repositório
```
git clone https://github.com/anycarolinys/dockerized_flask_api.git
```

2. Execute os containers em segundo plano 
```
docker-compose up --build -d 
```
Para execuções posteriores basta
```
docker-compose up -d 
```

3. Devem haver dois containers em execução (Aplicação Flask e MySQL) confira com
```
docker ps
```

4. Para realizar requisições a API Flask usando terminal em ambiente Linux
```
curl -X POST http://localhost:5000/api/users \
    -H "Content-Type: application/json" \
    -d '{"name": "<>", "birth_date": "<>"}'
```

5. Para consultar o banco de dados usando terminal em ambiente Linux
```
docker exec -it mysql_db mysql -u flask_user -pflask_password
USE flask_db;
SELECT * FROM user;
exit
```

7. Para encerrar a execução dos containers  
```
docker-compose down
```

## **Como foi desenvolvido o projeto**  
**1. Decisão da tecnologia**
- Escolhi linguagem Python pela familiaridade
- Decidi entre os frameworks mais conhecidos (Flask e FastAPI) vendo [comparação](https://www.netguru.com/blog/python-flask-versus-fastapi) entre os mesmos
- Escolhi Flask por ser mais antigo, supondo haver mais recursos e melhor documentação

**2. Implementação dos arquivos para o Docker**  
- Utilizei [este artigo](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/) como base

**3. Implementação da API**  
- Utilizei a [documentação oficial](https://flask.palletsprojects.com/en/stable/tutorial/layout/) como principal referência, principalmente para compreender a estrutura de um projeto Flask

## **Resultados**
- A API deve conter ao menos uma rota simples  
Arquivo ```routes.py``` rota '/api/users'  

- A API deve conseguir se conectar ao banco de dados e executar uma operação
```
database.session.add(user)
database.session.commit()
```
em ```routes.py```  

- A configuração de rede e volumes deve ser funcional  
Parâmetro ```networks``` e ```volumes``` em ```docker-compose.yml```    

- Utilize volumes para persistência de dados do banco de dados  
Para testar esse recurso encerre os serviços com
```
docker-compose down
```  
reinicie com  

```
docker-compose up -d 
```  
e faça uma requisição ao banco de dados confirmando que os registros permanecem lá  

## **Principais dificuldades**  
**1. Compreender a estrutura padrão de uma aplicação Flask**
- Como não existe um builder que automatize a geração de um projeto Flask e vários exemplos traziam diferentes estruturas de arquivos e formas de rodar o projeto, utilizei IA para me fornecer o esqueleto de estrutura modularizada para esse framework

## **O que poderia ter sido melhorado/realizado com mais tempo**  
-  Poderia ser adicionada uma documentação com o framework Swagger utilizando a biblioteca [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/swagger.html)
- Poderia ser adicionada uma rota GET para obter os registros cadastrados

## **Principais aprendizados**
- Compreensão do framework Flask para desenvolvimento de APIs
- Persistência de dados com o docker compose utilizando volumes
