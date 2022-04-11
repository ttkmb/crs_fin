from flask import Flask, request, render_template
from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk


app = Flask(__name__)

posts = get_posts_all()


@app.route('/')
def index():
    return render_template('index.html', posts = posts)



@app.route('/posts/<int:pk>')
def post(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)

    return render_template('post.html', post = post, comments = comments)

@app.route('/search/')
def search():
    search_by = request.args['s'].lower()
    if search_by:
        posts = search_for_posts(search_by)
        if posts:
            return render_template('search.html', search_by = search_by, posts = posts, len_posts = len(posts))

@app.route('/users/<string:username>')
def user(user_name):
    posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', posts = posts)


if __name__ == '__main__':
    app.run(debug=True)
