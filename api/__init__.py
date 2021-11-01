from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = '3HUKw39wfrHK6a1ipZE71MP30JM0fhRV'
    from .views import main
    app.register_blueprint(main)

    return app
