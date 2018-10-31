from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
	conn = sqlite3.connect('database.db')
	if request.method=='POST':
			#username = request.form['description']
			#password = request.form['services']
			
			
			return render_template("ClientRegister.html")
	else:
            return render_template("ClientRegister.html")

if __name__ == '__main__':
    app.run(debug=False)
