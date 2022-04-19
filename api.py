from flask import Flask, jsonify
from utils import get_posts_all, get_post_by_pk


api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False


@api.get('/api/posts/')
def show_posts():
    data = get_posts_all()
    return jsonify(data)


@api.route('/api/posts/<int:pk>', methods=['GET'])
def show_post_by_pk(pk):
    posts = get_post_by_pk(pk)
    return jsonify(posts)



if __name__ == '__main__':
    api.run(debug=True)
