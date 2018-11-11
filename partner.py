import sqlite3 as sql
from flask import g
from flask import Flask
from flask import render_template
from flask import request
from regression import regModel
from openpyxl import load_workbook

app = Flask(__name__,template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.before_request
def before_request():
    if 'localhost' in request.host_url or '0.0.0.0' in request.host_url:
        app.jinja_env.cache={}
'''
@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('partner.html',)
'''

@app.route('/')
def list():
    #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
    Database = 'ca_firm.db'
    con = sql.connect(Database)
    con.row_factory = sql.Row
  
    cur = con.cursor()
    
    exe = 'INSERT INTO CLIENT(USERNAME,PASSWORD,FIRST_NAME,LAST_NAME,EMAIL_ID,COMPANY,CONTACT_NO,PAN_NO) VALUES (?,?,?,?,?,?,?,?)'
    params =  ("sidvin97","pass","Sid","Vin","sid.fpl@gmail.com",1,"8971864700","dummy")
    cur.execute(exe,params)
    exe = 'INSERT INTO SERVICE(USER,TYPE_OF_SERVICE,DESCRIPTION,ACCEPTED,ALLOCATED) VALUES (?,?,?,?,?)'
    params =  ("sidvin97","Audit","This is service A",0,0)
    cur.execute(exe,params)
    

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
    con.close()
    return render_template("list.html",rows1=rows1,rows2=rows2,rows3=rows3,rows4=rows4,rows5=rows5)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("ummmmmm?")
        asd = request.get_json()
        print(asd)
        return "hey"
    #return render_template("partner.html")

@app.route('/quot', methods=['GET', 'POST'])
def quot():
    print("Here")
    if request.method == 'POST':
        enterDetail = request.get_json()
        print(enterDetail)
        #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        type_of_service=enterDetail["type"]
        est_hrs=int(enterDetail["time"])
        ob=regModel()
        amt=round(ob.model(type_of_service,est_hrs))
        out_txt="The quotation is: Rs. "+str(amt)
        print(out_txt)
        return out_txt

@app.route('/quotation', methods=['GET', 'POST'])
def quotation():
    if request.method == 'POST':
        enterDetail = request.get_json()
        print(enterDetail)
        #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        Database = 'ca_firm.db'
        con = sql.connect(Database)
        con.row_factory = sql.Row
        cur = con.cursor()
        print(enterDetail["quotation"])
        exe = 'UPDATE SERVICE SET QUOTATION=%s WHERE TOKEN_NO = %s' % (enterDetail["quotation"],enterDetail["token"])
        cur.execute(exe)
        exe = 'UPDATE SERVICE SET ESTIMATED_HOURS=%f WHERE TOKEN_NO = %s' % (float(enterDetail["time"]),enterDetail["token"])
        cur.execute(exe)
        exe = "select * from SERVICE"
        cur.execute(exe)
        rows = cur.fetchall()
        print(rows)
        con.commit()
        con.close()
        '''
        wb=load_workbook("regression_dataset.xlsx")
        ws=wb.worksheets[0]
        new_row_data=[enterDetail["type"],"No Description Available",float(enterDetail["time"]),float(enterDetail["quotation"])]
        print("Adding to the xlsx", new_row_data)
        ws.append(new_row_data)
        wb.save("regression_dataset.xlsx")
        '''
        return "done"

@app.route('/allocate', methods=['GET', 'POST'])
def allocate():
    if request.method == 'POST':
        allocateSer = request.get_json()
        print(allocateSer)
        
        #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        Database = 'ca_firm.db'
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
        #Database = '/Users/simrandhinwa/Desktop/SE/ca_firm.db'
        Database = 'ca_firm.db'
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
        Database = 'ca_firm.db'
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
        Database = 'ca_firm.db'
        con = sql.connect(Database,detect_types=sql.PARSE_DECLTYPES)
        con.row_factory = sql.Row 
        cur = con.cursor()
        token = mess["token"]
        exe = "select token,description from completed_service_docs where token=%s" % token
        cur.execute(exe)
        rows7 = cur.fetchall()
        print("right")
        print(rows7)
        return render_template("list.html",rows7=rows7)
        return "happy"

'''
        cur.execute("ALTER TABLE service Verified='Yes' where Token_No=%s",(toVerify.token,))
query_string = "SELECT * FROM p_shahr WHERE os = %s"
    cursor.execute(query_string, (username,))
'''

if __name__ == '__main__':
    app.jinja_env.auto_reload=True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=False)

#select Token_No, Document, Description from Service JOIN Service_Docs ON select * from Service, Service_Status where Service_Status.Completed = Yes