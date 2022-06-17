from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from extensions import db
from .models.chipdata import Chip

chip_blueprint = Blueprint('chip', __name__, template_folder='templates')



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
        
     
        
    return render_template('chip.html', form=form)