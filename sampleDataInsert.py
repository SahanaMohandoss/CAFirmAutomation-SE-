import sqlite3
def createConn(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def insertEmployee(conn, empData):
    sql_query = ''' INSERT INTO EMPLOYEE(USERNAME, PASSWORD, FIRST_NAME, CONTACT_NO, LAST_NAME, EMPLOYEE_ID, EMAIL_ID)
    VALUES(?,?,?,?,?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sql_query,empData)
    return cursor.lastrowid

def insertService(conn, servData):
    sql_query = ''' INSERT INTO SERVICE(USER, 
    TYPE_OF_SERVICE,
    QUOTATION,
    DESCRIPTION,
    ACCEPTED,
    ALLOCATED,
    ESTIMATED_HOURS,
    FEEDBACK,
    SENTIMENT) 
    VALUES(?,?,?,?,?,?,?,?,?)
    '''
    cur = conn.cursor()
    cur.execute(sql_query, servData)
    return cur.lastrowid

def insertClient(con, clieData):
    sql_query = '''
    INSERT INTO CLIENT (
        USERNAME,
        PASSWORD,
        FIRST_NAME,
        LAST_NAME,
        EMAIL_ID,
        COMPANY,
        CONTACT_NO,
        AADHAR_NO,
        PAN_NO
    )
    VALUES(?,?,?,?,?,?,?,?,?)
    '''

    cur = con.cursor()
    cur.execute(sql_query, clieData)
    return cur.lastrowid

def insertPart(conn, partData):
    sql_query = '''
    INSERT INTO PARTNER(
        USERNAME,
        PASSWORD,
        FIRST_NAME,
        LAST_NAME,
        EMPLOYEE_ID,
        CONTACT_NO,
        EMAIL_ID
    )
    VALUES(?,?,?,?,?,?,?)
    '''

    cur = conn.cursor()
    cur.execute(sql_query, partData)
    return cur.lastrowid

def insertServStat(con, ssdata):
    sql_query = '''
    INSERT INTO SERVICE_STATUS(
        TOKEN,
        COMPLETED,
        VERIFIED,
        REMARKS,
        STATUS_FOR_PARTNER,
        STATUS_FOR_CLIENT
    ) VALUES(?,?,?,?,?,?)
    '''
    cur = con.cursor()
    cur.execute(sql_query, ssdata)
    return cur.lastrowid

def insertCompDoc(con, docData):
    sql_query = '''
    INSERT INTO COMPLETED_SERVICE_DOCS(
        TOKEN,
        DESCRIPTION
    ) VALUES(?,?)
    '''

    cur = con.cursor()
    cur.execute(sql_query, docData)
    return cur.lastrowid

def insertCompInv(conn, invData):
    sql_query='''
    INSERT INTO COMPLETED_SERVICE_INVOICE(
        TOKEN,
        GENERATED_BY
    ) VALUES(?,?)
    '''
    cur = conn.cursor()
    cur.execute(sql_query, invData)
    return cur.lastrowid

'''
    tables to work on:
        client - 
        employee -
        partner -
        service -
        completed_service_docs -
        completed_service_invoice -

        
'''




if (__name__ == '__main__'):
    db = 'ca_firm.db'

    con = createConn(db)
    with con:
        emp1 = ('abc1','abc','abc',123,'cba',12,'g@g.c')
        emp2 = ('def2','def','def',456,'fed',23,'b@b.c')
        emp3 = ('ghi3','ghi','ghi',789,'ihg',34,'c@c.c')

        serv1 = ('cli1','a',56,'qweqwe',0,0,23,'qweqw','pos')
        serv2 = ('cli2','b',67,'werwer',1,0,34,'qweq','pos')
        serv3 = ('cli3','c',78,'ertert',1,0,56,'ewrwe','neg')

        cli1 = ('cli1','ilc','client1','ent','shivassv97@gmail.com',0,889,'sdfasf','qelihfb')
        cli2 = ('cli2','ilc','client2','bent','simrandhinwa@gmail.com',1,890,'dfgddfg','jhefb')
        cli3 = ('cli3','ilc','client3','kent','shardulsingh1@gmail.com',1,900,'erwwer','duhfb')
        cli4 = ('ganmann','iop', 'client4', 'bob', 'shivasv97@gmail.com', 1, 909, 'fgwe','wrgw')

        par1 = ('shiv','bobgg','shiv','sv',54,8900,'shivassv97@gmail.com')
        par2 = ('abc','wer','fgb','tnh',3343,6676,'shivasv97@gmail.com')

        doc1 = (1,'svsvsdv')
        doc2 = (2,'rgtnert')

        inv1 = (1,'shiv')
        inv2 = (2,'shiv')

        ss1 = (1, 1, 0, 'asda', 'asfa', 'gdas')
        ss2 = (2, 1, 1, 'sdfa','wergw','tjyjr')

        '''i1 = insertEmployee(con, emp1)
        i1 = insertEmployee(con, emp2)
        i1 = insertEmployee(con, emp3)

        i1 = insertService(con, serv1)
        i1 = insertService(con, serv2)
        i1 = insertService(con, serv3)

        i1 = insertClient(con, cli1)
        i1 = insertClient(con, cli2)
        i1 = insertClient(con, cli3)

        i1 = insertPart(con, par1)
        i1 = insertPart(con, par2)

        i1 = insertCompInv(con, inv1)
        i1 = insertCompInv(con, inv2)

        i1 = insertCompDoc(con, doc1)
        i1 = insertCompDoc(con, doc2)

        i1 = insertServStat(con, ss1)
        i1 = insertServStat(con, ss2)'''
        cur1 = con.cursor()
        """cur1.execute('''UPDATE SERVICE_STATUS
SET COMPLETED = 1 WHERE TOKEN = 1; ''',)
        cur1 = con.cursor()
        cur1.execute('''UPDATE SERVICE_STATUS
SET COMPLETED = 1 WHERE TOKEN = 2; ''',)"""
        #cur1.execute('''DELETE FROM COMPLETED_SERVICE_INVOICE WHERE TOKEN=2''')
        i1 = insertClient(con, cli4)

        '''empdata1 = ('emp1322', '123', 'bob', '789', 'gg', 1238, 'shi@g.c')
        empdata2 = ('empali12', '124', 'alu', '234', 'ali', 1239, 'vdi@g.c')
        empRowId1 = insertEmployee(con, empdata1)
        empRowId2 = insertEmployee(con, empdata2)

        servdata1 = ('bbki','type1',45.2,'some work desc',0,0,34,'solid work', 'pos')
        servdata2 = ('ganmann','type4',32.2,'some work desc again',1,0,12,'fast n good work', 'pos')
        servRowId1 = insertService(con, servdata1)
        servRowId2 = insertService(con, servdata2)'''