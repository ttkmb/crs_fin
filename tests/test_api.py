import unittest

from api import api


def test_api():
    result = api.test_client().get('/api/posts/').json
    assert isinstance(result, list)


def test_check_keys_success():
    response = api.test_client().get('/api/posts/1')

    for key in ["poster_name",
                "poster_avatar",
                "pic",
                "content",
                "views_count",
                "likes_count",
                "pk"]:
        assert key in response.json.keys()


def test_api_sec():
    result = api.test_client().get('/api/posts/1').json
    assert isinstance(result, dict)


def test_check_keys_success_sec():
    response = api.test_client().get('/api/posts/1')

    for key in ["poster_name",
                "poster_avatar",
                "pic",
                "content",
                "views_count",
                "likes_count",
                "pk"]:
        assert key in response.json.keys()
