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
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    edad = Column(String(250), nullable=True)
class History(Base):
    __tablename__ = 'histories'
    id = Column(Integer, primary_key=True)
    photo = Column(String(250), nullable=True)
    video = Column(String(250), nullable=True)
    text = Column(String(250), nullable=True)
    sticker = Column(String(250), nullable=False)
    form = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    history = relationship(User)
class Follower(Base):
    __tablename__ = 'Followers'
    user_id = Column(Integer, ForeignKey('users.id'),primary_key=True)
    follower_id = Column(Integer, ForeignKey('users.id'),primary_key=True)
    follower = relationship(User)
class Profilephoto(Base):
    __tablename__ = 'profilephotos'
    id = Column(Integer, primary_key=True)
    width = Column(String(250), nullable=False)
    heigth = Column(String(250), nullable=False)
    photo = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    profilephoto = relationship(User)
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    photo = Column(String(250), nullable=False)
    video = Column(String(250), nullable=False)
    text = Column(String(250), nullable=False)
    tag = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    hashtag = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    post = relationship(User)
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    symbol = Column(String(250), nullable=True)
    reference = Column(String(250), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('users.id'))
    comment = relationship(Post)
    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')