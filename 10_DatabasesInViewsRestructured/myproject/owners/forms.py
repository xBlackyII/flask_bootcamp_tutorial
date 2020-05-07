from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    id = IntegerField("Id of Puppy:")
    name = StringField("Name of Owner:")
    submit = SubmitField("Add Owner")
