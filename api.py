from flask import Flask, jsonify
from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False


@api.route('/api/posts', methods=['GET'])
def show_posts():
    data = get_posts_all()
    return jsonify(data)


@api.route('/api/posts/<int:pk>', methods=['GET'])
def show_post_by_id(pk):
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return jsonify(post)


if __name__ == '__main__':
    api.run(debug=True)
