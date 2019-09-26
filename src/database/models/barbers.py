""" Barber model module """
# pylint: disable=missing-docstring
# pylint: disable=no-member
# pylint: disable=too-few-public-methods
from . import db

class Barber(db.Model):
    """ Barber table model """
    email = db.Column(db.String(50), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def save_barber(self):
        barber = Barber(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            password=self.password
        )

        db.session.add(barber)
        db.session.commit()

    def __repr__(self):
        return '<Barber: {}>'.format(self.name)
