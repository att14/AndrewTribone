import json
import requests

from flask import Flask
from flask import render_template

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
	contents = json.loads(
		requests.get(
			'https://api.github.com/repos/att14/AndrewTribone/contents'
		).content
	)
	return render_template('index.html', contents=contents)

if __name__ == '__main__':
	app.run()
