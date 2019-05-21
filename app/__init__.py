import os
from flask import Flask, request, current_app
from app_config import Config 

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init all the lib package here
    

    # Registering Blueprint 
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.general import bp as general_bp
    app.register_blueprint(general_bp)
    app.add_url_rule('/', endpoint="index")

    return app