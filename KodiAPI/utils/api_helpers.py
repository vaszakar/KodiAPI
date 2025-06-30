import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user_by_id(user_id):
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.get(url)
    return response


def create_post(user_id, title, body):
    url = f"{BASE_URL}/posts"
    payload = {
        "userId": user_id,
        "title": title,
        "body": body
    }
    response = requests.post(url, json=payload)
    return response


def get_all_users():
    url = f"{BASE_URL}/users"
    response = requests.get(url)
    return response.json()


def get_posts_by_user(user_id):
    url = f"{BASE_URL}/posts?userId={user_id}"
    response = requests.get(url)
    return response.json()


def get_all_posts():
    url = f"{BASE_URL}/posts"
    response = requests.get(url)
    return response.json()


def get_comments_by_post(post_id):
    url = f"{BASE_URL}/comments?postId={post_id}"
    response = requests.get(url)
    return response.json()


def get_post_by_id(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url)
    return response
