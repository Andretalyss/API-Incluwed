from dotenv import load_dotenv
import os

def set_environments():
    load_dotenv()

    db_config = {
        'database': os.getenv('DB_DATABASE'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }

    return db_config

def set_environments_with_secret():
    load_dotenv()

    secret = os.getenv('SECRET_TOKEN')

    db_config = {
        'database': os.getenv('DB_DATABASE'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }

    return db_config, secret