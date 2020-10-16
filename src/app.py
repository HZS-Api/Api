import sys
from flask_injector import FlaskInjector
from src.controllers import incidents_blueprint
from src.config.dependencies import configure

def main(Flask):
    app = Flask(__name__)
    app.register_blueprint(incidents_blueprint)

    # Setup Flask Injector
    FlaskInjector(app=app, modules=[configure])

    return app
