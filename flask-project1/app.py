from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()  # load environment variables from .env

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

@app.route('/')
def home():
    return "Hello world, from flask."

@app.route('/env')
def get_env_vars():
    env_vars = {
        'SECRET_KEY': os.environ.get('SECRET_KEY'),
        'DATABASE_URI': os.environ.get('DATABASE_URI'),
        # Add more environment variables as needed
    }
    return jsonify(env_vars)

@app.route('/all_env')
def get_all_env_vars():
    return jsonify(dict(os.environ))

if __name__ == "__main__":
    app.run(debug=True)