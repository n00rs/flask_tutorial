from flask import Blueprint,render_template
# import methods to check user session exist
from flask_login import current_user,login_required


views = Blueprint("views",__name__)

# define routes for views

@views.route("/")
@login_required
def home():
    return render_template("home.html")