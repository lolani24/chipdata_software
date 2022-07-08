from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField, SelectField,IntegerField, FloatField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from extensions import db
from chipdata.models.chipdata import QA, EQA


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
    qa = None
    form = QAForm()
    if form.validate_on_submit():
        qa = QA(channel_1=form.channel_1.data, channel_2=form.channel_2.data, channel_3=form.channel_3.data, channel_4=form.channel_4.data, channel_5=form.channel_5.data) 
        db.session.add(qa)
        db.session.commit()
        form.channel_1.data =''
        form.channel_2.data =''
        form.channel_3.data = ''
        form.channel_4.data =''
        form.channel_5.data=''
    return render_template('qa.html', form=form, correct_login = True, before_login = False)



class EQAForm(FlaskForm):
    Reschannel_1 = FloatField('Channel 1 Resistance', validators=[DataRequired()])
    Reschannel_2 = FloatField('Channel 2 Resistance', validators=[DataRequired()])
    Reschannel_3 = FloatField('Channel 3 Resistance', validators=[DataRequired()])
    Reschannel_4 = FloatField('Channel 4 Resistance', validators=[DataRequired()])
    Reschannel_5 = FloatField('Channel 5 Resistance', validators=[DataRequired()])
    submit = SubmitField("Submit")


@QA_blueprint.route('/EQA', methods=['POST', 'GET'])
def eqa():
    eqa = None
    form = EQAForm()
    if form.validate_on_submit():
        eqa = EQA(Reschannel_1=form.Reschannel_1.data, Reschannel_2=form.Reschannel_2.data, Reschannel_3=form.Reschannel_3.data, Reschannel_4=form.Reschannel_4.data, Reschannel_5=form.Reschannel_5.data) 
        db.session.add(eqa)
        db.session.commit()
        form.Reschannel_1.data =''
        form.Reschannel_2.data =''
        form.Reschannel_3.data = ''
        form.Reschannel_4.data =''
        form.Reschannel_5.data=''
    return render_template('eqa.html', form=form, correct_login = True, before_login = False)