import json
from os.path import dirname, abspath


full_path = dirname(dirname(abspath(__file__)))+"/crs_final/"


def get_posts_all():
    with open(full_path+'data/data.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)
        return data



def get_posts_by_user(user_name):
    with open(full_path + 'data/data.json', 'r', encoding='utf8') as f:
        file = json.load(f)
    posts = []
    for post in file:
        name = post['poster_name']
        if user_name in name:
            posts.append(post)
    return posts



def get_comments_by_post_id(post_id):
    with open(full_path + 'data/comments.json', 'r', encoding='utf8') as f:
        file = json.load(f)
    comments = []
    for comment in file:
        if comment['post_id'] == post_id:
            comments.append(comment)
    return comments




def search_for_posts(query):
    posts = get_posts_all()
    search_list = []
    query_lower = query.lower()
    for post in posts:
        search_world = post['content'].lower()
        if query_lower in search_world:
            search_list.append(post)
    return search_list




def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post

