from flask import Flask
from flask import request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World! Your browser is {0}.</h1>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
    manager.run()
    #app.run(host="0.0.0.0", debug=True)
