import json
import requests

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CONTENT_BASE = 'https://api.github.com/repos/att14/AndrewTribone/contents/'

@app.route('/')
def home():
	contents = requests.get(CONTENT_BASE).content
	return render_template('index.html', contents=json.loads(contents))

@app.route('/_get_blob')
def get_blob():
	blob_path = request.args.get('blob_path')
	return jsonify(result=requests.get(CONTENT_BASE + blob_path))

if __name__ == '__main__':
	app.run()
