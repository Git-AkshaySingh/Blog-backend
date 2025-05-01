from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.hello_routes import hello_blueprint
    app.register_blueprint(hello_blueprint)

    return app
