"""This is an example of auth.py -- Which is not included because it conatins my API keys...

# Basic format for auth class
class APIName(object):
	def __init__(self):
		"""Sets up variables"""

	def handler(self):
		"""Creates a handler instance and returns it"""

	def token_gen(self):
		"""Creates a token and returns it. This is not necessary for all classes."""

# To use the class create an instance of it
lfm_auth_example = ExampleLastFM()

# Access keys
lfm_auth_example.api_key
"""
import pylast


class LastFMAuth(object):
	"""I created a fake LastFM account, feel free to use this info for testing.

	Just rename this file to auth.py
	"""

	def __init__(self):
		self.api_key = u'675c7a3098c1351af0799cd9061f376f'
		self.secret = u'd215d16aa211bacae84ae3416209cbdc'
		self.user = u'LFM_API_Example'
		self.password = pylast.md5(u'lfmapiexample')

		self.handler = None

	def handler_gen(self):
		"""Creates a Network Object and returns it"""

		self.handler = pylast.LastFMNetwork(
			api_key=self.api_key,
			api_secret=self.secret,
			username=self.user,
			password_hash=self.password,
		)
		return self.handler
