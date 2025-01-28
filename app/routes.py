from flask import Blueprint, request, jsonify
from .models import User
from .extensions import database


blueprint = Blueprint('api', __name__, url_prefix='/api')

@blueprint.route('/users', methods=['POST'])
def create_user():
    """
    Rota para criar um novo usuário.

    Espera um JSON no corpo da requisição com os seguintes campos:
        - name (str): Nome do usuário (obrigatório).
        - birth_date (str): Data de nascimento no formato 'YYYY-MM-DD' (obrigatório).

    Retorna:
        - 201: Usuário criado com sucesso, com os dados do usuário no formato JSON.
        - 400: Erro de entrada inválida, com mensagem de erro.
        - 500: Erro interno do servidor, com mensagem de erro.
    """
    
    #  Obter dados do corpo da requisição
    data = request.get_json()

    # Garantir que os campos obrigatórios estão presentes
    if not data or not all(item in data for item in ("name", "birth_date")):
        return jsonify({"error": "Input not accepted"}), 400
    
    try:
        # Criar instância do usuário com os dados fornecidos
        user = User(
            name=data['name'],
            birth_date=data['birth_date']
        )

        # Adicionar e salvar o usuário no banco de dados
        database.session.add(user)
        database.session.commit()

        # Retornar os dados do usuário criado
        return jsonify(user.to_dict()), 201
    except Exception as e:
        # Lidar com erros e retornar mensagem
        return jsonify({"Error ": str(e)}), 500
