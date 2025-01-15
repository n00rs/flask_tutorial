from flask import Blueprint,render_template

views = Blueprint("views",__name__)

# define routes for views

@views.route("/")
def hello():
    return render_template("home.html")