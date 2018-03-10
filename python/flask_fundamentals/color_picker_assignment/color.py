from flask import Flask, redirect, render_template, request

c = Flask(__name__)

@c.route('/', methods = ['POST'])
def index():

    values_ok = True
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']

    if red < 0 or red > 255 or green < 0 or green > 255 or blue < 0 or blue > 255:
        values_ok = False
        
    return render_template('color.html', red = red, green = green, blue = blue, values_ok = values_ok)


# @c.route('/interact', methods = ['POST'])
# def interact():


c.run(debug=True)