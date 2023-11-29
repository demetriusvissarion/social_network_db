from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new PostRepository

    posts = repository.all() # Get all posts

    # Assert on the results
    assert str(posts) == '[Post(1, 1, Lorem ipsum, Lorem ipsum dolor sit amet, 6575), Post(2, 2, Consectetur, Consectetur adipiscing elit, 436), Post(3, 3, Sed do, Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua, 354), Post(4, 4, Ut enim, Ut enim ad minim veniam, 3245)]'

"""
When we call PostRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, 4, 'Ut enim', 'Ut enim ad minim veniam', 0))

    result = repository.all()
    assert str(result) == '[Post(1, 1, Lorem ipsum, Lorem ipsum dolor sit amet, 6575), Post(2, 2, Consectetur, Consectetur adipiscing elit, 436), Post(3, 3, Sed do, Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua, 354), Post(4, 4, Ut enim, Ut enim ad minim veniam, 3245), Post(5, 4, Ut enim, Ut enim ad minim veniam, 0)]'

# """
# When we call PostRepository#find
# We get a single Post object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = PostRepository(db_connection)

#     post = repository.find(3)
#     assert post == Post(3, "TestPost3", "test3.email@test.com")


# """
# When we call PostRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = PostRepository(db_connection)
#     repository.delete(4)

#     result = repository.all()
#     assert result == [
#         Post(1, "TestPost1", "test1.email@test.com"),
#         Post(2, "TestPost2", "test2.email@test.com"),
#         Post(3, "TestPost3", "test3.email@test.com"),
#     ]
