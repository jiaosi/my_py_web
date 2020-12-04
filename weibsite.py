

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '''<img src="{{ url_for('static', filename='pic.jpg')}}" />'''

if __name__ == '__main__':
	app.run(host='107.172.206.163', debug=True)
