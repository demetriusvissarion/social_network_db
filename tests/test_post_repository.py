# from lib.user_repository import UserRepository
# from lib.user import User

# """
# When we call UserRepository#all
# We get a list of User objects reflecting the seed data.
# """
# def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
#     db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
#     repository = UserRepository(db_connection) # Create a new UserRepository

#     users = repository.all() # Get all users

#     # Assert on the results
#     assert users == [
#         User(1, "TestUser1", "test1.email@test.com"),
#         User(2, "TestUser2", "test2.email@test.com"),
#         User(3, "TestUser3", "test3.email@test.com"),
#         User(4, "TestUser4", "test4.email@test.com"),
#     ]

# """
# When we call UserRepository#find
# We get a single User object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = UserRepository(db_connection)

#     user = repository.find(3)
#     assert user == User(3, "TestUser3", "test3.email@test.com")

# """
# When we call UserRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = UserRepository(db_connection)

#     repository.create(User(None, "TestUser5", "test5.email@test.com"))

#     result = repository.all()
#     assert result == [
#         User(1, "TestUser1", "test1.email@test.com"),
#         User(2, "TestUser2", "test2.email@test.com"),
#         User(3, "TestUser3", "test3.email@test.com"),
#         User(4, "TestUser4", "test4.email@test.com"),
#         User(5, "TestUser5", "test5.email@test.com"),
#     ]

# """
# When we call UserRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = UserRepository(db_connection)
#     repository.delete(4)

#     result = repository.all()
#     assert result == [
#         User(1, "TestUser1", "test1.email@test.com"),
#         User(2, "TestUser2", "test2.email@test.com"),
#         User(3, "TestUser3", "test3.email@test.com"),
#     ]
