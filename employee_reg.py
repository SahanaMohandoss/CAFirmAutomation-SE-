from flask import Flask
from flask import render_template
from flask import request
import sqlite3
from flask import json, session
from validate_email import validate_email
import re
import flask
app = Flask(__name__)

Database = 'ca_firm.db'



@app.route('/EmployeeHome')
def EmployeeHome():
    testtext = session['testtext']
    name = session['username'] 
    s = query_db("SELECT token_no ,current_timestamp, quotation, type_of_service,  status_for_client, emp, estimated_time_of_completion  FROM service  \
        JOIN service_status ON token_no = service_status.token \
        JOIN service_allocation ON token_no = service_allocation.token \
         WHERE emp = ?", [name])
    print(s)
    m = query_db("SELECT sender , current_timestamp ,message  FROM messages  \
         WHERE recepient = ? ORDER BY current_timestamp DESC", [name])
    print(m)
    files = query_db("SELECT completed_service_docs.token , filename , completed_service_docs.description   FROM completed_service_docs  \
                JOIN service ON completed_service_docs.token = service.token_no \
                JOIN service_allocation ON completed_service_docs.token = service_allocation.token \
         WHERE emp = ? ", [name])
    print(files)
    invoice = query_db("SELECT completed_service_invoice.token, generated_by , current_timestamp ,filename, invoice_amount  FROM completed_service_invoice  \
         JOIN service ON completed_service_invoice.token = token_no \
         JOIN service_allocation ON service_allocation.token = completed_service_invoice.token  \
         WHERE service_allocation.EMP = ? ORDER BY current_timestamp DESC", [name])


    print(invoice)

    rows4 = query_db("select S.TOKEN_NO,S.DESCRIPTION,S.TYPE_OF_SERVICE, S.current_timestamp, estimated_time_of_completion FROM SERVICE S JOIN SERVICE_STATUS SS ON S.TOKEN_NO = SS.TOKEN JOIN SERVICE_ALLOCATION ON S.TOKEN_NO = SERVICE_ALLOCATION.TOKEN WHERE SS.COMPLETED=0 AND SERVICE_ALLOCATION.EMP = ?", [name])
    
    rows5 = query_db("select S.TOKEN_NO,S.DESCRIPTION,S.TYPE_OF_SERVICE, S.current_timestamp, estimated_time_of_completion FROM SERVICE S JOIN SERVICE_STATUS SS ON S.TOKEN_NO = SS.TOKEN JOIN SERVICE_ALLOCATION ON S.TOKEN_NO = SERVICE_ALLOCATION.TOKEN WHERE SS.COMPLETED=1 AND SS.VERIFIED=0 AND SERVICE_ALLOCATION.EMP = ?", [name])
    return render_template("EMPLOYEEV2.html", username=name, items = s, messages= m, files=files, invoice=invoice,rows4=rows4, rows5=rows5)


@app.route('/complete', methods=['GET', 'POST'])
def complete():
    if request.method == 'POST':
        ReceivedValues = request.get_json()
        print(ReceivedValues)
        con = sql.connect(Database)
        con.row_factory = sql.Row
        cur = con.cursor()
        print(ReceivedValues["token"])
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
        exe = query_db('UPDATE SERVICE_STATUS SET STATUS_FOR_PARTNER = ? WHERE TOKEN = ?',[ReceivedValues["status"]], [ReceivedValues["token"]])
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
        exe = query_db('UPDATE SERVICE_STATUS SET STATUS_FOR_CLIENT = ? WHERE TOKEN = ?',[ReceivedValues["status"]], [ReceivedValues["token"]])
        con.close()
        return "done"

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)
