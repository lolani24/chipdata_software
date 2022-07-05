from flask import Flask, render_template, url_for
from extensions import db
from datetime import datetime



from login.auth import auth_blueprint
from homepage.home import home_blueprint
from chipdata.basicinfo import chip_blueprint
from QA.quality_assurance import QA_blueprint
 


def create_app():
   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chip.db'
   

   
   
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   app.config['SECRET_KEY'] = "zxcvbnm,"

   db.init_app(app)



   app.register_blueprint(auth_blueprint, url_prefix='/auth')
   app.register_blueprint(home_blueprint, url_prefix='/home')
   app.register_blueprint(chip_blueprint, url_prefix='/chip')
   app.register_blueprint(QA_blueprint, url_prefix='/QA')


   @app.route('/')
   def test():
      return "test"

   return app


   #run test 12
