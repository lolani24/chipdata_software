from flask import Blueprint, render_template, url_for 
from login.auth import authorize, correct_login, before_login
home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
def home():
    return render_template("home.html", correct_login = True, before_login = False)

