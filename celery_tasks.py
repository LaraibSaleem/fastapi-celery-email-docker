import logging
from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
from starlette.responses import JSONResponse
import smtplib
from email.message import EmailMessage


LOGGER = logging.getLogger(__name__)

# Initialize celery
celery = Celery('tasks', broker='amqp://user:password@broker:5672//')
# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)


# Send Email- Run Asynchronously with celery
# Example process of long running task
@celery.task(serializer='json')
def send_email(email_list):


    MAIL_SERVER = "smtp.googlemail.com"

    gmail_user = "user@gmail.com"
    gmail_password = "pw"

    email_subject = "This is subject"
    email_text = "This is text."

    msg = EmailMessage()
    msg.set_content(email_text)
    msg['From'] = gmail_user
    msg['To'] = email_list
    msg['Subject'] = email_subject
    try:
        server = smtplib.SMTP(MAIL_SERVER, 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
