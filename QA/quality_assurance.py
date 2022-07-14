from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField, SelectField,IntegerField, FloatField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from extensions import db
from chipdata.models.chipdata import Batch, Wafer, Chip, OQA, EQA, LQA
from db_utils import get_or_create #either finds an exisiting row or creates a new one 



QA_blueprint = Blueprint('QA', __name__, template_folder='templates')

qa_success = False
eqa_success = False
lqa_success = False

#OQA Form 

class OQAForm(FlaskForm):
    channel_1 = SelectField('Channel 1', choices=[('Good'),('Bad')])
    channel_2 = SelectField('Channel 2', choices=[('Good'),('Bad')])
    channel_3 = SelectField('Channel 3', choices=[('Good'),('Bad')])
    channel_4 = SelectField('Channel 4', choices=[('Good'),('Bad')])
    channel_5 = SelectField('Channel 5', choices=[('Good'),('Bad')])
    submit = SubmitField("Submit")

qa_success=None
eqa_success=None
lqa_success=None

@QA_blueprint.route('/OQA', methods=['POST', 'GET'])
def oqa():
    oqa = None
    form = OQAForm()
    if form.validate_on_submit():
        oqa = OQA(channel_1=form.channel_1.data, channel_2=form.channel_2.data, channel_3=form.channel_3.data, channel_4=form.channel_4.data, channel_5=form.channel_5.data) 
        db.session.add(oqa)
        db.session.commit()
        form.channel_1.data =''
        form.channel_2.data =''
        form.channel_3.data = ''
        form.channel_4.data =''
        form.channel_5.data=''
        return render_template('qa.html', form=form, correct_login = True, before_login = False, qa_success=True)
    else:
        return render_template('qa.html', form = form, correct_login = True, before_login = False, qa_success = False)


#EQA Form 

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
        return render_template('eqa.html', form=form, correct_login = True, before_login = False, eqa_success=True)
    else:
        return render_template('eqa.html', form = form, correct_login = True, before_login = False, eqa_success = False)




#LQA Form 
class LQAForm(FlaskForm):
    channel_1_min = FloatField('Channel 1 Minimal Current', validators=[DataRequired()])
    channel_1_max= FloatField('Channel 1 Maximum Current', validators=[DataRequired()])
    channel_1_slope = FloatField('Channel 1 Slope', validators=[DataRequired()])
    channel_2_min = FloatField('Channel 2 Minimal Current', validators=[DataRequired()])
    channel_2_max= FloatField('Channel 2 Maximum Current', validators=[DataRequired()])
    channel_2_slope = FloatField('Channel 2 Slope', validators=[DataRequired()])
    channel_3_min = FloatField('Channel 3 Minimal Current', validators=[DataRequired()])
    channel_3_max= FloatField('Channel 3 Maximum Current', validators=[DataRequired()])
    channel_3_slope = FloatField('Channel 3 Slope', validators=[DataRequired()])
    channel_4_min = FloatField('Channel 4 Minimal Current', validators=[DataRequired()])
    channel_4_max= FloatField('Channel 4 Maximum Current', validators=[DataRequired()])
    channel_4_slope = FloatField('Channel 4 Slope', validators=[DataRequired()])
    channel_5_min = FloatField('Channel 5 Minimal Current', validators=[DataRequired()])
    channel_5_max= FloatField('Channel 5 Maxium Current', validators=[DataRequired()])
    channel_5_slope = FloatField('Channel 5 Slope', validators=[DataRequired()])
    submit = SubmitField("Submit")


@QA_blueprint.route('/LQA', methods=['POST', 'GET'])
def lqa():
    lqa = None
    form = LQAForm()
    if form.validate_on_submit():
        lqa = LQA(channel_1_min = form.channel_1_min.data, channel_1_max = form.channel_1_max.data, channel_1_slope = form.channel_1_slope.data, channel_2_min = form.channel_2_min.data, channel_2_max = form.channel_2_max.data, channel_2_slope = form.channel_2_slope.data, channel_3_min = form.channel_3_min.data, channel_3_max = form.channel_3_max.data, channel_3_slope = form.channel_3_slope.data, channel_4_min = form.channel_4_min.data, channel_4_max = form.channel_4_max.data, channel_4_slope = form.channel_4_slope.data, channel_5_min = form.channel_5_min.data, channel_5_max = form.channel_5_max.data, channel_5_slope = form.channel_5_slope.data) 
        db.session.add(lqa)
        db.session.commit()
        form.channel_1_min.data = ''
        form.channel_1_max.data = ''
        form.channel_1_slope.data = ''
        form.channel_2_min.data = ''
        form.channel_2_max.data = ''
        form.channel_2_slope.data = ''
        form.channel_3_min.data = ''
        form.channel_3_max.data = ''
        form.channel_3_slope.data = ''
        form.channel_4_min.data = ''
        form.channel_4_max.data = ''
        form.channel_4_slope.data = ''
        form.channel_5_min.data = ''
        form.channel_5_max.data = ''
        form.channel_5_slope.data = ''
        
        return render_template('lqa.html', form=form, correct_login = True, before_login = False, lqa_success = True)
    else:
        return render_template('lqa.html', form = form, correct_login = True, before_login = False, lqa_success = False)
