from flask import Flask, render_template

hello = Flask(__name__)

@hello.route('/')
def hello_world():
    return render_template('hello.html')

hello.run(debug=True)