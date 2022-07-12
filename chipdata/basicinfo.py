from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from extensions import db
from .models.chipdata import Chip
from chipdata.models.chipdata import QA, EQA, LQA

chip_blueprint = Blueprint('chip', __name__, template_folder='templates')


#Basic Chip Information Form
class ChipForm(FlaskForm):
	id = StringField("Chip ID", validators=[DataRequired()])
	wafer = StringField("Wafer Number", validators=[DataRequired()])
	batch = StringField("Batch Number", validators=[DataRequired()])
	submit = SubmitField("Submit")

@chip_blueprint.route('/', methods=['POST', 'GET'])
def chip():
    form = ChipForm()
    if form.validate_on_submit():
        chip = Chip.query.filter_by(id=form.id.data).first()
        if chip is None:
            chip = Chip(id=form.id.data, batch=form.batch.data, wafer=form.wafer.data) 
            db.session.add(chip)
            db.session.commit()
        form.id.data =''
        form.batch.data =''
        form.wafer.data = ''
    return render_template('chip.html', form=form, correct_login = True, before_login = False)


# Basic Data Table 
@chip_blueprint.route('/data')
def data():
    chip_info = Chip.query.order_by(Chip.date_added)
    return render_template("datatable.html", chip_info=chip_info, correct_login = True, before_login = False)


# Chip Interface
@chip_blueprint.route('/simo')
def simo():
    return render_template("simo.html", correct_login = True, before_login = False)

@chip_blueprint.route('/me')
def me():
    return render_template("me.html", correct_login = True, before_login = False)



