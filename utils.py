import json
from os.path import dirname, abspath

full_path = dirname(dirname(abspath(__file__)))+"/crs_final/"
def get_posts_all():  # вывод всех постов
    with open(full_path+'data/data.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)
        return data


#print(get_posts_all())


def get_posts_by_user(user_name):  # вывод постов определенного пользователя
    with open(full_path+'data/data.json', 'r', encoding='utf8') as f:
        file = json.load(f)
    posts = []
    for post in file:
        name = post['poster_name']
        if user_name in name:
            posts.append(post)
    return posts


# print(get_posts_by_user('leo'))

def get_comments_by_post_id(post_id):
    with open(full_path+'data/comments.json', 'r', encoding='utf8') as f:
        file = json.load(f)
    comments = []
    for comment in file:
        if comment['post_id'] == post_id:
            comments.append(comment)
    return comments


# print(get_comments_by_post_id(2))


def search_for_posts(query):
    posts = get_posts_all()
    search_list = []
    query_lower = query.lower()
    for post in posts:
        search_world = post['content'].lower()
        if query_lower in search_world:
            search_list.append(post)
    return search_list


# print(search_for_posts('днем'))


def get_post_by_pk(pk):  # вывод поста по его идентификатору
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post

# print(get_post_by_pk(2))
