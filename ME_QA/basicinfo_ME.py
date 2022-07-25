from pickle import NONE
from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField,SelectField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from extensions import db
from chipdata.models.chipdata import Batch, Wafer, Chip, OQA, EQA, LQA, BatchME, WaferME, ChipME, OQAme, EQAme, LQAme
from db_utils import get_or_create #either finds an exisiting row or creates a new one 


chip_ME_blueprint = Blueprint('chipME', __name__, template_folder='templates')

chipME_info_v = None


#Basic Chip Information Form
class ChipMEForm(FlaskForm):
	chipME= SelectField('Chip', choices=[('A1'),('A2'),('A3'),('A4'),
                                    ('B1'),('B2'),('B3'),('B4'),('B5'),('B6'),
                                    ('C1'),('C2'),('C3'),('C4'),('C5'),('C6'),
                                    ('D1'),('D2'),('D3'),('D4')], validators=[DataRequired()])
	waferME = StringField("Wafer Number", validators=[DataRequired()])
	batchME = StringField("Batch Number", validators=[DataRequired()])
	submit = SubmitField("Submit")

@chip_ME_blueprint.route('/', methods=['POST', 'GET'])
def chipME():
    form = ChipMEForm()
    if form.validate_on_submit():
        batchME = get_or_create(db.session, BatchME, batchME_number=form.batchME.data)
        waferME = get_or_create(db.session, WaferME,waferME_number=form.waferME.data,batchME_id=batchME.id)
        chipME = get_or_create(db.session, ChipME, chipME=form.chipME.data, waferME_id = waferME.id)
        form.batchME.data=''
        form.waferME.data=''
        form.chipME.data=''
        return redirect(url_for('chipME.datatableME',chipME_id = chipME.id))
    else:
        return render_template('me.html', form=form, correct_login = True, before_login = False, chipME_info_v = False)
    
@chip_ME_blueprint.route('/datatableME/<int:chipME_id>')
def datatableME(chipME_id):
    chipME_info = ChipME.query.filter_by(id=chipME_id).first()
    oqaME_info = OQAme.query.filter_by(chipME_id=chipME_id).first()
    eqaME_info = EQAme.query.filter_by(chipME_id=chipME_id).first()
    lqaME_info = LQAme.query.filter_by(chipME_id=chipME_id).first()
    return render_template ('datatableME.html', chipME_info=chipME_info, oqaME_info = oqaME_info, eqaME_info = eqaME_info, lqaME_info = lqaME_info, correct_login = True, before_login = False)