class Post:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, user_id, title, content, views):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.content = content
        self.views = views

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an SocialNetwork
    def __repr__(self):
        return f"Post({self.id}, {self.user_id}, {self.title}, {self.content}, {self.views})"


# Create post (user_id, title, content)
# See views () => hardcode a number

# Table: users
# id: SERIAL
# username: text
# email: text

# Table: posts
# id: SERIAL
# user_id: int
# title: text
# content: text
# views: int