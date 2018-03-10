from flask import Flask, render_template, redirect, request, flash, session

sv = Flask(__name__)

sv.secret_key = "1928ifmdlksmlfk"
@sv.route('/')
def index():
    return render_template('index.html')

@sv.route('/results', methods = ['POST'])
def process():
    # Added checks for form validation for validation exercise
    error = False
    name = request.form['name']
    if not name.replace(' ','').isalpha() or len(name) <= 0:
        error = True
        flash("Your name cannot be empty or cannot contain numbers!")
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(comment) > 120 or len(comment) <=0:
        error = True
        flash("Comments must be between 1 and 120 characters!")
    if error:
        return redirect('/')

    print name
    print location
    print language
    print comment

    return render_template('results.html', name = name, location = location, language = language, comment = comment)

sv.run(debug=True)