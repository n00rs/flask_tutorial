from flask import Blueprint

views = Blueprint("views",__name__)

# define routes for views

@views.route("/")
def hello():
    return "<h1>Hello world views</h1>"