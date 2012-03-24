from auth import LastFM
from libfm import LibFM
from libfm import LibFMError

# The auth file is not included in repo because it contains sensitive information
# I have porivded an example file if you are interested (auth_example.py)
last_fm = LastFM()

# Create a handler instance with API key and application secret
lib_fm = LibFM(last_fm.api_key, last_fm.secret)

try:
	token = last_fm.token
	lib_fm.create_session(token)

	info = lib_fm.read('user.getRecentTracks', user=last_fm.user)
	print info
except LibFMError, err:
	print err

