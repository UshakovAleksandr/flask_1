from api import db
import hashlib
from config import Config
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    notes = db.relationship("Note", backref='user', lazy='joined', cascade="all, delete-orphan")

    def set_password(self, password: str):
        salt_password = f'{password}{Config.SALT}'
        self.password = pwd_context.encrypt(salt_password)

    def verify_password(self, password):
        return pwd_context.verify(f"{password}{Config.SALT}", self.password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
