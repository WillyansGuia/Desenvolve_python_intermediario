# Importando UserMixin
from flask_login import UserMixin
#importando Login
from app import login

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id =  db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullebale=False)
    password_hash = db.Column(db.String(128), nullable=False)

    #novos campos
    profile_pic = db.Column(db.String(300)) #URL para fotos de perfil
    bio = db.Column(db.Text)

    posts = db.relationship('Post', back_populates='author', lazy='dynamic'

    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password)
        return check_password_hash(self.password_hash, password)                        )

def load_user(id):
    return db.session.get(User, int(id))
