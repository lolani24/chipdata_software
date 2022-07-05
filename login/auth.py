from pickle import FALSE, TRUE
from pip import main
from flask import Blueprint, render_template, request 

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

if __name__=='__main__':
    auth_blueprint.run()

@auth_blueprint.route('/login', methods=["GET", "POST"])
def login():
    return render_template("login.html")
def authorize():
    if request.method == "POST": 
        p_username = request.form.get("fusername")  
        p_password = request.form.get("fpassword") 
        if p_username == "aranlab" and p_password == "andres_23":
            return render_template("home.html")
        else:
            return "Incorrect Login Information"
    else:
        return "Invalid Method"

@auth_blueprint.route('/logout')
def logout():
    return "logout page"


#user aranlab
#password andres_23
