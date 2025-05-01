from flask import Blueprint

hello_blueprint = Blueprint('hello', __name__)

@hello_blueprint.route("/hello", methods=["GET"])
def say_hello():
    return {"message": "Hello, Flask is running!"}
