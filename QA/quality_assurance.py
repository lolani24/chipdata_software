from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField,  BooleanField, ValidationError, TextAreaField, SelectField,IntegerField, FloatField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from extensions import db
from chipdata.models.chipdata import Batch, Wafer, Chip, OQA, EQA, LQA
from db_utils import get_or_create 


QA_blueprint = Blueprint('QA', __name__, template_folder='templates')

qa_success = False
eqa_success = False
lqa_success = False


#Creating functions to create complete data table 

#OQA Form 

class OQAForm(FlaskForm):
    channel_1 = SelectField('Channel 1', choices=[('Good'),('Bad')])
    channel_1_note = StringField('Notes')
    channel_2 = SelectField('Channel 2', choices=[('Good'),('Bad')])
    channel_2_note = StringField('Notes')
    channel_3 = SelectField('Channel 3', choices=[('Good'),('Bad')])
    channel_3_note = StringField('Notes')
    channel_4 = SelectField('Channel 4', choices=[('Good'),('Bad')])
    channel_4_note = StringField('Notes')
    channel_5 = SelectField('Channel 5', choices=[('Good'),('Bad')])
    channel_5_note = StringField('Notes')
    submit = SubmitField("Submit")


eqa_success=None
lqa_success=None

@QA_blueprint.route('/OQA/<int:chip_id>', methods=['POST', 'GET'])
def oqa(chip_id):
    oqa = None
    form = OQAForm()
    if form.validate_on_submit():
        chip_info = Chip.query.filter_by(id=chip_id).first()
        channels = get_or_create(db.session, OQA, channel_1= form.channel_1.data,channel_1_note=form.channel_1_note.data,
                                 channel_2=form.channel_2.data, channel_2_note=form.channel_2_note.data, channel_3=form.channel_3.data, 
                                 channel_3_note=form.channel_3_note.data, channel_4=form.channel_4.data, channel_4_note=form.channel_4_note.data, 
                                 channel_5=form.channel_5.data, channel_5_note=form.channel_5_note.data, chip_id = chip_info.id )
        form.channel_1.data =''
        form.channel_1_note.data = ''
        form.channel_2.data =''
        form.channel_2_note.data = ''
        form.channel_3.data = ''
        form.channel_3_note.data = ''
        form.channel_4.data =''
        form.channel_4_note.data = ''
        form.channel_5.data=''
        form.channel_5_note.data = ''
        return redirect(url_for('QA.successOQA',chip_id = chip_info.id))
    else:
        return render_template('qa.html', form = form, correct_login = True, before_login = False, qa_success = False)

@QA_blueprint.route('/successOQA/<int:chip_id>')
def successOQA(chip_id):
    chip_info = Chip.query.filter_by(id=chip_id).first()
    return render_template ('successOQA.html',  correct_login = True, before_login = False, chip_info=chip_info)


#EQA Form 

class EQAForm(FlaskForm):
    Reschannel_1 = FloatField('Channel 1 Resistance')
    Reschannel_2 = FloatField('Channel 2 Resistance')
    Reschannel_3 = FloatField('Channel 3 Resistance')
    Reschannel_4 = FloatField('Channel 4 Resistance')
    Reschannel_5 = FloatField('Channel 5 Resistance')
    submit = SubmitField("Submit")


@QA_blueprint.route('/EQA/<int:chip_id>', methods=['POST', 'GET'])
def eqa(chip_id):
    eqa = None
    form = EQAForm()
    if form.validate_on_submit():
        chip_info = Chip.query.filter_by(id=chip_id).first()
        channels = get_or_create(db.session, EQA, Reschannel_1= form.Reschannel_1.data,
                                 Reschannel_2=form.Reschannel_2.data, Reschannel_3=form.Reschannel_3.data,
                                 Reschannel_4=form.Reschannel_4.data, Reschannel_5=form.Reschannel_5.data,
                                  chip_id = chip_info.id )
        form.Reschannel_1.data =''
        form.Reschannel_2.data =''
        form.Reschannel_3.data = ''
        form.Reschannel_4.data =''
        form.Reschannel_5.data=''
        return redirect(url_for('QA.successEQA',chip_id = chip_info.id))
    else:
        return render_template('eqa.html', form = form, correct_login = True, before_login = False, eqa_success = False)

@QA_blueprint.route('/successOQA/<int:chip_id>')
def successEQA(chip_id):
    chip_info = Chip.query.filter_by(id=chip_id).first()
    return render_template ('successEQA.html',  correct_login = True, before_login = False, chip_info=chip_info)




#LQA Form 
class LQAForm(FlaskForm):
    channel_1_min = FloatField('Channel 1 Minimal Current')
    channel_1_max= FloatField('Channel 1 Maximum Current')
    channel_1_dirac_voltage = FloatField('Channel 1 Dirac Voltage')
    channel_1_slope = FloatField('Channel 1 Slope')
    
    channel_2_min = FloatField('Channel 2 Minimal Current')
    channel_2_max= FloatField('Channel 2 Maximum Current')
    channel_2_dirac_voltage = FloatField('Channel 2 Dirac Voltage')
    channel_2_slope = FloatField('Channel 2 Slope')

    channel_3_min = FloatField('Channel 3 Minimal Current')
    channel_3_max= FloatField('Channel 3 Maximum Current')
    channel_3_dirac_voltage = FloatField('Channel 3 Dirac Voltage')
    channel_3_slope = FloatField('Channel 3 Slope')

    channel_4_min = FloatField('Channel 4 Minimal Current')
    channel_4_max= FloatField('Channel 4 Maximum Current')
    channel_4_dirac_voltage = FloatField('Channel 4 Dirac Voltage')
    channel_4_slope = FloatField('Channel 4 Slope')

    channel_5_min = FloatField('Channel 5 Minimal Current')
    channel_5_max= FloatField('Channel 5 Maxium Current')
    channel_5_dirac_voltage = FloatField('Channel 5 Dirac Voltage')
    channel_5_slope = FloatField('Channel 5 Slope')

    submit = SubmitField("Submit")


@QA_blueprint.route('/LQA/<int:chip_id>', methods=['POST', 'GET'])
def lqa(chip_id):
    lqa = None
    form = LQAForm()
    if form.validate_on_submit():
        chip_info = Chip.query.filter_by(id=chip_id).first()
        channels = get_or_create(db.session, LQA, channel_1_min = form.channel_1_min.data, channel_1_max = form.channel_1_max.data, channel_1_dirac_voltage = form.channel_1_dirac_voltage.data, channel_1_slope = form.channel_1_slope.data, 
                    channel_2_min = form.channel_2_min.data, channel_2_max = form.channel_2_max.data, channel_2_dirac_voltage = form.channel_2_dirac_voltage.data, channel_2_slope = form.channel_2_slope.data, 
                    channel_3_min = form.channel_3_min.data, channel_3_max = form.channel_3_max.data, channel_3_dirac_voltage = form.channel_3_dirac_voltage.data, channel_3_slope = form.channel_3_slope.data, 
                    channel_4_min = form.channel_4_min.data, channel_4_max = form.channel_4_max.data, channel_4_dirac_voltage = form.channel_4_dirac_voltage.data, channel_4_slope = form.channel_4_slope.data, 
                    channel_5_min = form.channel_5_min.data, channel_5_max = form.channel_5_max.data, channel_5_dirac_voltage = form.channel_5_dirac_voltage.data, channel_5_slope = form.channel_5_slope.data,
                    chip_id = chip_info.id) 
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
        
        return redirect(url_for('QA.successLQA',chip_id = chip_info.id))
    else:
        return render_template('lqa.html', form = form, correct_login = True, before_login = False, lqa_success = False)

@QA_blueprint.route('/successLQA/<int:chip_id>')
def successLQA(chip_id):
    chip_info = Chip.query.filter_by(id=chip_id).first()
    return render_template ('successLQA.html',  correct_login = True, before_login = False, chip_info=chip_info)

#Update Forms Buttons
@QA_blueprint.route('/update/<int:chip_id>')
def update(chip_id):
    chip_info = Chip.query.filter_by(id=chip_id).first()
    return render_template ('updateButtons.html',  correct_login = True, before_login = False, chip_info=chip_info)


#Update OQA Form 
@QA_blueprint.route('/updateoqa/<int:chip_id>', methods=['GET', 'POST'])
def update_OQA(chip_id):
    chip_info = Chip.query.filter_by(id=chip_id).first()
    oqa = OQA.query.filter(OQA.chip_id == chip_id).first()
    if request.method =='POST':
        form = OQAForm(formdata=request.form, obj=oqa)
        form.populate_obj(oqa)
        db.session.commit()
        flash('Updated Successfully!')
        return redirect(url_for('QA.successOQA', chip_id=oqa.chip_id))
    form = OQAForm(obj=oqa)
    return render_template('updateOQA.html', oqa=oqa, form=form,chip_info=chip_info, correct_login = True, before_login = False)


#Update EQA Form 
@QA_blueprint.route('/updateqa/<int:chip_id>', methods=['GET', 'POST'])
def update_EQA(chip_id):
    chip_info = Chip.query.filter_by(id=chip_id).first()
    eqa = EQA.query.filter(EQA.chip_id == chip_id).first()
    if request.method =='POST':
        form = EQAForm(formdata=request.form, obj=eqa)
        form.populate_obj(eqa)
        db.session.commit()
        flash('Updated Successfully!')
        return redirect(url_for('QA.successEQA', chip_id=eqa.chip_id))
    form = EQAForm(obj=eqa)
    return render_template('updateEQA.html', eqa=eqa, form=form,chip_info=chip_info, correct_login = True, before_login = False)


#Update LQA Form 
@QA_blueprint.route('/updatelqa/<int:chip_id>', methods=['GET', 'POST'])
def update_LQA(chip_id):
    chip_info = Chip.query.filter_by(id=chip_id).first()
    lqa = LQA.query.filter(LQA.chip_id == chip_id).first()
    if request.method =='POST':
        form = LQAForm(formdata=request.form, obj=lqa)
        form.populate_obj(lqa)
        db.session.commit()
        flash('Updated Successfully!')
        return redirect(url_for('QA.successLQA', chip_id=lqa.chip_id))
    form = LQAForm(obj=lqa)
    return render_template('updateLQA.html', lqa=lqa, form=form,chip_info=chip_info, correct_login = True, before_login = False)