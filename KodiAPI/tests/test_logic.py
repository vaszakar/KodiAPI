from utils.api_helpers import get_all_users, get_posts_by_user
from utils.api_helpers import get_all_posts, get_comments_by_post


def test_users_have_posts():
    users = get_all_users()

    for user in users:
        user_id = user["id"]
        posts = get_posts_by_user(user_id)

        # Verify that each user has at least one post

        assert len(posts) > 0, f"User {user_id} has no posts!"


def test_posts_have_comments():
    posts = get_all_posts()

    for post in posts:
        post_id = post["id"]
        comments = get_comments_by_post(post_id)

        # Verify that each post has at least one comment

        assert len(comments) > 0, f"Post {post_id} has no comments!"
