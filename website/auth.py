from flask import Blueprint

# 
auth = Blueprint("auth",__name__)

@auth.route("/")
def hello():
    return "<h1> Hello World Auth </h1> "