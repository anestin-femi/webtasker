from flask import Flask,jsonify,render_template

app = Flask(__name__)

@app.route('/index')
def index():
	return jsonify({'user':'james'})


if __name__ == '__main__':
	app.run(debug=True,port=3000)