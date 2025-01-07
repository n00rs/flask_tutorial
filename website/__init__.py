from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # importing blue prints from auth and view
    from .auth import auth
    from .views import views
    
    app.register_blueprint(auth,url_prefix="/auth")
    app.register_blueprint(views,url_prefix = "/")
    return app