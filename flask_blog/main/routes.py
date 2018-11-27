from flask import render_template, request, Blueprint
from flask_blog.models import Post

main = Blueprint('main', __name__)


@main.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    posts = Post.query.order_by(
        Post.posted_at.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')
