from flask import (
    Flask,
    render_template,
    session,
    redirect,
    url_for,
    flash
)
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    BooleanField,
    DateTimeField,
    RadioField,
    SelectField,
    TextField,
    TextAreaField
)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


class SimpleForm(FlaskForm):
    submit = SubmitField('Click Me.')


class InfoForm(FlaskForm):
    """docstring"""
    breed = StringField("What Breed are you?", validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField('Please chose your mood:', choices=[
                      ('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField(u'Pick your favorite food:',
                              choices=[('chi', 'Chicken'), ('bf', 'Beef'), ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()

    # The user hit 'submit'.
    if form.validate_on_submit():
        # store it in this session.
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        # no arguments to pass because is it in session.
        return redirect(url_for('thankyou'))

    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


@app.route('/flash', methods=['GET', 'POST'])
def myflash():
    form = SimpleForm()
    if form.validate_on_submit():
        flash('You just clicked the button.')
        return redirect(url_for('myflash'))
    return render_template('flash.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
