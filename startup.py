from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#create a Flask Instance 
app = Flask(__name__)
app.config['SECRET_KEY'] = "only for learning purposes"
app.config['SQLALCHEMY_DATABASE_URL']= 'sqlite:///db.sqlite'


#create a route decorator (creating the url)
@app.route('/') #homepage
def index():
    front = "this is the home page"
    return render_template("index.html", front=front)

#create Custom Error Pages 

#Invalid URL 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

#Login Page 
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method =='POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else: 
            return redirect(url_for('home'))
    return render_template('login.html', error=error)



# Create a Form Class 
class ChipForm(FlaskForm):
    chip_ID =  IntegerField("Chip ID", validators=[DataRequired()])
    batch_number =  IntegerField('Batch Number', validators=[DataRequired()])
    wafer_number = IntegerField('Wafer Number', validators=[DataRequired()])
    submit = SubmitField("Submit")


#create chip data form 
@app.route('/chipdata', methods=['GET', 'POST'])
def chipdata():
    chip_ID = None
    form = ChipForm()
    return render_template("chipbasicinfo.html", chipdata=chipdata,form=form )

