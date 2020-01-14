import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    password = Column(String(250), nullable=False)
    fullname = Column(String(250), nullable=True)
    email = Column(String(250), nullable=False)
    phone_num = Column(Integer, nullable=False)
    profile_pic_url = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__ = 'followers'
    timestamp = Column(String(250), nullable=False)  
    denayorrejectoption = Column(String(250), nullable=True) 
    follower_status = Column(String(250), nullable=False)  
    follower_id = Column(Integer, ForeignKey('users.id'),primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'),primary_key=True)
    follower = relationship(User)
    user = relationship(User)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    photo_id = Column(String(250), nullable=False)
    img_url = Column(String(250), nullable=False)
    timestamp = Column(String(250), nullable=False)
    pic_descrition = Column(String(250), nullable=True)
    location = Column(String(250), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    photo_id = Column(Integer, nullable=False)
    comment = Column(String(250), nullable=True)
    img_url = Column(String(250), nullable=False)
    timestamp = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    posts_id = Column(Integer, ForeignKey('posts.id'))
    posts = relationship(Post)

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    photo_id = Column(Integer, nullable=False)
    liker_id = Column(Integer, nullable=False)
    timestamp = Column(String(250), nullable=False)
    img_url = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    posts_id = Column(Integer, ForeignKey('posts.id'))
    posts = relationship(Post)

    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')