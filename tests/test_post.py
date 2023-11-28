from lib.post import Post

"""
Post constructs with an id, user_id, title, content and views
"""
def test_post_constructs():
    post = Post(1, 1, 'Lorem ipsum', 'Lorem ipsum dolor sit amet', 0)
    assert post.id == 1
    assert post.user_id == 1
    assert post.title == 'Lorem ipsum'
    assert post.content == 'Lorem ipsum dolor sit amet'
    assert post.views == 0

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, 1, 'Lorem ipsum', 'Lorem ipsum dolor sit amet', 0)
    assert str(post) == "Post(1, 1, Lorem ipsum, Lorem ipsum dolor sit amet, 0)"
    # Try commenting out the `__repr__` method in lib/post.py
    # And see what happens when you run this test again.

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, 1, 'Lorem ipsum', 'Lorem ipsum dolor sit amet', 0)
    post2 = Post(1, 1, 'Lorem ipsum', 'Lorem ipsum dolor sit amet', 0)
    assert post1 == post2
    # Try commenting out the `__eq__` method in lib/post.py
    # And see what happens when you run this test again.


# INSERT INTO posts (user_id, title, content, views) VALUES (1, 'Lorem ipsum', 'Lorem ipsum dolor sit amet', 0);
# INSERT INTO posts (user_id, title, content, views) VALUES (2, 'Consectetur', 'Consectetur adipiscing elit', 0);
# INSERT INTO posts (user_id, title, content, views) VALUES (3, 'Sed do', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua', 0);
# INSERT INTO posts (user_id, title, content, views) VALUES (4, 'Ut enim', 'Ut enim ad minim veniam', 0);

