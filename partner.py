import sqlite3 as sql
from flask import g
from flask import Flask
from flask import render_template
from flask import request
import json
import datetime
app = Flask(__name__,template_folder='templates')

'''
@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('partner.html',)
'''
Database = "ca_firm"
@app.route('/')
def list():
    #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
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
    cur.execute("select S.TOKEN_NO,S.DESCRIPTION,S.TYPE_OF_SERVICE FROM SERVICE S JOIN SERVICE_STATUS SS ON S.TOKEN_NO = SS.TOKEN WHERE SS.COMPLETED=0")
    rows4 = cur.fetchall()
    cur.execute("select S.TOKEN_NO,S.DESCRIPTION,S.TYPE_OF_SERVICE FROM SERVICE S JOIN SERVICE_STATUS SS ON S.TOKEN_NO = SS.TOKEN WHERE SS.COMPLETED=1 AND SS.VERIFIED=0")
    rows5 = cur.fetchall()
    cur.execute("select EMAIL_ID from CLIENT")
    client_mail = cur.fetchall()
    cur.execute("select * from completed_service_docs")
    service_docs = cur.fetchall()   
    #cur.execute("select TOKEN_NO,DESCRIPTION,TYPE_OF_SERVICE,FEEDBACK ,SENTIMENT FROM SERVICE")
    #feedback = cur.fetchall()
    con.close()
    return render_template("list.html",rows1=rows1,rows2=rows2,rows3=rows3,rows4=rows4,rows5=rows5,client_mail=client_mail,service_docs=service_docs)#,feedback=feedback)


def query_db(query, args=(), one=False):
    con = sql.connect(Database)
    cur = con.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    con.commit()
    return (rv[0] if rv else None) if one else rv


def get_time():
	now=datetime.datetime.now()
	#today=str(today)
	#toks=today.split(' ')
	#toks1=toks[0].split('-')
	#for i i
	#print(toks)
	#print(toks1)
	today=str(now.year)+"-"+str(now.month)+"-"+str(now.day)
	return today
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("ummmmmm?")
        asd = request.get_json()
        print(asd)
        return "hey"
    #return render_template("partner.html")


@app.route('/filee', methods=['GET', 'POST'])
def filee():
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



@app.route('/reminder', methods=['GET', 'POST'])
def reminder():
    if request.method == 'POST':
        print("ummmmmm?")
        rem = request.get_json()
        #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        con = sql.connect(Database)
        con.row_factory = sql.Row
        cur = con.cursor()
        ids = ""
        for id in rem["mailing_list"]:
                ids += id + ";"
        ids = ids[:-1]

        exe = 'INSERT INTO REMINDERS (REMINDER_NAME,GENERATED_BY,REMINDER_TIMESTAMP,CURR_TIMESTAMP,REMINDER_MESSAGE,MAILING_LIST) VALUES(?,?,?,?,?,?)'
        param = (rem["reminder_name"],rem["generated_by"],get_time(),rem["curr_timestamp"],rem["reminder_message"],ids)
        cur.execute(exe,param)
        con.commit()
        con.close()
        print(rem)
        return "hey"
    #return render_template("partner.html")

@app.route('/quotation', methods=['GET', 'POST'])
def quotation():
    if request.method == 'POST':
        enterDetail = request.get_json()
        print(enterDetail)
        #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        con = sql.connect(Database)
        con.row_factory = sql.Row
        cur = con.cursor()
        print(enterDetail["quotation"])
        exe = 'UPDATE SERVICE SET QUOTATION=%s ESTIMATED_HOURS =%s WHERE TOKEN_NO = %s' % (enterDetail["quotation"],enterDetail["time"],enterDetail["token"])
        cur.execute(exe)
        con.commit()
        con.close()
        return "done"

@app.route('/allocate', methods=['GET', 'POST'])
def allocate():
    if request.method == 'POST':
        allocateSer = request.get_json()
        print(allocateSer)
        
        #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        con = sql.connect(Database)
        con.row_factory = sql.Row
        cur = con.cursor()
        exe = 'INSERT INTO SERVICE_ALLOCATION (TOKEN,EMP,ALLOCATED_BY) VALUES (?,?,?)'
        params =  (allocateSer["token"],allocateSer["employee"],allocateSer["partner"])
        cur.execute(exe,params)
        con.commit() 
        con.close()
        return "done"

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        toVerify = request.get_json()
   
        print(toVerify)
        #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        con = sql.connect(Database)
        con.row_factory = sql.Row 
        cur = con.cursor()
        exe = "UPDATE SERVICE_STATUS SET VERIFIED=1 WHERE TOKEN= %s" % (toVerify["token"])
        cur.execute(exe)
        con.commit()
        return "cutes"

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        mess = request.get_json()
        #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        con = sql.connect(Database)
        con.row_factory = sql.Row 
        cur = con.cursor()
        token = mess["token"]
        exe = "select EMP from SERVICE_ALLOCATION where TOKEN=?"
        para = (token,)
        cur.execute(exe,para)
        emp = cur.fetchall()
        print("here")
        print(token)
        print(emp[0][0])
        params =  (mess["sender"],emp[0][0],mess["message"],mess["token"])
        exe = "INSERT INTO MESSAGES (SENDER,RECEPIENT,MESSAGE,TOKEN) VALUES(?,?,?,?)"
        cur.execute(exe,params)
        con.commit()
        return "cutes"


@app.route('/getDocs', methods=['GET', 'POST'])
def getDocs():
    if request.method == 'POST':
        mess = request.get_json()
        #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        con = sql.connect(Database,detect_types=sql.PARSE_DECLTYPES)
        con.row_factory = sql.Row 
        cur = con.cursor()
        token = mess["token"]
        exe = "select token,description from completed_service_docs where token=%s" % token
        cur.execute(exe)
        rows7 = cur.fetchall()
        print("right")
        print(rows7)
        a = []
        for i in rows7:
                a.append(i)
        print(a)
        #return render_template("list.html",rows7=rows7)
        return a

'''
        cur.execute("ALTER TABLE service Verified='Yes' where Token_No=%s",(toVerify.token,))
query_string = "SELECT * FROM p_shahr WHERE os = %s"
    cursor.execute(query_string, (username,))
'''

if __name__ == '__main__':
    app.run(debug=False)

#select Token_No, Document, Description from Service JOIN Service_Docs ON select * from Service, Service_Status where Service_Status.Completed = Yes