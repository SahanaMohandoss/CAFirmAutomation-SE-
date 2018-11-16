from flask import Flask
from flask import render_template
from flask import request
import sqlite3
from flask import json, session
from validate_email import validate_email
import re
import flask
# from sentiment_analyzer import SentimentAnalyzer
app = Flask(__name__)
# from employee_reg import *
from partner import *


#one logged in instance

#integrate


#Connect to database
Database = 'ca_firm.db'

#On start go to registration page
@app.route('/', methods=['POST', 'GET'])
def home():
			return render_template("ClientRegister.html")


#To insert  values to a table in a db
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

    id = cur.lastrowid
    cur.close()
    con.commit()
    con.close()
    return id

#To query a table in db
def query_db(query, args=(), one=False):
    con = sqlite3.connect(Database)
    cur = con.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    con.commit()
    con.close()
    return (rv[0] if rv else None) if one else rv

#Sign up code with validation of the fields
@app.route('/signUp',methods=['POST'])
def signUp():
    print("here")
    print(request.form)
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
    if(request.form['usertype']=="0"):
        n = query_db('SELECT * FROM client WHERE username = ?',
                    [_name], one=True)
        #exists[0] = int(request.form['usertype'])
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
    elif(request.form['usertype']=="1"):
        print("here in check emp")
        n = query_db('SELECT * FROM employee WHERE username = ?',
                        [_name], one=True)
        #exists[0] = int(request.form['usertype'])
        if n is not None:
            print("This username exists")
            exists[0] = 1
        e = query_db("SELECT * FROM employee WHERE email_id = ?", [_email], one=True)
        if e is not None:
            print("This email exists")
            exists[1] = 1      
        print(exists)
    else:
        n = query_db('SELECT * FROM partner WHERE username = ?',
                        [_name], one=True)
        #exists[0] = int(request.form['usertype'])
        if n is not None:
            print("This username exists")
            exists[0] = 1
        e = query_db("SELECT * FROM partner WHERE email_id = ?", [_email], one=True)
        if e is not None:
            print("This email exists")
            exists[1] = 1  




    print(_name, _lname, validate_email(_email) , (_password == _confpassword), flag)
    #Check type of user and validation and accordingly insert into correct DB
    if _name and _lname and _num and _fname and  _email and _password and validate_email(_email) and (_password == _confpassword) and flag and not(exists[0]==1 or exists[1]==1 or exists[2] ==1 or exists[3] == 1):
        print("ALL OK")
    	#INSERT TO DATABASE
        if(request.form['usertype']=="0"): 
            print("here in client")
            cols = ("username", "password", "first_name", "last_name","email_id", "company", "contact_no", "aadhar_no", "pan_no")
            vals = (_name, _password , _fname, _lname , _email , int(request.form['clientType']), _num , request.form['aadhar'] , request.form['pan'])
            insert("client" , cols, vals)
            desc = request.form.getlist('filedesc')
            print(desc)
            file = request.files.getlist('files[]')
            i = 0
            print(file)
            for f in file:
                print(f)
                filename = secure_filename(f.filename)
                cols = ("user" , "document", "description" , "filename")
                vals = (_name , sqlite3.Binary(f.read()) , desc[i], filename)
                i+=1
                insert("client_files" , cols, vals)
            print(file)
            print(request.form)
            print(request.files)






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

#Login and check type of user to redirect to correct page
@app.route('/logIn',methods=['POST'])
def logIn():
    #print(request.form)
    t = request.form['typeofuser']
    name = request.form['uname']
    password = request.form['pwd']
    print("In log in")
    print(name , password , t)
    #ADPTER PATTERN: Check type of user and render the corresponding interface
    #0: client , 1:employee , 2: partner
    if(t=="0"):
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
    elif(t=="1"):
        a = query_db("SELECT * FROM employee WHERE username = ?", [name], one=True)
        print("Values" , a)
        if(a is None):
            return json.dumps({'status':0})
        else:
            if(a[1]==password):
                
                #render_template("ClientHome.html")
                session['username'] = name
                return json.dumps({'status':1 , 'type':int(t) })

            else:
                return json.dumps({'status':2})
    else:
        a = query_db("SELECT * FROM partner WHERE username = ?", [name], one=True)
        print("Values" , a)
        if(a is None):
            return json.dumps({'status':0})
        else:
            if(a[1]==password):
                
                #render_template("ClientHome.html")
                session['username'] = name
                return json.dumps({'status':1 , 'type':int(t) })

            else:
                return json.dumps({'status':2})


#To render client page and get the necessary data to display
@app.route('/clientHome')
def clientHome():
    #To pass username
    name = session['username'] 
    print(name)
    name = name.strip()
    s = query_db("SELECT token_no ,current_timestamp, quotation, type_of_service,  status_for_client, emp, estimated_time_of_completion, accepted  FROM service  \
        JOIN service_status ON token_no = service_status.token \
        JOIN service_allocation ON token_no = service_allocation.token \
         WHERE user = ?", [name])
    print(s)
    accepted=[]
    quotation=[]
    #Handle null values in tables check the employee assigned and end date
    for i in range(len(s)):
        x = s[i]
        print(x[5])
        print(x[6])
        if(x[5]  is None):
            print(list(x))
            x =list(x)
            x[5]="Not updated yet"
            s[i] = tuple(x)
        if(x[6]  is None):
            x =list(x)
            x[6]="Not allocated yet"
            s[i] = tuple(x)
        print("value of status is", x[4])
        if(x[2]==0.0):
            accepted.append(1) 
        else: 
            accepted.append(x[7])
        quotation.append(x[2])
    #get clients' messages
    m = query_db("SELECT sender , current_timestamp ,message  FROM messages  \
         WHERE recepient = ? ORDER BY current_timestamp DESC", [name])
    print(m)
    #Get completed docs
    files = query_db("SELECT token_no , filename , completed_service_docs.description   FROM completed_service_docs  \
                JOIN service ON completed_service_docs.token = token_no \
         JOIN service_status ON service_status.token = token_no\
         WHERE user = ? AND verified = ?", [name, 1])
    print(files)
    #Get invoice docs of client
    invoice = query_db("SELECT token_no, generated_by , current_timestamp ,filename, invoice_amount  FROM completed_service_invoice  \
         JOIN service ON completed_service_invoice.token = token_no \
         JOIN service_status ON service_status.token = token_no\
         WHERE user = ?  AND verified = ? ORDER BY current_timestamp DESC", [name,1])
    print(invoice)
    print(accepted)
    return render_template("ClientHome.html", username=name, items = s, messages= m, files=files, invoice=invoice, accepted=accepted, quotation=quotation)


#To submit feedbak of service on click of button

# @app.route('/submitFeedback', methods=['POST'])
# def submitFeedback():
#     data = request.json
#     print("Submitting feedback")
#     print(data)
#     f = data["feedback"]
#     print(f)
#     t = int(data["token"])
#     print(t)
#     #Sentiment analysis of the feedbcak
#     ob=SentimentAnalyzer()
#     sentiment=ob.get_string([f])
#     print(sentiment)
#     s = query_db("UPDATE service SET feedback = ? \
#          WHERE token_no = ?",[data['feedback'], data['token']])
#     s = query_db("UPDATE service SET sentiment = ? \
#          WHERE token_no = ?",[sentiment[0], data['token']])
#     print(s)
#     s= query_db("SELECT feedback FROM service  \
#          WHERE token_no = ?",[ data['token']])
#     print(s)

#     return json.dumps({'status':2})


#To upload files for a service for a user

@app.route('/serviceFileUpload', methods=['POST'])
def serviceFileUpload():
    #data = request.json
    d= request.form['serv_desc']
    t= request.form['serv_token']
    print(d)
    f = request.files.getlist('serv_file')[0]
    filename =f.filename
    print(filename)
    cols = ("token" , "document", "description" , "filename")
    vals = (t , sqlite3.Binary(f.read()), d, filename)
    insert("service_docs" , cols, vals)
    print("Uploaded")
    return json.dumps({'status':2})

#To send messages from one user to another

@app.route('/sendMessage', methods=['POST'])
def sendMessage():
    data = request.json
    print("Submitting feedback")
    print(data)
    c = data["content"]
    t = data["to"]
    f = data["from"]

    z = query_db("SELECT * from client where username = ?", [t])
    print(z)
    if(not(z)):
        z = query_db("SELECT * from employee where username = ?",[t])

    if(not(z)):
        z = query_db("SELECT * from partner where username = ?", [t])
    if (not(z)):
            print("To username not there")
            return json.dumps({'status':0})
    else:
        print(t,f,c)
        cols = ("sender" , "recepient", "message")
        vals = (f,t,c)
        insert("messages" , cols, vals)

        return json.dumps({'status':2})

#To download files and invoice documents
@app.route('/fileDownload', methods=['POST'])
def fileDownload():
    data = request.json
    print("Downloading file...")
    print(data)
    f = data["filename"]
    f = f.strip()
    t = int(data["token"])
    d = data["desc"]
    file = query_db("SELECT document   FROM completed_service_docs  \
               WHERE token = ? AND filename LIKE ? AND description LIKE ? ", [t,f,d])
    print(file)
    with open("files/"+str(t)+"_"+f, 'wb') as output_file:
           output_file.write(file[0][0])
    return json.dumps("{'status':2}")

@app.route('/fileDownloadEmployee', methods=['POST'])
def fileDownloadEmployee():
    print("called")
    data = request.json
    print("Downloading file...")
    f = data["filename"]
    f = f.strip()
    t = int(data["token"])
    d = data["desc"]
    file = query_db("SELECT document   FROM service_docs  \
               WHERE token = ? AND filename LIKE ? AND description LIKE ? ", [t,f,d])
    with open("files/"+str(t)+"_"+f, 'wb') as output_file:
           output_file.write(file[0][0])
    return json.dumps("{'status':2}")

# @app.route('/fileUploadEmployee', methods=['POST'])
# def fileUploaddEmployee():
#     print("called")
#     data = request.json
#     print("Uploading file...")
#     f = data["filename"]
#     f = f.strip()
#     t = int(data["token"])
#     d = data["desc"]
#     file = query_db("SELECT document   FROM service_docs  \
#                WHERE token = ? AND filename LIKE ? AND description LIKE ? ", [t,f,d])
#     with open("files/"+str(t)+"_"+f, 'wb') as output_file:
#            output_file.write(file[0][0])
#     return json.dumps("{'status':2}")

# @app.route('/fileUploadEmployee', methods=['POST'])
# def fileUploadEmployee():
#     try:
#         data = request.json
#         _filename = data["filename"].strip()
#         con = sqlite3.connect('ca_firm.db', detect_types=sqlite3.PARSE_DECLTYPES)
#         con.row_factory = sqlite3.Row
#         cur = con.cursor()
#         cur.execute('PRAGMA foreign_keys=ON;')
#         _f = open(_filename,'rb')
#         _split = os.path.split(_filename)
#         _file = _split[1]
#         _blob = _f.read()
#         t = int(data["token"])
#         d = data["desc"]
#         cur.execute('INSERT INTO completed_service_docs VALUES (?,?,?,?)', (t,sqlite3.Binary(_blob),_file,d))
#         _f.close()
#         con.commit()
#         cur.close()
#         con.close()
#         print("upload seccessful")
#     except Exception as ex:
#         print (ex)
#     return json.dumps("{'status':2}")

@app.route('/fileUploadEmployee', methods=['POST'])
def fileUploadEmployee():
    #data = request.json
    d= request.form['serv_desc']
    t= request.form['serv_token']
    print(d)
    f = request.files.getlist('serv_file')[0]
    filename =f.filename
    print(filename)
    cols = ("token" , "document", "description" , "filename")
    vals = (t , sqlite3.Binary(f.read()), d, filename)
    insert("completed_service_docs" , cols, vals)
    print("Uploaded")
    return json.dumps({'status':2})




#For a client to accept a service given quotation
@app.route('/acceptService', methods=['POST'])
def acceptService():
    data = request.json
    t = int(data["token"][0])
    s = query_db("UPDATE service SET accepted = ? \
         WHERE token_no = ?",[1, t])
    print("updated")
    checkexistence = query_db("SELECT * FROM SERVICE_STATUS WHERE token = ?", [t])
    if checkexistence is None:
        query_db("INSERT INTO SERVICE_STATUS (TOKEN,COMPLETED,VERIFIED,status_for_partner, status_for_client) values(?,0,0,'NO COMMENTS', 'accepted')", t)
    else:
        query_db("UPDATE SERVICE_STATUS SET status_for_client = 'Accepted' WHERE token = ?", [t])
    return json.dumps("{'status':2}")

#Download the invoice document to th invoice folder
@app.route('/invoiceFileDownload', methods=['POST'])
def invoiceFileDownload():
    data = request.json
    print("Downloading file...")
    print(data)
    f = data["filename"]
    f = f.strip()
    t = int(data["token"])
    g = data["gen"]
    regex = re.compile(r'[\n\r\t]')
    g = regex.sub("", g)
    a = float(data["amt"])
    print(f,t,g,a)
    file = query_db("SELECT invoice_document   FROM completed_service_invoice  \
               WHERE token = ? AND filename LIKE ?", [t,f])
    print(file)
    with open("invoice/"+str(t)+"_"+f, 'wb') as output_file:
           output_file.write(file[0][0])
    return json.dumps({'status':2})


#Logout
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   
   return render_template("ClientRegister.html"  )


def cover_str(cvr):
    cvr = request.files['cover']
    if cvr and allowed_file(cvr.filename):
        filename = (cvr.filename)
        cvr = cvr.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return cvr

#To submit a request from client
@app.route('/submitRequest',methods=['POST'])
def submitRequest():
    print("IN SUBMIT")
    #Get data from FE

    username =session['username']
    description = request.form['description']
    service = request.form['service']
    #Insert  the request to services tab;e
    cols = ("user", "type_of_service", "description" , "quotation" , "accepted" , "allocated")
    vals = (username , service , description, 0.0 , 0, 0)
    print(username , service, description)
    insert("service" , cols, vals)
    token = query_db("SELECT * FROM service WHERE user = ? AND type_of_service LIKE ? AND description LIKE ?", [username , service, description], one=True)
    token = token[1]
    print(token)
    #Add the following tokens to service status and allocation
    cols = ("token" , "completed", "verified", "remarks", "status_for_partner", "status_for_client")
    vals = (token , 0 , 0 , "", "" , "Not Accepted" )
    insert("service_status" , cols, vals)
    cols = tuple(["token"])
    vals = tuple([token])
    insert("service_allocation" , cols, vals)
    #Handling file uploads
    print("here in submit")
    print(service, description)
    #handle storing blob files
    desc = request.form.getlist('filedesc')
    print(desc)
    file = request.files.getlist('files[]')
    i = 0
    for f in file:
        print(f)
        filename = (f.filename)
        cols = ("token" , "document", "description" , "filename")
        vals = (token , sqlite3.Binary(f.read()) , desc[i], filename)
        i+=1
        insert("service_docs" , cols, vals)
    print(file)
    print(request.form)
    print(request.files)
    return json.dumps({"status":0, "token":token})    

#EMPLOYEE STARTS HERE
@app.route('/EmployeeHome')
def EmployeeHome():
    #testtext = session['testtext']
    name = session['username'] 
    s = query_db("SELECT token_no ,current_timestamp, quotation, type_of_service,  status_for_client, emp, ESTIMATED_HOURS  FROM service  \
        JOIN service_status ON token_no = service_status.token \
        JOIN service_allocation ON token_no = service_allocation.token \
         WHERE emp = ?", [name])
    m = query_db("SELECT sender , current_timestamp ,message  FROM messages  \
         WHERE recepient = ? ORDER BY current_timestamp DESC", [name])
    files = query_db("SELECT service_docs.token , filename , service_docs.description   FROM service_docs  \
                JOIN service ON service_docs.token = service.token_no \
                JOIN service_allocation ON service_docs.token = service_allocation.token \
         WHERE emp = ? ", [name])
    invoice = query_db("SELECT completed_service_invoice.token, generated_by , current_timestamp ,filename, invoice_amount  FROM completed_service_invoice  \
         JOIN service ON completed_service_invoice.token = token_no \
         JOIN service_allocation ON service_allocation.token = completed_service_invoice.token  \
         WHERE service_allocation.EMP = ? ORDER BY current_timestamp DESC", [name])


    print(files)
    rows4 = query_db("select S.TOKEN_NO,S.DESCRIPTION,S.TYPE_OF_SERVICE, S.current_timestamp, ESTIMATED_HOURS FROM SERVICE S JOIN SERVICE_STATUS SS ON S.TOKEN_NO = SS.TOKEN JOIN SERVICE_ALLOCATION ON S.TOKEN_NO = SERVICE_ALLOCATION.TOKEN WHERE SS.COMPLETED=0 AND SERVICE_ALLOCATION.EMP = ?", [name])
    
    rows5 = query_db("select S.TOKEN_NO,S.DESCRIPTION,S.TYPE_OF_SERVICE, S.current_timestamp, ESTIMATED_HOURS FROM SERVICE S JOIN SERVICE_STATUS SS ON S.TOKEN_NO = SS.TOKEN JOIN SERVICE_ALLOCATION ON S.TOKEN_NO = SERVICE_ALLOCATION.TOKEN WHERE SS.COMPLETED=1 AND SS.VERIFIED=0 AND SERVICE_ALLOCATION.EMP = ?", [name])
    return render_template("EMPLOYEEV2.html", username=name, items = s, messages= m, files=files, invoice=invoice,rows4=rows4, rows5=rows5)


@app.route('/complete', methods=['GET', 'POST'])
def complete():
    if request.method == 'POST':
        ReceivedValues = request.get_json()
        print(ReceivedValues)
        con = sql.connect(Database)
        con.row_factory = sql.Row
        cur = con.cursor()
        print(ReceivedValues.keys())
        # print(ReceivedValues["token"])
        checkexistence = query_db('SELECT * FROM SERVICE_STATUS WHERE TOKEN = ?', [ReceivedValues["token"]] )
        if checkexistence is None:
            query_db("INSERT INTO SERVICE_STATUS (TOKEN,COMPLETED,VERIFIED,status_for_partner) values(?,1,0,'NO COMMENTS')", [ReceivedValues["token"]])
        else:
            exe = query_db('UPDATE SERVICE_STATUS SET COMPLETED = 1 WHERE TOKEN = ?', [ReceivedValues["token"]])
        con.close()
        return "done"




@app.route('/partnerstatus', methods=['GET', 'POST'])
def partnerstatus():
    if request.method == 'POST':
        ReceivedValues = request.get_json()
        print(ReceivedValues)
        con = sql.connect(Database)
        con.row_factory = sql.Row
        cur = con.cursor()
        print(ReceivedValues["token"])
        checkexistence = query_db('SELECT * FROM SERVICE_STATUS WHERE TOKEN = ?', [ReceivedValues["token"]] )
        if checkexistence is None:
            query_db("INSERT INTO SERVICE_STATUS (TOKEN,COMPLETED,VERIFIED,status_for_partner) values(?,0,0,'NO COMMENTS')", [ReceivedValues["token"]])
        exe = query_db('UPDATE SERVICE_STATUS SET STATUS_FOR_PARTNER = ? WHERE TOKEN = ?',[ReceivedValues["status"], ReceivedValues["token"]])
        query_db('UPDATE SERVICE SET ALLOCATED=0 WHERE TOKEN_NO = ?', [ReceivedValues["token"]])
        query_db('DELETE FROM SERVICE_ALLOCATION WHERE TOKEN = ?', [ReceivedValues["token"]])
        con.close()
        return "done"

@app.route('/clientstatus', methods=['GET', 'POST'])
def clientstatus():
    if request.method == 'POST':
        ReceivedValues = request.get_json()
        print(ReceivedValues)
        con = sql.connect(Database)
        con.row_factory = sql.Row
        cur = con.cursor()
        print(ReceivedValues["token"])
        checkexistence = query_db('SELECT * FROM SERVICE_STATUS WHERE TOKEN = ?', [ReceivedValues["token"]] )
        print("checkexistence=", checkexistence)
        if checkexistence is None:
            query_db("INSERT INTO SERVICE_STATUS (TOKEN,COMPLETED,VERIFIED,status_for_partner) values(?,0,0,'NO COMMENTS')", [ReceivedValues["token"]])
            print("in the if statement")
        exe = query_db('UPDATE SERVICE_STATUS SET STATUS_FOR_CLIENT = ? WHERE TOKEN = ?',[ReceivedValues["status"], ReceivedValues["token"]])
        print(query_db('Select status_for_client from service_status where token = ?', [ReceivedValues["token"]]))
        con.close()
        return "done"

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True, port = 5002)
