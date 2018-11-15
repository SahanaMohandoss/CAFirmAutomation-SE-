import datetime
from celery import Celery
from celery import group
CELERY_TIMEZONE = 'Asia/Calcutta'
CELERY_INCLUDE = True
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from celery.schedules import crontab
import sqlite3 as sql


app=Celery('tasks',broker='amqp://localhost//',backend='amqp://localhost//')

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

def isSame(curr_time,rem_time):
	curr_toks=[int(i) for i in curr_time.split("-")]
	rem_toks=[int(i) for i in rem_time.split("-")]
	'''
	if(curr_toks[0]==rem_toks[0] and curr_toks[1]==rem_toks[1] and curr_toks[2]==rem_toks[2]):
		return 1
	else:
		return 0
	'''
	if(curr_toks[0]<rem_toks[0]):
		return 1
	else:
		if(curr_toks[1]<rem_toks[1]):
			return 1
		else:
			if(rem_toks[2]<=curr_toks[2]):
				return 1
			else: 
				return 0

@app.task
def send_reminders():
	Database = 'ca_firm.db'
	con = sql.connect(Database)
	con.row_factory = sql.Row
	cur = con.cursor()
	MY_ADDRESS="se.cafirm@gmail.com"
	MY_PASSWORD="seaccount"
	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login(MY_ADDRESS, MY_PASSWORD)
	exe='SELECT * FROM REMINDERS WHERE SENT=0 ORDER BY REMINDER_TIMESTAMP ASC'
	cur.execute(exe)
	rows3 = cur.fetchall()
	for i in rows3:
		reminders_id=i[0]
		#print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
		subject=i[1]
		curr_time=get_time()
		rem_time=i[3]
		message=i[5]
		mailing_list=i[6].split(";")
		send=isSame(curr_time,rem_time)
		print("Mail Subject: ",subject)
		print("Current Time: ",curr_time)
		print("Reminder Time: ",rem_time)
		print("Send Reminder: ",send)
		print("Reminder Message: ",message)
		print("Mailing List: ",mailing_list)
		print("\n\n")
		if(send): 
			for j in mailing_list:
				msg = MIMEMultipart()
				msg['From']=MY_ADDRESS
				msg['To']=j
				msg['Subject']=subject
				msg.attach(MIMEText(message, 'plain'))
				try:
					s.send_message(msg)
					del msg
				except:
					continue
			exe = "UPDATE REMINDERS SET SENT=1 WHERE REMINDER_ID= %d" % (reminders_id)
			cur.execute(exe)
			con.commit()	    
	# Terminate the SMTP session and close the connection
	con.close()
	s.quit()


app.conf.update(
	beat_schedule=
	{
	'run-every-2-minutes':{
		'task':'tasks.send_reminders',
		'schedule':crontab(minute='*/2'),
		}
	}
)
