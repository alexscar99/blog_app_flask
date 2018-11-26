from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post


posts = [
    {
        'author': 'Alex Scarlett',
        'title': 'Blog Post One',
        'content': 'First blog post content',
        'date_posted': 'November 22, 2018'
    },
    {
        'author': 'Jane Smith',
        'title': 'Blog Post Two',
        'content': 'Second blog post content',
        'date_posted': 'November 24, 2018'
    }
]


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f'Account successfully created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
