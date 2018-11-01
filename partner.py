import sqlite3 as sql
from flask import g
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__,template_folder='templates')

'''
@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('partner.html',)
'''

@app.route('/')
def list():
    Database = '/Users/simrandhinwa/data.db'
    con = sql.connect(Database)
    con.row_factory = sql.Row
  
    cur = con.cursor()
    
    cur.execute("select * from employee")
    rows2 = cur.fetchall();
    
    cur.execute("select * from new")
                 
    rows1 = cur.fetchall();
    print(rows1)
    return render_template("list.html",rows1=rows1,rows2=rows2)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        asd = request.json
        print(asd)
    return render_template("partner.html")

if __name__ == '__main__':
    app.run(debug=False)
