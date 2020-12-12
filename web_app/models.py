from web_app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
import enum

class RoomType(enum.Enum):
    Economy = 0
    Business = 1
    Premium = 2

class CleanupType(enum.Enum):
    Standartní = 0
    Předúklid = 1
    Minibar = 2
    Kompletní = 3

class Room(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    r_type = db.Column(db.Enum(RoomType), nullable=False)

    cleanups = db.relationship('Cleanup', backref='room', cascade="all, delete-orphan")
    faults = db.relationship('Fault', backref='room', cascade="all, delete-orphan")
    discoveries = db.relationship('Discovery', backref='room', cascade="all, delete-orphan")

class Cleanup(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    c_type = db.Column(db.Enum(CleanupType), nullable=False)
    completed = db.Column(db.DateTime)
    to_be_completed = db.Column(db.DateTime, nullable=False)

class Fault(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

class Discovery(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable = False)
    isAdmin = db.Column(db.Boolean, nullable=False, default=False)
    name = db.Column(db.String(50), nullable = True)
    surname = db.Column(db.String(50), nullable = True)

    @property
    def unhashed_password(self):
        raise AttributeError('Cannot read unhashed password.')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)