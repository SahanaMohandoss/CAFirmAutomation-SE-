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
    Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
    con = sql.connect(Database)
    con.row_factory = sql.Row
  
    cur = con.cursor()
    
    cur.execute("select USERNAME from EMPLOYEE")
    rows2 = cur.fetchall()
    
    cur.execute("select TOKEN_NO,DESCRIPTION,TYPE_OF_SERVICE FROM SERVICE WHERE ACCEPTED=0")          
    rows1 = cur.fetchall()
    print(rows1)
    print("hereeeeeeeeeee")
    cur.execute("select TOKEN_NO,DESCRIPTION,TYPE_OF_SERVICE FROM SERVICE WHERE ACCEPTED=1 AND ALLOCATED=0")
    rows3 = cur.fetchall()
    #cur.execute("select Token_No, Document,Description from service where Completed='Yes' AND Verified='No'")
    #print("andddddd")
    #rows3 = cur.fetchall()
    #print(rows3)
    con.close()
    return render_template("list.html",rows1=rows1,rows2=rows2,rows3=rows3)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("ummmmmm?")
        asd = request.get_json()
        print(asd)
        return "hey"
    #return render_template("partner.html")

@app.route('/quotation', methods=['GET', 'POST'])
def quotation():
    if request.method == 'POST':
        print("ummmmmm yeah?")
        enterDetail = request.get_json()
        print(enterDetail)
        Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        con = sql.connect(Database)
        con.row_factory = sql.Row
        cur = con.cursor()
        print(enterDetail["quotation"])
        exe = 'UPDATE SERVICE SET QUOTATION=%s WHERE TOKEN_NO = %s' % (enterDetail["quotation"],enterDetail["token"])
        cur.execute(exe)
        con.commit()
        con.close()
        return "done"

@app.route('/allocate', methods=['GET', 'POST'])
def allocate():
    if request.method == 'POST':
        allocateSer = request.get_json()
        print(allocateSer)
        
        Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        con = sql.connect(Database)
        con.row_factory = sql.Row
        cur = con.cursor()
        exe = 'INSERT INTO SERVICE_ALLOCATION (TOKEN,EMP,ALLOCATED_BY,ESTIMATED_HOURS) VALUES (?,?,?,?)'
        params =  (allocateSer["token"],allocateSer["employee"],allocateSer["partner"],1)
        cur.execute(exe,params)
        con.commit() 
        con.close()
        return "done"

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        toVerify = request.get_json()
        print(toVerify)
        Database = '/Users/simrandhinwa/data.db'
        con = sql.connect(Database)
        con.row_factory = sql.Row 
        cur = con.cursor()
        print(toVerify['token'])
        return "cutes"
'''
        cur.execute("ALTER TABLE service Verified='Yes' where Token_No=%s",(toVerify.token,))
query_string = "SELECT * FROM p_shahr WHERE os = %s"
    cursor.execute(query_string, (username,))
'''

if __name__ == '__main__':
    app.run(debug=False)

#select Token_No, Document, Description from Service JOIN Service_Docs ON select * from Service, Service_Status where Service_Status.Completed = Yes