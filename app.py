from lib.database_connection import DatabaseConnection
from lib.social_network_repository import SocialNetworkRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all social_networks
social_network_repository = SocialNetworkRepository(connection)
social_networks = social_network_repository.all()

# List them out
for social_network in social_networks:
    print(social_network)
