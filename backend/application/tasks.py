from sqlalchemy import func
from celery import shared_task
from .models import Users, Role, Songs, Album
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
        Jiggly App Team
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


@shared_task(ignore_result=True)
def monthly_report():
    template = '''
    <style>
      table {
        width: 60%;
        border-collapse: collapse;
      }
      th,
      td {
        padding: 5px;
        text-align: left;
        border-bottom: 1px solid #ddd;
      }
      th {
        background-color: #9ac5e7;
      }
      h3 {
        text-align: center;
      }
    </style>
    <h3>Your Monthly Report : Jiggly App</h3>
    Total Songs: {{ total_songs }} <br />
    Total Albums: {{ total_albums }} <br />
    Total Likes: {{ total_likes }} <br />
    Average Rating: {{ avg_rating }}
    <br /><br />
    <table border="1">
      <thead>
        <tr>
          <th>Song</th>
          <th>Genre</th>
          <th>Likes</th>
          <th>Flags</th>
        </tr>
      </thead>
      <tbody>
        {% for song in songs %}
        <tr>
          <td>{{ song['title'] }}</td>
          <td>{{ song['genre'] }}</td>
          <td>{{ song['likes'] }}</td>
          <td>{{ song['flags'] }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
    <br />
    <p>Thank you for using Jiggly App!</p>
    <p>
      Best Regards, <br />
      Jiggly App Team
    </p>
    <p>Disclaimer: This is an auto-generated email. Please do not reply.</p>
    '''
    template = Template(template)
    creators = Users.query.filter(Users.role.has(Role.name == 'Creator')).all()
    for creator in creators:
        songs = Songs.query.filter(Songs.user_id == creator.id).all()
        albums = Album.query.filter(Album.user_id == creator.id).all()
        
        total_songs = len(songs)
        total_albums = len(albums)
        total_likes = sum([song.likes for song in songs])
        total_ratings = sum([rating.rating for song in songs for rating in song.ratings])
        avg_rating = round(total_ratings / total_songs if total_songs > 0 else 0, 2)
        subject = "Monthly Report"
        content = template.render(songs=songs, total_songs=total_songs, total_albums=total_albums,
                                  total_likes=total_likes, avg_rating=avg_rating)
        send_email(creator.email, subject, content)
        
        
        
    
    
