from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from extensions import db
from chipdata.models.chipdata import QA


QA_blueprint = Blueprint('QA', __name__, template_folder='templates')

class QAForm(FlaskForm):
        channel_1 = StringField("Channel 1", validators=[DataRequired()])
        channel_2 = StringField("Channel 2", validators=[DataRequired()])
        channel_3 = StringField("Channel 3", validators=[DataRequired()])
        channel_4 = StringField("Channel 4", validators=[DataRequired()])
        channel_5 = StringField("Channel 5", validators=[DataRequired()])
        submit = SubmitField("Submit")

@QA_blueprint.route('/', methods=['POST', 'GET'])
def qa():
    form = QAForm()
    if form.validate_on_submit():
        qa = QA.query.filter_by(channel_1=form.channel_1.data).first()
        if qa is None:
            qa = QA(channel_1=form.channel_1.data, channel_2=form.channel_2.data, channel_3=form.channel_3.data, channel_4=form.channel_4.data, channel_5=form.channel_5.data) 
           
            db.session.add(qa)
            db.session.commit()
        form.channel_1.data =''
        form.channel_2.data =''
        form.channel_3.data = ''
        form.channel_4.data =''
        form.channel_5.data=''
    return render_template('qa.html', form=form)
