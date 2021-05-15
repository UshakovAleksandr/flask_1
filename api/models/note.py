from api import db
from datetime import datetime
from api.models.user import User


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(64), index=True, unique=True)
    note_text = db.Column(db.String(64), index=True, unique=False)
    date = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'header': self.header,
            "note_text": self.note_text,
            "date": self.date
        }
