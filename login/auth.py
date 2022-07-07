from pickle import FALSE, TRUE
from pip import main
from flask import Blueprint, render_template, request

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

correct_login = None
before_login = True
incorrect_login = None
 
@auth_blueprint.route('/login')
def login():
    return render_template("login.html")
   
@auth_blueprint.route('/login', methods =["GET", "POST"])
def authorize():
    if request.method == "POST":
        p_username = request.form.get("fusername")  
        p_password = request.form.get("fpassword")
        if p_username == "aranlab" and p_password == "andres_23":
            return render_template("home.html", correct_login = True, before_login = False)
        else:
            return render_template("login.html", incorrect_login = True)
    else:
        return "Invalid Method" 
                            
@auth_blueprint.route('/logout')
def logout():
    return render_template("logout.html")
 
 
#user aranlab
#password andres_23
# round 11