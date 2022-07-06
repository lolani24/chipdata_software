from flask import Blueprint, render_template, url_for 
#from login.auth import authorize, correct_login
#if correct_login == True, go to home, elif correct_login == False go to login
home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
def home():
    return render_template("home.html")

