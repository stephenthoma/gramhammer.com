from app.extensions import bcrypt, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def authenticate(cls, email, password):
        """
        Check that user exists and password is correct
        """
        user = cls.query.filter_by(email=email).first()
        if user is None:
            return {'success': False, 'error': 'User Not Found'}
        user_sec = Security.query.filter_by(user_id=user.id).first()
        salt = user_sec.salt
        password_hashed = user.password
        password_correct = bcrypt.check_password_hash(password_hashed,
                                                      password + salt)
        if password_correct is False:
            return {'success': False, 'error': 'Incorrect Password'}
        return {'user': user}


class UserMeta(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))

    def __init__(self, user_id, firstname, lastname):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname


class Security(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    salt = db.Column(db.String(20))

    def __init__(self, salt):
        self.salt = salt
