# from lib.social_network_repository import SocialNetworkRepository
# from lib.social_network import SocialNetwork

# """
# When we call SocialNetworkRepository#all
# We get a list of SocialNetwork objects reflecting the seed data.
# """
# def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
#     db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
#     repository = SocialNetworkRepository(db_connection) # Create a new SocialNetworkRepository

#     social_networks = repository.all() # Get all social_networks

#     # Assert on the results
#     assert social_networks == [
#         SocialNetwork(1, "Pixies", "Rock"),
#         SocialNetwork(2, "ABBA", "Pop"),
#         SocialNetwork(3, "Taylor Swift", "Pop"),
#         SocialNetwork(4, "Nina Simone", "Jazz"),
#     ]

# """
# When we call SocialNetworkRepository#find
# We get a single SocialNetwork object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = SocialNetworkRepository(db_connection)

#     social_network = repository.find(3)
#     assert social_network == SocialNetwork(3, "Taylor Swift", "Pop")

# """
# When we call SocialNetworkRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = SocialNetworkRepository(db_connection)

#     repository.create(SocialNetwork(None, "The Beatles", "Rock"))

#     result = repository.all()
#     assert result == [
#         SocialNetwork(1, "Pixies", "Rock"),
#         SocialNetwork(2, "ABBA", "Pop"),
#         SocialNetwork(3, "Taylor Swift", "Pop"),
#         SocialNetwork(4, "Nina Simone", "Jazz"),
#         SocialNetwork(5, "The Beatles", "Rock"),
#     ]

# """
# When we call SocialNetworkRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = SocialNetworkRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     result = repository.all()
#     assert result == [
#         SocialNetwork(1, "Pixies", "Rock"),
#         SocialNetwork(2, "ABBA", "Pop"),
#         SocialNetwork(4, "Nina Simone", "Jazz"),
#     ]
