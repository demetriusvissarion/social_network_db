from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

# Retrieve all users
user_repository = UserRepository(connection)
users = user_repository.all()
for user in users:
    print(user)

# Retrieve all users posts
post_repository = PostRepository(connection)
posts = post_repository.all()
for post in posts:
    print(post)

# Find all posts by a certain user (user_id == 3)
print(post_repository.find_by_user_id(3))