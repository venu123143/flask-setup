from flask import Flask, jsonify, redirect, url_for
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

@app.route('/')
def home():
    return "Hello world, from flask."


@app.route('/users/<name>/<int:user_id>')
def route_navigate(name, user_id):
    print(name,"")
    if name == 'admin':
        return redirect(url_for('admin'))
    elif name == 'user':
        return redirect(url_for('user')) #url_for will take the 1st argument as the function.
    elif name == 'teacher':
        return redirect(url_for('teacher'))
    else:
        return f"User {name, user_id} not recognized"

@app.route('/admin')
def admin():
    return "Admin page"

@app.route('/user/cameto')
def user():
    return "came to user"

@app.route('/teacher/study')
def teacher():
    return "teacher to allenv"
@app.route('/generate_url')
def generate_url():
    # Generate a URL with parameters
    url = url_for('route_navigate', name='testuser', user_id='456')
    return f"Generated URL: {url}"  # fstrings
def add_url_rule_function():
    return "new functoin";

app.add_url_rule("/rule", add_url_rule_function);

@app.route('/test', endpoint='my_custom_endpoint')
def test_function():
    return "Test"

@app.route('/generate')
def generate():
    return url_for('my_custom_endpoint') #using the endpoint name.

if __name__ == "__main__":
    app.run(debug=True)