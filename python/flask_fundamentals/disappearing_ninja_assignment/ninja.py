from flask import Flask, render_template, redirect, request

n = Flask(__name__)

@n.route('/')
def index():
    return render_template('index.html')

@n.route('/ninja')
def ninja(): 
    return render_template('ninja.html')

@n.route('/ninja/<color>')
def ninja_color(color):
    if color == "purple":
        return render_template('donny.html')
    elif color == "blue":
        return render_template('leo.html')
    elif color == "red":
        return render_template('raph.html')
    elif color == "orange":
        return render_template('mikey.html')
    
    return render_template('april.html')

n.run(debug=True)