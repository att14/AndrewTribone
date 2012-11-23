from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from presenter import Blob
from presenter import Repository


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

repo = Repository()

@app.route('/')
def home():
	return render_template(
		'index.html',
		contents=repo.list_objects(repo.toplevel)
	)

@app.route('/_get_blob')
def get_blob():
	"""AJAX handler to display contents of a file."""
	b = Blob(request.args.get('relpath', type=str).strip())
	return jsonify({'result': b.show()})

if __name__ == '__main__':
	app.run()
