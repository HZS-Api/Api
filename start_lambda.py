from flask_lambda import FlaskLambda
from src.app import main

http_server = main(FlaskLambda)
