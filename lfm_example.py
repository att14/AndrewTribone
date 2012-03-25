from auth import LastFMAuth

# The auth file is not included in repo because it contains sensitive information
# I have porivded an example file if you are interested (auth_example.py)
last_fm_auth = LastFMAuth()

lfm_handler = last_fm_auth.handler_gen()

user = lfm_handler.get_user('atribone')
print user.get_recent_tracks()
