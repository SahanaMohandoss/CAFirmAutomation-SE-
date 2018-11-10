import sqlite3 as lite
import os
def insertfile(_filename):
    try:
        con = lite.connect('/Users/simrandhinwa/Desktop/SE/ca_firm.db', detect_types=lite.PARSE_DECLTYPES)
        con.row_factory = lite.Row
        cur = con.cursor()
        cur.execute('PRAGMA foreign_keys=ON;')
        _f = open(_filename,'rb')
        _split = os.path.split(_filename)
        _file = _split[1]
        _blob = _f.read()
        cur.execute('INSERT INTO completed_service_docs (token,document,description) VALUES (?,?,?)', (5,lite.Binary(_blob),"some"))
        _f.close()
        con.commit()
        cur.close()
        con.close()
    except Exception as ex:
        print(ex)
def getfile(_filename):
    try:
        con = lite.connect('/Users/simrandhinwa/Desktop/SE/ca_firm.db', detect_types=lite.PARSE_DECLTYPES)
        con.row_factory = lite.Row
        cur = con.cursor()
        cur.execute('PRAGMA foreign_keys=ON;')
        cur.execute('SELECT document from completed_service_docs where token = ?', (5,))
        _files = cur.fetchall()
        print("donee")
        print(_files)
        if len(_files) > 0:
            _file  = open('/Users/simrandhinwa/Desktop/SE/new.txt','w+')
            _file.write(_files[0][0])
            _file.close()
        cur.close()
        con.close()
    except Exception as ex:
        print(ex)
#insertfile('/Users/simrandhinwa/Desktop/SE/test.txt')
getfile('/Users/simrandhinwa/Desktop/SE/test.txt')
