from .models.models import User, Post
from . import db

def create_user(username, email, password, profile_pic=None, bio=None):
    user = User(username=username, email=email, profile_pic=profile_pic, bio=bio)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def create_post(body, author):
    p = Post(body=body, author=author)
    db.session.add(p)
    db.session.commit()
    return p

def get_timeline(limit=5):
    return Post.query.order_by(Post.timestamp.desc()).limit(limit).all()
