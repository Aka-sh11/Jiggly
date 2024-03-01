from flask import Flask, make_response
# from flask_restful import Api
from application.models import db, Users
from config import DevelopmentConfig
from application.apis import api
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    api.init_app(app)
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return Users.query.filter_by(id=identity).one_or_none()

    @jwt.invalid_token_loader
    def invalid_token_callback(msg):
        return make_response('invalid token', 401)

    @jwt.expired_token_loader
    def expired_token_callback(msg):
        return make_response('token expired', 401)

    with app.app_context():
        import application.routes
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)