from lib.social_network import SocialNetwork

"""
SocialNetwork constructs with an id, name and genre
"""
def test_social_network_constructs():
    social_network = SocialNetwork(1, "Test SocialNetwork", "Test Genre")
    assert social_network.id == 1
    assert social_network.name == "Test SocialNetwork"
    assert social_network.genre == "Test Genre"

"""
We can format social_networks to strings nicely
"""
def test_social_networks_format_nicely():
    social_network = SocialNetwork(1, "Test SocialNetwork", "Test Genre")
    assert str(social_network) == "SocialNetwork(1, Test SocialNetwork, Test Genre)"
    # Try commenting out the `__repr__` method in lib/social_network.py
    # And see what happens when you run this test again.

"""
We can compare two identical social_networks
And have them be equal
"""
def test_social_networks_are_equal():
    social_network1 = SocialNetwork(1, "Test SocialNetwork", "Test Genre")
    social_network2 = SocialNetwork(1, "Test SocialNetwork", "Test Genre")
    assert social_network1 == social_network2
    # Try commenting out the `__eq__` method in lib/social_network.py
    # And see what happens when you run this test again.
