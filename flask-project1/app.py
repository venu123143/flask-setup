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


@app.route('/users/<name>')
def user(name):
    print(name)
    if name == 'admin':
        return redirect(url_for('admin'))
    elif name == 'user':
        return redirect(url_for('allenv')) #changed url_for to allenv.
    elif name == 'teacher':
        return redirect(url_for('env'))
    else:
        return f"User {name} not recognized"

@app.route('/admin')
def admin():
    return "Admin page"
@app.route('/user')
def allenv():
    return "came to allenv"

if __name__ == "__main__":
    app.run(debug=True)