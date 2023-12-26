from flask import Blueprint, request, jsonify
import re, bcrypt
from config.properties import set_environments
from config.jdbc.jdbc import sign_up_new_user

sign_up_route = Blueprint('signUp_route', __name__)

def valida_senha(senha):
    padrao_senha = r'^(?=.*[A-Za-z0-9])(?=.*[@#$%^&+=])(?=\S+$).{8,}$'
    if re.match(padrao_senha, senha):
        return True
    else:
        return False

def validacao_email(email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(padrao_email, email):
        return True
    else:
        return False

@sign_up_route.route('/signup', methods=['POST'], strict_slashes=False)
def user_sign_up():
    data = request.get_json()

    # Executando validações de campos
    if 'email' not in data:
        return jsonify({'error': 'Campo "email" é obrigatório.'}), 400
    elif 'nome' not in data:
        return jsonify({'error': 'Campo "nome" é obrigatório.'}), 400
    elif 'sobrenome' not in data:
        return jsonify({'error': 'Campo "sobrenome" é obrigatório.'}), 400
    elif 'password' not in data:
        return jsonify({'error': 'Campo "password" é obrigatório.'}), 400
    elif 'nascimento' not in data:
        return jsonify({'error': 'Campo "nascimento" é obrigatório.'}), 400
    
    # Carregando valores dos campos
    nome = data['nome']
    sobrenome = data['sobrenome']
    email = data['email']
    nascimento = data['nascimento']
    password = data['password']

    # Validação dos campos existentes
    if validacao_email(email) == False:
        return jsonify({'error': 'Campo "email" contém um email inválido.'}), 400 

    if valida_senha(password) == False:
        return jsonify({
            'mensagem': 'A senha precisa ter pelo menos um número, um caractere especial e ter mais de 8 caracteres.'}), 400

    encrypted_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    db_config = set_environments()
    try:
        if 'telefone' in data:
            telefone = data['telefone']
            sign_up_new_user(db_config, nome, sobrenome, email, encrypted_password, nascimento, telefone)
        else:
            sign_up_new_user(db_config, nome, sobrenome, email, encrypted_password, nascimento)
        
        return jsonify({"Message": "Usuário cadastrado com sucesso."}), 200
    except Exception as e:
        return jsonify({"Error": f"{e}"}), 400
