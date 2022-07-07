from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from extensions import db
from chipdata.models.chipdata import QA


QA_blueprint = Blueprint('QA', __name__, template_folder='templates')




class QAForm(FlaskForm):
    channel_1 = SelectField('Channel 1', choices=[('Good'),('Bad')])
    channel_2 = SelectField('Channel 2', choices=[('Good'),('Bad')])
    channel_3 = SelectField('Channel 3', choices=[('Good'),('Bad')])
    channel_4 = SelectField('Channel 4', choices=[('Good'),('Bad')])
    channel_5 = SelectField('Channel 5', choices=[('Good'),('Bad')])
    submit = SubmitField("Submit")

@QA_blueprint.route('/OQA', methods=['POST', 'GET'])
def qa():
    form = QAForm()
    if form.validate_on_submit():
        qa = QA.query.order_by(QA.channel_1, QA.channel_2).all()
        print(qa)
        if qa is None:
            qa = QA(channel_1=form.channel_1.data, channel_2=form.channel_2.data, channel_3=form.channel_3.data, channel_4=form.channel_4.data, channel_5=form.channel_5.data) 
            db.session.add(qa)
            db.session.commit()
        form.channel_1.data =''
        form.channel_2.data =''
        form.channel_3.data = ''
        form.channel_4.data =''
        form.channel_5.data=''
    return render_template('qa.html', form=form, correct_login = True, before_login = False)
