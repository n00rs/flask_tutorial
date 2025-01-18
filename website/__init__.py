from flask import Flask
# import SQLAlchemy to handle db
from flask_sqlalchemy import SQLAlchemy
# import path from os for checking whether db exists
from os import path
# import login manager from flask login module 
from flask_login import LoginManager
# call SQLAlchemy 
db = SQLAlchemy()
# database name
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # configuration for SQLALCHEMY to save db
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    
    # to initialize db call init_app method and pass flask app
    db.init_app(app)
    
    # importing blue prints from auth and view
    from .auth import auth
    from .views import views
    
    app.register_blueprint(auth,url_prefix="/auth")
    app.register_blueprint(views,url_prefix = "/")
    
    from .models import Note,User
    
    create_database(app)
    
    '''
    call LoginManager and set default view if not logged in
    '''
    login_manager =  LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app=app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app: Flask):
    if not path.exists('website/'+DB_NAME):
        with app.app_context():
            db.create_all()