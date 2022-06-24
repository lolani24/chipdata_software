from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea


QA_blueprint = Blueprint('QA', __name__, template_folder='templates')




@QA_blueprint.route('/')
def qa():
    return ("hello")