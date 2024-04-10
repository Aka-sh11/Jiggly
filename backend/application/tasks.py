from celery import shared_task
from .models import Users, Role
from datetime import datetime, timedelta, timezone
from jinja2 import Template

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_HOST = "localhost"
SMTP_PORT = 1025
SENDER_EMAIL = 'admin@jiggly.com'
SENDER_PASSWORD = ''


def send_email(to, subject, content_body):
    msg = MIMEMultipart()
    msg["To"] = to
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg.attach(MIMEText(content_body, 'html'))
    client = SMTP(host=SMTP_HOST, port=SMTP_PORT)
    client.send_message(msg=msg)
    client.quit()
    

@shared_task(ignore_result=True)
def daily_reminder():
    template = '''
    <p>
        Dear {{ name }},
    </p>
    <br />
    <p>
        We've noticed you haven't been using our Jiggly Music App recently.
    </p>
    <p>
        Dive into our latest tracks and albums. They are always up-to-date and available for your enjoyment.
    </p>
    <p>
        Excited to see you jiggle to our tunes soon.
    </p>
    <br />
    <p>
        Best Regards,
    </p>
    <p>
        Jiggly Team
    </p>
        <small>Feel the Music, Feel the Joy! </small>
    '''
    template = Template(template)
    timestamp = datetime.now(timezone.utc) - timedelta(hours=24)
    inactive_users = Users.query.filter(
        Users.last_visited < timestamp, Users.role.has(Role.name == 'User')).all()
    for user in inactive_users:
        subject = "We miss you " + user.username.capitalize() + "!"
        send_email(user.email, subject, template.render(name=user.username))

    
    
