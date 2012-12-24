from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from tribone.lib.presenter import Blob
from tribone.lib.presenter import Tree
from tribone.lib.presenter import Repository


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

repo = Repository()

@app.route('/')
def home():
    return render_template(
        'index.html',
        contents=repo.list_objects(repo.toplevel))

@app.route('/_get_blob')
def get_blob():
    """AJAX handler to display contents of a file."""
    b = Blob(
        request.args.get('dirpath', type=str).strip(),
        request.args.get('filename', type=str).strip())
    return jsonify({'result': b.show()})

@app.route('/_get_tree')
def get_tree():
    """AJAX handler to display contents of a file."""
    t = Tree(
        request.args.get('dirpath', type=str).strip(),
        request.args.get('dirname', type=str).strip())
    return jsonify({'result': t.nav_list_html})

if __name__ == '__main__':
    app.run()
