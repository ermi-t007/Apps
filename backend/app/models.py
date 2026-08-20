from sqlalchemy import Column, Integer, String, DateTime, JSON, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=True)
    youtube_refresh_token = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Channel(Base):
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    channel_id = Column(String, nullable=False)
    rss_url = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)
    last_checked_at = Column(DateTime(timezone=True), nullable=True)

class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey('channels.id'))
    youtube_video_id = Column(String, nullable=False)
    path = Column(String, nullable=True)
    status = Column(String, default='pending')
    metadata = Column(JSON, nullable=True)

class Clip(Base):
    __tablename__ = 'clips'
    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, ForeignKey('videos.id'))
    start_s = Column(Integer)
    end_s = Column(Integer)
    score = Column(Integer, nullable=True)
    path = Column(String, nullable=True)
    uploaded_at = Column(DateTime(timezone=True), nullable=True)
