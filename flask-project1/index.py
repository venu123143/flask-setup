from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/admin')
def admin():
    return "Admin page"

@app.route('/user/cameto')
def user():
    return "came to user"

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode