from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello, User</h1>"


@app.route('/information')
def info():
    return "<h1>Information about me.</h1>"


@app.route('/puppy/<name>')
def puppy(name):
    return f"<h1>This is the page for {name.upper()}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
