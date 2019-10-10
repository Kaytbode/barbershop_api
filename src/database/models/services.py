""" Service model module """
# pylint: disable=missing-docstring
# pylint: disable=no-member
from . import db


class Service(db.Model):
    """ Service table model """
    service_id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(50), nullable=False)
    location = db.Column(db.Text(), nullable=False)
    barber = db.Column(db.String, db.ForeignKey('barber.email'), nullable=False)
    start = db.Column(db.DateTime(), nullable=False)
    stop = db.Column(db.DateTime(), nullable=True)
    duration = db.Column(db.Integer(), nullable=True)
    fee = db.Column(db.String(12), nullable=True)
    status = db.Column(db.String(12), default='current')

    def add_service(self):
        service = Service(
            customer=self.customer,
            location=self.location,
            barber=self.barber,
            start=self.start,
            status=self.status
        )

        db.session.add(service)
        db.session.commit()

    @staticmethod
    def get_service(service_id):
        service = Service.query.get(service_id)

        return service

    def __repr__(self):
        return '<Service: {}>'.format(self.name)
