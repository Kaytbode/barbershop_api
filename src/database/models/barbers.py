""" Barber model module """
from . import db

class Barber(db.Model):
    """ Barber table model """
    email = db.Column(db.String(50), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Barber: {}>'.format(self.name)
