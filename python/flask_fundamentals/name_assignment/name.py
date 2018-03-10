from flask import Flask, render_template, redirect, request

name = Flask(__name__)
@name.route('/')
def index():
    return render_template('name.html')

@name.route('/process', methods = ['POST'])
def process():
    name = request.form['name']

    print name

    return redirect('/')
name.run(debug=True)