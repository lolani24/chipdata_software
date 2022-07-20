from pickle import NONE
from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField,SelectField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from extensions import db
from chipdata.models.chipdata import Batch, Wafer, Chip, OQA, EQA, LQA
from db_utils import get_or_create #either finds an exisiting row or creates a new one 


chip_blueprint = Blueprint('chip', __name__, template_folder='templates')

chip_info_v = None


#Basic Chip Information Form
class ChipForm(FlaskForm):
	chip= SelectField('Chip', choices=[('A1'),('A2'),('A3'),('A4'),('A5'),
                                    ('B1'),('B2'),('B3'),('B4'),('B5'),('B6'),('B7'),
                                    ('C1'),('C2'),('C3'),('C4'),('C5'),('C6'),('C7'),('C8'),('C9'),
                                    ('D1'),('D2'),('D3'),('D4'),('D5'),('D6'),('D7'),('D8'),('D9'),
                                    ('E1'),('E2'),('E3'),('E4'),('E5'),('E6'),('E7'),('E8'),('E9'),
                                    ('F1'),('F2'),('F3'),('F4'),('F5'),('F6'),('F7'),
                                    ('G1'),('G2'),('G3'),('G4'),('G5')
                                    ], validators=[DataRequired()])
	wafer = StringField("Wafer Number", validators=[DataRequired()])
	batch = StringField("Batch Number", validators=[DataRequired()])
	submit = SubmitField("Submit")

@chip_blueprint.route('/', methods=['POST', 'GET'])
def chip():
    form = ChipForm()
    if form.validate_on_submit():
        batch = get_or_create(db.session, Batch, batch_number=form.batch.data)
        wafer = get_or_create(db.session, Wafer,wafer_number=form.wafer.data,batch_id=batch.id)
        chip = get_or_create(db.session, Chip, chip=form.chip.data, wafer_id = wafer.id)
        form.batch.data=''
        form.wafer.data=''
        form.chip.data=''
        return redirect(url_for('chip.datatable',chip_id = chip.id))
    else:
        return render_template('simo.html', form=form, correct_login = True, before_login = False, chip_info_v = False)
    
@chip_blueprint.route('/datatable/<int:chip_id>')
def datatable(chip_id):
    chip_info = Chip.query.filter_by(id=chip_id).first()
    oqa_info = OQA.query.filter_by(chip_id=chip_id).first()
    eqa_info = EQA.query.filter_by(chip_id=chip_id).first()
    lqa_info = LQA.query.filter_by(chip_id=chip_id).first()
    return render_template ('datatable.html', chip_info=chip_info, oqa_info = oqa_info, eqa_info = eqa_info, lqa_info = lqa_info, correct_login = True, before_login = False)










