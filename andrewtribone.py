import os
from flask import Flask
from flask import render_template

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
