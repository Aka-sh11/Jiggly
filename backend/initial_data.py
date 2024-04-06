# from main import app
from application.models import db, Role, Users
from werkzeug.security import generate_password_hash

# with app.app_context():
#     db.create_all()
#     admin = Role(name='Admin', description='Administrator Description')
#     db.session.add(admin)
#     user = Role(name='User', description='User Description')
#     db.session.add(user)
#     creator = Role(name='Creator', description='Creator Description')
#     db.session.add(creator)
#     try:
#         db.session.commit()
#     except:
#         pass


def initial_data():
    from main import app
    with app.app_context():
        db.create_all()

        roles = [
            {'name': 'Admin', 'description': 'Administrator Description'},
            {'name': 'User', 'description': 'User Description'},
            {'name': 'Creator', 'description': 'Creator Description'}
        ]

        for role in roles:
            role_in_db = Role.query.filter_by(name=role['name']).first()
            if not role_in_db:
                new_role = Role(name=role['name'],
                                description=role['description'])
                db.session.add(new_role)

        user_in_db = Users.query.filter_by(username='akasharma').first()
        if not user_in_db:
            hashed_password = generate_password_hash('mad2jan24')
            user = Users(username='akasharma', password=hashed_password, email='22f2000700@ds.study.iitm.ac.in', role_id=1)
            db.session.add(user)
        
        try:
            db.session.commit()
        except:
            pass
