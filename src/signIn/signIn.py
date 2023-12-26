from flask import Blueprint, request, jsonify
from config.properties import set_environments_with_secret
from ..signUp.signup import validacao_email
from config.jdbc.jdbc import sign_in_user

sign_in_route = Blueprint('signIn_route', __name__)

@sign_in_route.route('/signin', methods=['POST'], strict_slashes=False)
def sign_in():
    data = request.get_json()

    if 'email' not in data:
        return jsonify({'error': 'Campo "email" é obrigatório.'}), 400
    elif 'password' not in data:
        return jsonify({'error': 'Campo "password" é obrigatório.'}), 400
    
    email = data['email']
    password = data['password']

    # Validação dos campos existentes
    if validacao_email(email) == False:
        return jsonify({'error': 'Campo "email" contém um email inválido.'}), 400 

    db_config, secret = set_environments_with_secret()

    try:
        response, status = sign_in_user(db_config, secret, email, password)
        if status == 0:
            return jsonify({'Bearer': response}), 200
        elif status == 1:
            return jsonify({'error': "Credenciais inválidas."}), 400
        else:
            return jsonify({'error': response})
        
    except Exception as e:
        return jsonify({"Error": f"{e}"})

    
