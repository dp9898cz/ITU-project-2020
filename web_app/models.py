from web_app.extensions import db
import enum

class RoomType(enum.Enum):
    Economy = 0
    Business = 1
    Premium = 2

class CleanupType(enum.Enum):
    Standartni = 0
    Preduklid = 1
    Minibar = 2

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

class Discovery(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    description = db.Column(db.String, nullable=False)