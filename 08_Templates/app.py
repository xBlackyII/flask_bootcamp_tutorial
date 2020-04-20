from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user_logged_in = True
    return render_template('home.html', user_logged_in=user_logged_in)


@app.route('/puppy/<name>')
def puppy(name):
    return render_template('puppy.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
