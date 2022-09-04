from flask import Flask

def create_app():
    app=Flask(__name__)

    from first_flask.user.views import req as http_req

    app.register_blueprint(http_req)
    return app
