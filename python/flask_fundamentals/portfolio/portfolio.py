from flask import Flask, render_template

portfolio = Flask(__name__)

@portfolio.route('/')
def index():
    return render_template('index.html')

@portfolio.route('/projects')
def projects():
    return render_template('projects.html')

@portfolio.route('/about_me')
def about_me():
    return render_template('about_me.html')

portfolio.run(debug=True)
