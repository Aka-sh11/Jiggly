from main import app
from application.models import db, Role

with app.app_context():
    db.create_all()
    admin = Role(name='Admin', description='Administrator Description')
    db.session.add(admin)
    user = Role(name='User', description='User Description')
    db.session.add(user)
    creator = Role(name='Creator', description='Creator Description')
    db.session.add(creator)
    try:
        db.session.commit()
    except:
        pass    