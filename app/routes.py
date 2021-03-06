from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Rishat'}
    posts = [
        {
            'author': {'username': 'Mixa'},
            'body':'Hello'
        },
        {
            'author': {'username': 'John'},
            'body': 'Greetings'
        },
        {
            'author': {'username': 'Alex'},
            'body': 'Are you ok?'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)