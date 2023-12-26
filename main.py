from flask import Flask
from config.properties import set_environments
from config.jdbc.jdbc import init_db_instances

from src.signUp.signup import sign_up_route
from src.signIn.signIn import sign_in_route

api = Flask(__name__)
api.register_blueprint(sign_up_route, url_prefix='/api/users')
api.register_blueprint(sign_in_route, url_prefix='/api/users')

if __name__ == '__main__':
    db_config = set_environments()
    try:
        init_db_instances(db_config=db_config)
    except Exception as e:
        print(f"{e}")
        exit(code=400)
    api.run(debug=True)