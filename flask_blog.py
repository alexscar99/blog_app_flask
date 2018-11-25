from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
