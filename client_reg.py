from flask import Flask
from flask import render_template
from flask import request
import sqlite3
from flask import json, session
from validate_email import validate_email

app = Flask(__name__)

Database = 'ca_firm.db'

@app.route('/', methods=['POST', 'GET'])
def home():
			return render_template("ClientRegister.html")

def insert(table, fields=(), values=()):
    # g.db is the database connection
	con = sqlite3.connect(Database)

	cur = con.cursor()
	print("connected")
	query = 'INSERT INTO %s (%s) VALUES (%s)' % (
        table,
        ', '.join(fields),
        ', '.join(['?'] * len(values))
    )
	cur.execute(query, values)
	con.commit()
	id = cur.lastrowid
	cur.close()
	return id

def query_db(query, args=(), one=False):
	con = sqlite3.connect(Database)
	cur = con.execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

@app.route('/signUp',methods=['POST'])
def signUp():
    print("here")
    # read the posted values from the UI
    _name = request.form['username']
    _fname = request.form['firstname']
    _lname = request.form['lastname']
    _email = request.form['email']
    _password = request.form['password']
    _confpassword = request.form['confpassword']
    _num = request.form['number']
    flag = 0
    print(request.form['usertype'])
    if(request.form['usertype']=="0"):
    	a = request.form['aadhar']
    	p = request.form['pan']
    	print(a and p)
    	if( a and p ):
    		flag = 1
    else:
    	if(request.form['employeeID']):
    		flag = 1
    # validate the received values

    #Check if uname exists:
    exists = [0 , 0,0,0,0] #utype , uname, emai, aadhar, pan,
    n = query_db('SELECT * FROM client WHERE username = ?',
                [_name], one=True)
    exists[0] = int(request.form['usertype'])
    if n is not None:
    	print("This username exists")
    	exists[0] = 1
    e = query_db("SELECT * FROM client WHERE email_id = ?", [_email], one=True)
    if e is not None:
    	print("This email exists")
    	exists[1] = 1
    
    a = query_db("SELECT * FROM client WHERE aadhar_no = ?", [request.form['aadhar']], one=True)
    if a is not None:
    	print("This aadhar exists")
    	exists[2] = 1
    
    p = query_db("SELECT * FROM client WHERE pan_no = ?", [request.form['pan']], one=True)
    if p is not None:
    	print("This pan exists")
    	exists[3] = 1



    print(_name, _lname, validate_email(_email) , (_password == _confpassword), flag)
    if _name and _lname and _num and _fname and  _email and _password and validate_email(_email) and (_password == _confpassword) and flag and not(exists[0]==1 or exists[1]==1 or exists[2] ==1 or exists[3] == 1):
        print("ALL OK")
    	#INSERT TO DATABASE
        if(request.form['usertype']=="0"): 
            print("here in client")
            cols = ("username", "password", "first_name", "last_name","email_id", "company", "contact_no", "aadhar_no", "pan_no")
            vals = (_name, _password , _fname, _lname , _email , int(request.form['clientType']), _num , request.form['aadhar'] , request.form['pan'])
            insert("client" , cols, vals)
            print("done")
	    	#print(rows1)
        elif(request.form['usertype']=="1"):
            print("here in employee")
            cols = ("username", "password", "first_name", "last_name","email_id", "contact_no", "employee_id")
            vals = (_name, _password , _fname, _lname , _email , _num , request.form['employeeID'] )
            insert("employee" , cols, vals)
            print("done")
        else:
            print("here in partner")
            cols = ("username", "password", "first_name", "last_name","email_id", "contact_no", "employee_id")
            vals = (_name, _password , _fname, _lname , _email , _num , request.form['employeeID'] )
            insert("partner" , cols, vals)
            print("done")

        return json.dumps({'html':'<span>All fields good !!</span>','status':0})
    elif(exists[0]==1 or exists[1]==1 or exists[2] ==1 or exists[3] == 1):
    	return json.dumps({'html':'<span>All fields good !!</span>','status':2, 
    		'username':exists[0],
    		'email':exists[2],
    		'aadhar':exists[2],
    		'pan':exists[3],
    		})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>','status':1})


@app.route('/logIn',methods=['POST'])
def logIn():
    #print(request.form)
    name = request.form['uname']
    password = request.form['pwd']
    print("In log in")
    print(name , password)
    a = query_db("SELECT * FROM client WHERE username = ?", [name], one=True)
    print("Values" , a)
    if(a is None):
        return json.dumps({'status':0})
    else:
        if(a[1]==password):
            
            #render_template("ClientHome.html")
            session['username'] = name
            return json.dumps({'status':1 , 'type':int(a[5]) })

        else:
            return json.dumps({'status':2})


@app.route('/clientHome')
def clientHome():
    
    name = session['username']
    return render_template("ClientHome.html", username=name)



@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   
   return render_template("ClientRegister.html")

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)
