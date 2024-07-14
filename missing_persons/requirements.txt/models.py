from datetime import datetime
from db_helper import db

class Person(db.Model):
    id - db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=False)  # 'missing' or 'wanted'
    date_reported = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Person {self.name}>'
