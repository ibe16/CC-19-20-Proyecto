import os

from celery import Celery
import smtplib, ssl

broker = os.environ['CELERY_BROKER_URL']

app = Celery('notifier_rest', broker=broker)

port = os.environ['SMTP_PORT']
password=os.environ['PASSWORD']
email = os.environ['CORREO']
smtp_server=os.environ['SMTP_SERVER']

@app.task(name='Send_emails')
def send_emails(id_line, email_list):
    context = ssl.create_default_context()

    message = 'Subject: Downtime in line {id_line}\n\n This message is sent from Python.'.format(id_line=id_line)

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=context) 
        server.login(email, password)

        for receiver_email in email_list:
            server.sendmail(email, receiver_email, message)
    except Exception:
        print("Ha habido un error")
    finally:
        server.quit() 



