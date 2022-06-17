from flask import Blueprint, render_template

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

@auth_blueprint.route('/login')
def login():
    return render_template("login.html")

@auth_blueprint.route('/signup')
def signup():
    return "signup page"

@auth_blueprint.route('/signout')
def signout():
    return "signout page"

@auth_blueprint.route('/logout')
def logout():
    return "logout page"