"""This is an example of auth.py -- Its not included because it conatins my API keys (derp)

# Basic format for auth class
class APIName(object):
	def __init__(self):
		self.api_key = u'abcdefghijklmnopqrstuvwxyz'
		self.secret = u'abcdefghijklmnopqrstuvwxyz'
		self.token = u'abcdefghijklmnopqrstuvwxyz'
		self.user = u'username'

# To use the class create an instance of it
lfm_auth_example = ExampleLastFM()

# Access keys
lfm_auth_example.api_key
"""

class ExampleLastFM(object):
	"""I created a fake LastFM account, feel free to use this info for testing."""
	def __init__(self):
		self.api_key = u'675c7a3098c1351af0799cd9061f376f'
		self.secret = u'd215d16aa211bacae84ae3416209cbdc'
		sefl.token = u''
		self.user = u'LFM_API_Example'

