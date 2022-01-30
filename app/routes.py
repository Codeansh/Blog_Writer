from app import app_
from flask import render_template


@app_.route('/')
@app_.route('/index')
def index():
    user = {'username': 'roy'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }]
    return render_template('index.html', user=user, posts=posts)


@app_.route('/about')
def about():
    return "<h1>About us</h1>"
