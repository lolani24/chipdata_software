from flask import Flask, render_template, url_for
from extensions import db
from datetime import datetime
from flask_migrate import Migrate
import os
from dotenv import load_dotenv



from login.auth import auth_blueprint
from homepage.home import home_blueprint
from chipdata.basicinfo import chip_blueprint
from QA.quality_assurance import QA_blueprint
from ME_QA.quality_assurance_ME import QA_ME_blueprint
from ME_QA.basicinfo_ME import chip_ME_blueprint



def create_app():
   app = Flask(__name__)
   load_dotenv()
   SQL_DSN = os.getenv('DATABASE_URL')
   print(SQL_DSN)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'SQL_DSN'
 

   migrate = Migrate(app, db)
   
   
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   app.config['SECRET_KEY'] = "zxcvbnm,"

   db.init_app(app)



   app.register_blueprint(auth_blueprint, url_prefix='/auth')
   app.register_blueprint(home_blueprint, url_prefix='/home')
   app.register_blueprint(chip_blueprint, url_prefix='/chip')
   app.register_blueprint(chip_ME_blueprint, url_prefix='/chipME')
   app.register_blueprint(QA_blueprint, url_prefix='/QA')
   app.register_blueprint(QA_ME_blueprint, url_prefix='/QA_ME')


   @app.route('/')
   def test():
      return render_template("login.html")

   return app

