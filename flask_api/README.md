- Escolhi linguagem Python pela familiaridade (versao 3.11.2)
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
└── .env