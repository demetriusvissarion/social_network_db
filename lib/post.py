# from lib.social_network import SocialNetwork

# class SocialNetworkRepository:

#     # We initialise with a database connection
#     def __init__(self, connection):
#         self._connection = connection

#     # Retrieve all social_networks
#     def all(self):
#         rows = self._connection.execute('SELECT * from social_networks')
#         social_networks = []
#         for row in rows:
#             item = SocialNetwork(row["id"], row["name"], row["genre"])
#             social_networks.append(item)
#         return social_networks

#     # Find a single social_network by their id
#     def find(self, social_network_id):
#         rows = self._connection.execute(
#             'SELECT * from social_networks WHERE id = %s', [social_network_id])
#         row = rows[0]
#         return SocialNetwork(row["id"], row["name"], row["genre"])

#     # Create a new social_network
#     # Do you want to get its id back? Look into RETURNING id;
#     def create(self, social_network):
#         self._connection.execute('INSERT INTO social_networks (name, genre) VALUES (%s, %s)', [
# social_network.name, social_network.genre])
#         return None

#     # Delete an social_network by their id
#     def delete(self, social_network_id):
#         self._connection.execute(
#             'DELETE FROM social_networks WHERE id = %s', [social_network_id])
#         return None


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