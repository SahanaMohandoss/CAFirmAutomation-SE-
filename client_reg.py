from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
   		username = request.form['description']
   		password = request.form['services']
   		#dbHandler.insertUser(username, password)
   		#users = dbHandler.retrieveUsers()
   		return render_template("ClientRegister.html")
    else:
            return render_template("ClientRegister.html")

if __name__ == '__main__':
    app.run(debug=False)
