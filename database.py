import sqlite3
conn=sqlite3.connect('ca_firm.db')
print("Connected successfully")

conn.execute('''DROP TABLE CLIENT;''')
conn.execute('''CREATE TABLE CLIENT 
            (USERNAME TEXT PRIMARY KEY NOT NULL,
            PASSWORD TEXT NOT NULL,
            FIRST_NAME TEXT NOT NULL,
            LAST_NAME TEXT NOT NULL,
            EMAIL_ID TEXT NOT NULL UNIQUE,
            COMPANY INTEGER NOT NULL CHECK (COMPANY >=0 AND COMPANY <2),
            CONTACT_NO TEXT NOT NULL,
            AADHAR_NO TEXT UNIQUE,
            PAN_NO TEXT NOT NULL UNIQUE);''')
print("Table CLIENT created successfully")


conn.execute('''DROP TABLE EMPLOYEE;''')
conn.execute('''CREATE TABLE EMPLOYEE 
            (USERNAME TEXT  NOT NULL UNIQUE,
            PASSWORD TEXT NOT NULL,
            FIRST_NAME TEXT NOT NULL,
            CONTACT_NO TEXT NOT NULL,
            LAST_NAME TEXT NOT NULL,
            EMPLOYEE_ID INTEGER PRIMARY KEY NOT NULL,
            EMAIL_ID TEXT NOT NULL UNIQUE);''')
print("Table EMPLOYEE created successfully")


conn.execute('''DROP TABLE PARTNER;''')
conn.execute('''CREATE TABLE PARTNER 
            (USERNAME TEXT NOT NULL UNIQUE,
            PASSWORD TEXT NOT NULL,
            FIRST_NAME TEXT NOT NULL,
            LAST_NAME TEXT NOT NULL,
            EMPLOYEE_ID INTEGER PRIMARY KEY NOT NULL,
            CONTACT_NO TEXT NOT NULL,
            EMAIL_ID TEXT NOT NULL UNIQUE);''')
print("Table PARTNER created successfully")


conn.execute('''DROP TABLE CLIENT_FILES''')
conn.execute('''CREATE TABLE CLIENT_FILES
            (USER TEXT PRIMARY KEY NOT NULL,
            DOCUMENT BLOB,
            DESCRIPTION TEXT,
            FOREIGN KEY(USER) REFERENCES CLIENT(USERNAME));''')
print("Table CLIENT_FILES created successfully")


conn.execute('''DROP TABLE REMINDERS''')
conn.execute('''CREATE TABLE REMINDERS
            (REMINDER_NAME TEXT NOT NULL,
            GENERATED_BY TEXT NOT NULL,
            REMINDER_TIMESTAMP TIMESTAMP NOT NULL,
            CURRENT_TIMESTAMP TIMESTAMP DEFAULT (DATETIME(CURRENT_TIMESTAMP,'localtime')),
            REMINDER_MESSAGE TEXT NOT NULL,
            MAILING_LIST TEXT NOT NULL,
            PRIMARY KEY(REMINDER_NAME,REMINDER_TIMESTAMP),
            FOREIGN KEY(GENERATED_BY) REFERENCES PARTNER(USERNAME));''')
print("Table REMINDERS created successfully")


conn.execute('''DROP TABLE SERVICE''')

conn.execute('''CREATE TABLE SERVICE
            (USER TEXT NOT NULL,
            TOKEN_NO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            TYPE_OF_SERVICE TEXT NOT NULL,
            QUOTATION REAL NOT NULL,
            DESCRIPTION TEXT NOT NULL,
            ACCEPTED INT NOT NULL CHECK (ACCEPTED >=0 AND ACCEPTED <2),
            ALLOCATED INT NOT NULL CHECK (ALLOCATED >=0 AND ALLOCATED <2)
            FOREIGN KEY(USER) REFERENCES CLIENT(USERNAME));''')
print("Table SERVICE created successfully")


conn.execute('''DROP TABLE MESSAGES''')
conn.execute('''CREATE TABLE MESSAGES
            (SENDER TEXT NOT NULL,
            RECEPIENT TEXT NOT NULL,
            MESSAGE TEXT NOT NULL,
            CURRENT_TIMESTAMP TIMESTAMP DEFAULT (DATETIME(CURRENT_TIMESTAMP,'localtime')),
            TOKEN INTEGER,
            FOREIGN KEY(TOKEN) REFERENCES SERVICE(TOKEN_NO));''')
print("Table MESSAGES created successfully")


conn.execute('''DROP TABLE REQUEST_FILES''')
conn.execute('''CREATE TABLE REQUEST_FILES
            (TOKEN INTEGER NOT NULL,
            REQUEST_MESSAGE TEXT NOT NULL,
            CURRENT_TIMESTAMP TIMESTAMP DEFAULT (DATETIME(CURRENT_TIMESTAMP,'localtime')),
           
            FOREIGN KEY(TOKEN) REFERENCES SERVICE(TOKEN_NO));''')
print("Table REQUEST_FILES created successfully")
#Removed  PRIMARY KEY(TOKEN,CURRENT_TIMESTAMP),

conn.execute('''DROP TABLE SERVICE_DOCS''')
conn.execute('''CREATE TABLE SERVICE_DOCS
            (TOKEN INTEGER NOT NULL,
            DOCUMENT BLOB,
            DESCRIPTION TEXT,
            PRIMARY KEY(TOKEN,DOCUMENT,DESCRIPTION),
            FOREIGN KEY(TOKEN) REFERENCES SERVICE(TOKEN_NO));''')
print("Table SERVICE_DOCS created successfully")


conn.execute('''DROP TABLE SERVICE_ALLOCATION''')
conn.execute('''CREATE TABLE SERVICE_ALLOCATION
            (TOKEN INTEGER NOT NULL,
            EMP TEXT NOT NULL,
            CURRENT_TIMESTAMP TIMESTAMP DEFAULT (DATETIME(CURRENT_TIMESTAMP,'localtime')),
            ALLOCATED_BY TEXT NOT NULL,
            ESTIMATED_HOURS INTEGER NOT NULL,
            PRIMARY KEY(TOKEN,EMP),
            FOREIGN KEY(TOKEN) REFERENCES SERVICE(TOKEN_NO),
            FOREIGN KEY(EMP) REFERENCES EMPLOYEE(USERNAME),
            FOREIGN KEY(ALLOCATED_BY) REFERENCES PARTNER(USERNAME));''')
print("Table SERVICE_ALLOCATION created successfully")


conn.execute('''DROP TABLE SERVICE_STATUS''')
conn.execute('''CREATE TABLE SERVICE_STATUS
            (TOKEN INTEGER PRIMARY KEY NOT NULL,
            COMPLETED INTEGER NOT NULL CHECK (COMPLETED >=0 AND COMPLETED <2)
            VERIFIED INTEGER NOT NULL CHECK (VERIFIED >=0 AND VERIFIED <2),
          	REMARKS TEXT,
            STATUS_FOR_PARTNER TEXT NOT NULL,
            STATUS_FOR_CLIENT TEXT,
            ESTIMATED_TIME_OF_COMPLETION TIMESTAMP,
            FOREIGN KEY(TOKEN) REFERENCES SERVICE(TOKEN_NO));''')
print("Table SERVICE_STATUS created successfully")


conn.execute('''DROP TABLE COMPLETED_SERVICE_DOCS''')
conn.execute('''CREATE TABLE COMPLETED_SERVICE_DOCS
            (TOKEN INTEGER NOT NULL,
            DOCUMENT BLOB,
            DESCRIPTION TEXT,
            PRIMARY KEY(TOKEN,DOCUMENT,DESCRIPTION),
            FOREIGN KEY(TOKEN) REFERENCES SERVICE_STATUS(TOKEN));''')
print("Table COMPLETED_SERVICE_DOCS created successfully")


conn.execute('''DROP TABLE COMPLETED_SERVICE_SUMMARY''')
conn.execute('''CREATE TABLE COMPLETED_SERVICE_SUMMARY
            (TOKEN INTEGER NOT NULL,
            SUMMARY TEXT,
            PRIMARY KEY(TOKEN,SUMMARY),
            FOREIGN KEY(TOKEN) REFERENCES SERVICE_STATUS(TOKEN));''')
print("Table COMPLETED_SERVICE_SUMMARY created successfully")


conn.execute('''DROP TABLE COMPLETED_SERVICE_INVOICE''')
conn.execute('''CREATE TABLE COMPLETED_SERVICE_INVOICE
            (TOKEN INTEGER PRIMARY KEY NOT NULL,
            GENERATED_BY TEXT,
            INVOICE_DOCUMENT BLOB,
            INVOICE_AMOUNT REAL,
            CURRENT_TIMESTAMP TIMESTAMP DEFAULT (DATETIME(CURRENT_TIMESTAMP,'localtime')),
            FOREIGN KEY(TOKEN) REFERENCES SERVICE_STATUS(TOKEN),
            FOREIGN KEY(GENERATED_BY) REFERENCES PARTNER(USERNAME));''')
print("Table COMPLETED_SERVICE_INVOICE created successfully")