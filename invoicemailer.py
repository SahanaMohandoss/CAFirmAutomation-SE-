import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def mailTo (fromaddr, toaddr, fpassword, filesList, fileNameList, subjectAtt=None, bodyAtt=None):
    msg = MIMEMultipart() 
  
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "CA Firm Service token "+ subjectAtt[0] +" has been completed"
    
    # string to store the body of the mail 
    body = "Dear "+bodyAtt[0]+",\n"+"The service "+bodyAtt[1]+" has been completed.\n PFA the corresponding documents and the invoice.\n Regards,\n CA Firm"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    for name, files in zip(fileNameList, filesList):

        # open the file to be sent  
        filename = name
        if (name is not None):
            file = open(name, 'wb')
            file.write(files)
            file.close()

            attachment = open(filename, "rb") 
        
        # instance of MIMEBase and named as p 
            p = MIMEBase('application', 'octet-stream') 
            
            # To change the payload into encoded form 
            p.set_payload((attachment).read()) 
            
            # encode into base64 
            encoders.encode_base64(p) 
            
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
            
            # attach the instance 'p' to instance 'msg' 
            msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(fromaddr, fpassword) # enter your password in clear text. LOL!
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    
    # terminating the session 
    s.quit() 