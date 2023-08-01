import json

import requests


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_users_data(url: str = USERS_DATA_URL):
    res = requests.get(url)
    if res:
        users_data = json.loads(res.text)

    return users_data
