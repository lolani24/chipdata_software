from pickle import NONE
from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from extensions import db
from chipdata.models.chipdata import Batch, Wafer, Chip, OQA, EQA, LQA
from db_utils import get_or_create #either finds an exisiting row or creates a new one 


chip_blueprint = Blueprint('chip', __name__, template_folder='templates')

chip_info_v = None


#Basic Chip Information Form
class ChipForm(FlaskForm):
	chip = StringField("Chip ID", validators=[DataRequired()])
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
        return render_template('chip.html', form=form, correct_login = True, before_login = False, chip_info_v = True)
    else:
        return render_template('chip.html', form = form, correct_login = True, before_login = False, chip_info_v = False)
    



# Basic Data Table 
@chip_blueprint.route('/data')
def data():
    chip_info = Chip.query.order_by(Chip.chip)
    
    return render_template("datatable.html", chip_info=chip_info, correct_login = True, before_login = False)


# Chip Interface
@chip_blueprint.route('/simo')
def simo():
    return render_template("simo.html", correct_login = True, before_login = False)

@chip_blueprint.route('/me')
def me():
    return render_template("me.html", correct_login = True, before_login = False)







