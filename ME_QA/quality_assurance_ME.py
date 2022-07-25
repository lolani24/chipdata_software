from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField,  BooleanField, ValidationError, TextAreaField, SelectField,IntegerField, FloatField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from extensions import db
from chipdata.models.chipdata import Batch, Wafer, Chip, OQA, EQA, LQA, BatchME, WaferME, ChipME, OQAme, EQAme, LQAme
from db_utils import get_or_create 


QA_ME_blueprint = Blueprint('QA_ME', __name__, template_folder='templates')

qa_success = False
eqa_success = False
lqa_success = False

#Creating functions to create complete data table 

#ME Chip OQA Form 


class OQAmeForm(FlaskForm):
    channel_1_ME = SelectField('Channel 1', choices=[('Good'),('Bad')])
    channel_1_note_ME = StringField('Notes')
    channel_2_ME = SelectField('Channel 2', choices=[('Good'),('Bad')])
    channel_2_note_ME = StringField('Notes')
    channel_3_ME = SelectField('Channel 3', choices=[('Good'),('Bad')])
    channel_3_note_ME = StringField('Notes')
    channel_4_ME = SelectField('Channel 4', choices=[('Good'),('Bad')])
    channel_4_note_ME = StringField('Notes')
    channel_5_ME = SelectField('Channel 5', choices=[('Good'),('Bad')])
    channel_5_note_ME = StringField('Notes')
    submit = SubmitField("Submit")


eqa_success=None
lqa_success=None

@QA_ME_blueprint.route('/OQAme/<int:chipME_id>', methods=['POST', 'GET'])
def oqaME(chipME_id):
    oqaME = None
    form = OQAmeForm()
    if form.validate_on_submit():
        chipME_info = ChipME.query.filter_by(id=chipME_id).first()
        ME_channels = get_or_create(db.session, OQAme, channel_1_ME= form.channel_1_ME.data,channel_1_note_ME=form.channel_1_note_ME.data,
                                 channel_2_ME=form.channel_2_ME.data, channel_2_note_ME=form.channel_2_note_ME.data, channel_3_ME=form.channel_3_ME.data, 
                                 channel_3_note_ME=form.channel_3_note_ME.data, channel_4_ME=form.channel_4_ME.data, channel_4_note_ME=form.channel_4_note_ME.data, 
                                 channel_5_ME=form.channel_5_ME.data, channel_5_note_ME=form.channel_5_note_ME.data, chipME_id = chipME_info.id )
        form.channel_1_ME.data =''
        form.channel_1_note_ME.data = ''
        form.channel_2_ME.data =''
        form.channel_2_note_ME.data = ''
        form.channel_3_ME.data = ''
        form.channel_3_note_ME.data = ''
        form.channel_4_ME.data =''
        form.channel_4_note_ME.data = ''
        form.channel_5_ME.data=''
        form.channel_5_note_ME.data = ''
        return redirect(url_for('QA_ME.successOQAme',chipME_id = chipME_info.id))
    else:
        chipME_info = ChipME.query.filter_by(id=chipME_id).first()
        return render_template('oqaME.html', form = form, correct_login = True, before_login = False, qa_success = False, chipME_info=chipME_info)

@QA_ME_blueprint.route('/successOQAme/<int:chipME_id>')
def successOQAme(chipME_id):
    chipME_info = ChipME.query.filter_by(id=chipME_id).first()
    return render_template ('successOQAme.html',  correct_login = True, before_login = False, chipME_info=chipME_info)
#EQA Form 

class EQAmeForm(FlaskForm):
    Reschannel_1_ME = FloatField('Channel 1 Resistance')
    Reschannel_2_ME = FloatField('Channel 2 Resistance')
    Reschannel_3_ME = FloatField('Channel 3 Resistance')
    Reschannel_4_ME = FloatField('Channel 4 Resistance')
    Reschannel_5_ME = FloatField('Channel 5 Resistance')
    submit = SubmitField("Submit")


@QA_ME_blueprint.route('/EQAme/<int:chipME_id>', methods=['POST', 'GET'])
def eqaME(chipME_id):
    eqaME = None
    form = EQAmeForm()
    if form.validate_on_submit():
        chipME_info = ChipME.query.filter_by(id=chipME_id).first()
        ME_channels = get_or_create(db.session, EQAme, Reschannel_1_ME= form.Reschannel_1_ME.data,
                                 Reschannel_2_ME=form.Reschannel_2_ME.data, Reschannel_3_ME=form.Reschannel_3_ME.data,
                                 Reschannel_4_ME=form.Reschannel_4_ME.data, Reschannel_5_ME=form.Reschannel_5_ME.data,
                                  chipME_id = chipME_info.id )
        form.Reschannel_1_ME.data =''
        form.Reschannel_2_ME.data =''
        form.Reschannel_3_ME.data = ''
        form.Reschannel_4_ME.data =''
        form.Reschannel_5_ME.data=''
        return redirect(url_for('QA_ME.successEQAme',chipME_id = chipME_info.id))
    else:
        chipME_info = ChipME.query.filter_by(id=chipME_id).first()
        return render_template('eqaME.html', form = form, chipME_info=chipME_info, correct_login = True, before_login = False, eqa_success = False)

@QA_ME_blueprint.route('/successEQAme/<int:chipME_id>')
def successEQAme(chipME_id):
    chipME_info = ChipME.query.filter_by(id=chipME_id).first()
    return render_template ('successEQAme.html',  correct_login = True, before_login = False, chipME_info=chipME_info)

#LQA Form 
class LQAmeForm(FlaskForm):
    channel_1_min_ME = FloatField('Channel 1 Minimal Current')
    channel_1_max_ME= FloatField('Channel 1 Maximum Current')
    channel_1_dirac_voltage_ME = FloatField('Channel 1 Dirac Voltage')
    channel_1_slope_ME = FloatField('Channel 1 Slope')
    
    channel_2_min_ME = FloatField('Channel 2 Minimal Current')
    channel_2_max_ME= FloatField('Channel 2 Maximum Current')
    channel_2_dirac_voltage_ME = FloatField('Channel 2 Dirac Voltage')
    channel_2_slope_ME = FloatField('Channel 2 Slope')

    channel_3_min_ME = FloatField('Channel 3 Minimal Current')
    channel_3_max_ME= FloatField('Channel 3 Maximum Current')
    channel_3_dirac_voltage_ME = FloatField('Channel 3 Dirac Voltage')
    channel_3_slope_ME = FloatField('Channel 3 Slope')

    channel_4_min_ME = FloatField('Channel 4 Minimal Current')
    channel_4_max_ME = FloatField('Channel 4 Maximum Current')
    channel_4_dirac_voltage_ME = FloatField('Channel 4 Dirac Voltage')
    channel_4_slope_ME = FloatField('Channel 4 Slope')

    channel_5_min_ME = FloatField('Channel 5 Minimal Current')
    channel_5_max_ME = FloatField('Channel 5 Maxium Current')
    channel_5_dirac_voltage_ME = FloatField('Channel 5 Dirac Voltage')
    channel_5_slope_ME = FloatField('Channel 5 Slope')

    submit = SubmitField("Submit")


@QA_ME_blueprint.route('/LQAme/<int:chipME_id>', methods=['POST', 'GET'])
def lqaME(chipME_id):
    lqaME = None
    form = LQAmeForm()
    if form.validate_on_submit():
        chipME_info = ChipME.query.filter_by(id=chipME_id).first()
        ME_channels = get_or_create(db.session, LQAme, channel_1_min_ME = form.channel_1_min_ME.data, channel_1_max_ME = form.channel_1_max_ME.data, channel_1_dirac_voltage_ME = form.channel_1_dirac_voltage_ME.data, channel_1_slope_ME = form.channel_1_slope_ME.data, 
                    channel_2_min_ME = form.channel_2_min_ME.data, channel_2_max_ME = form.channel_2_max_ME.data, channel_2_dirac_voltage_ME = form.channel_2_dirac_voltage_ME.data, channel_2_slope_ME = form.channel_2_slope_ME.data, 
                    channel_3_min_ME = form.channel_3_min_ME.data, channel_3_max_ME = form.channel_3_max_ME.data, channel_3_dirac_voltage_ME = form.channel_3_dirac_voltage_ME.data, channel_3_slope_ME = form.channel_3_slope_ME.data, 
                    channel_4_min_ME = form.channel_4_min_ME.data, channel_4_max_ME = form.channel_4_max_ME.data, channel_4_dirac_voltage_ME = form.channel_4_dirac_voltage_ME.data, channel_4_slope_ME = form.channel_4_slope_ME.data, 
                    channel_5_min_ME = form.channel_5_min_ME.data, channel_5_max_ME = form.channel_5_max_ME.data, channel_5_dirac_voltage_ME = form.channel_5_dirac_voltage_ME.data, channel_5_slope_ME = form.channel_5_slope_ME.data,
                    chipME_id = chipME_info.id) 
        form.channel_1_min_ME.data = ''
        form.channel_1_max_ME.data = ''
        form.channel_1_slope_ME.data = ''
        form.channel_2_min_ME.data = ''
        form.channel_2_max_ME.data = ''
        form.channel_2_slope_ME.data = ''
        form.channel_3_min_ME.data = ''
        form.channel_3_max_ME.data = ''
        form.channel_3_slope_ME.data = ''
        form.channel_4_min_ME.data = ''
        form.channel_4_max_ME.data = ''
        form.channel_4_slope_ME.data = ''
        form.channel_5_min_ME.data = ''
        form.channel_5_max_ME.data = ''
        form.channel_5_slope_ME.data = ''
        
        return redirect(url_for('QA_ME.successLQAme',chipME_id = chipME_info.id))
    else:
        chipME_info = ChipME.query.filter_by(id=chipME_id).first()
        return render_template('lqaME.html', form = form, correct_login = True, before_login = False, lqa_success = False, chipME_info=chipME_info)

@QA_ME_blueprint.route('/successLQAme/<int:chipME_id>')
def successLQAme(chipME_id):
    chipME_info = ChipME.query.filter_by(id=chipME_id).first()
    return render_template ('successLQAme.html',  correct_login = True, before_login = False, chipME_info=chipME_info)


#Update Forms Buttons
@QA_ME_blueprint.route('/updateME/<int:chipME_id>')
def updateME(chipME_id):
    chipME_info = ChipME.query.filter_by(id=chipME_id).first()
    return render_template ('updateButtonsME.html',  correct_login = True, before_login = False, chipME_info=chipME_info)


#Update OQA Form 
@QA_ME_blueprint.route('/updateoqaME/<int:chipME_id>', methods=['GET', 'POST'])
def update_OQAme(chipME_id):
    chipME_info = ChipME.query.filter_by(id=chipME_id).first()
    oqaME = OQAme.query.filter(OQAme.chipME_id == chipME_id).first()
    if request.method =='POST':
        form = OQAmeForm(formdata=request.form, obj=oqaME)
        form.populate_obj(oqaME)
        db.session.commit()
        flash('Updated Successfully!')
        return redirect(url_for('QA_ME.successOQAme', chipME_id=oqaME.chipME_id))
    form = OQAmeForm(obj=oqaME)
    return render_template('updateOQAme.html', oqaME=oqaME, form=form, chipME_info=chipME_info, correct_login = True, before_login = False)


#Update EQA Form 
@QA_ME_blueprint.route('/updateqaME/<int:chipME_id>', methods=['GET', 'POST'])
def update_EQAme(chipME_id):
    chipME_info = ChipME.query.filter_by(id=chipME_id).first()
    eqaME = EQAme.query.filter(EQAme.chipME_id == chipME_id).first()
    if request.method =='POST':
        form = EQAmeForm(formdata=request.form, obj=eqaME)
        form.populate_obj(eqaME)
        db.session.commit()
        flash('Updated Successfully!')
        return redirect(url_for('QA_ME.successEQAme', chipME_id=eqaME.chipME_id))
    form = EQAmeForm(obj=eqaME)
    return render_template('updateEQAme.html', eqaME=eqaME, form=form,chipME_info=chipME_info, correct_login = True, before_login = False)


#Update LQA Form 
@QA_ME_blueprint.route('/updatelqaME/<int:chipME_id>', methods=['GET', 'POST'])
def update_LQAme(chipME_id):
    chipME_info = ChipME.query.filter_by(id=chipME_id).first()
    lqaME = LQAme.query.filter(LQAme.chipME_id == chipME_id).first()
    if request.method =='POST':
        form = LQAmeForm(formdata=request.form, obj=lqaME)
        form.populate_obj(lqaME)
        db.session.commit()
        flash('Updated Successfully!')
        return redirect(url_for('QA_ME.successLQAme', chipME_id=lqaME.chipME_id))
    form = LQAmeForm(obj=lqaME)
    return render_template('updateLQAme.html', lqaME=lqaME, form=form,chipME_info=chipME_info, correct_login = True, before_login = False)