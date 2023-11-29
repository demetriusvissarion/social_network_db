from lib.post import Post

class PostRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all posts
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["user_id"], row["title"], row["content"], row["views"])
            posts.append(item)
        return posts

    # Find a single post by their id
    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["user_id"], row["title"], row["content"], row["views"])
    
    # Find all post by a user_id
    def find_by_user_id(self, user_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE user_id = %s', [user_id])
        row = rows[0]
        return Post(row["id"], row["user_id"], row["title"], row["content"], row["views"])

    # Create a new post
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, post):
        self._connection.execute('INSERT INTO posts (user_id, title, content, views) VALUES (%s, %s, %s, %s)', [
post.user_id, post.title, post.content, post.views])
        return None
    
    # # Delete an post by their id
    # def delete(self, post_id):
    #     self._connection.execute(
    #         'DELETE FROM posts WHERE id = %s', [post_id])
    #     return None


# INSERT INTO posts (user_id, title, content, views) VALUES (1, 'Lorem ipsum', 'Lorem ipsum dolor sit amet', 0);
# INSERT INTO posts (user_id, title, content, views) VALUES (2, 'Consectetur', 'Consectetur adipiscing elit', 0);
# INSERT INTO posts (user_id, title, content, views) VALUES (3, 'Sed do', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua', 0);
# INSERT INTO posts (user_id, title, content, views) VALUES (4, 'Ut enim', 'Ut enim ad minim veniam', 0);