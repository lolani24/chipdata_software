from flask import Flask, render_template, url_for
from extensions import db
from datetime import datetime
from flask_migrate import Migrate





from login.auth import auth_blueprint
from homepage.home import home_blueprint
from chipdata.basicinfo import chip_blueprint
from QA.quality_assurance import QA_blueprint
from ME_QA.quality_assurance_ME import QA_ME_blueprint
from ME_QA.basicinfo_ME import chip_ME_blueprint




def create_app():
   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pltcvhrinlycrp:713a98e467e100c4b8f2308e34eef37900d47060f243687ee336760181b51af3@ec2-44-206-214-233.compute-1.amazonaws.com:5432/deh52hi6ntqf4r'
   
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

