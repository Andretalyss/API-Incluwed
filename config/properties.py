import boto3, json

def set_environments():
    ssm_client = boto3.client('ssm', region_name='us-east-1')
    parameter_name = '/api/env/json'

    try:
        response = ssm_client.get_parameter(
            Name=parameter_name,
            WithDecryption=False
        )

        # print(response['Parameter']['Value'])
        dados = json.loads(response['Parameter']['Value'])

        DB_HOST=dados['DB_HOST']
        DB_USER=dados['DB_USER']
        DB_PASSWORD=dados['DB_PASSWORD']
        DB_DATABASE=dados['DB_DATABASE']
        DB_PORT=dados['DB_PORT']

        db_config = {
            'database': DB_DATABASE,
            'user': DB_USER,
            'password': DB_PASSWORD,
            'host': DB_HOST,
            'port': DB_PORT
        }

        return db_config

    except ssm_client.exceptions.ParameterNotFound:
        print("Não existe o parametro")
    except Exception as e:
        print(f"{e}")

   
def set_environments_with_secret():
    ssm_client = boto3.client('ssm', region_name='us-east-1')
    parameter_name = '/api/env/json'

    try:
        response = ssm_client.get_parameter(
            Name=parameter_name,
            WithDecryption=False
        )

        # print(response['Parameter']['Value'])
        dados = json.loads(response['Parameter']['Value'])

        DB_HOST=dados['DB_HOST']
        DB_USER=dados['DB_USER']
        DB_PASSWORD=dados['DB_PASSWORD']
        DB_DATABASE=dados['DB_DATABASE']
        DB_PORT=dados['DB_PORT']
        secret=dados['SECRET_TOKEN']

        db_config = {
            'database': DB_DATABASE,
            'user': DB_USER,
            'password': DB_PASSWORD,
            'host': DB_HOST,
            'port': DB_PORT
        }

        return db_config, secret
    except ssm_client.exceptions.ParameterNotFound:
        print("Não existe o parametro")
    except Exception as e:
        print(f"{e}")
