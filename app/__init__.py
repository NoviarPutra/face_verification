from flask import Flask
from flask_cors import CORS

from deepface import DeepFace
from app.api.routes import blueprint, logger


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(blueprint)
    logger.info(f"Welcome to DeepFace API v{DeepFace.__version__}!")
    return app
