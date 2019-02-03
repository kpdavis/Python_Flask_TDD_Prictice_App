'''
BaseTest

This class is the parent class to each no-unit test.
It allows for instatiation of the databaase dynamically
and makes sure that it is a new blank database each time.
'''

from unittest import TestCase
from app import app
from db import db

class BaseTest(TestCase):
    # setup db for each new session
    def setup(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'SQLITE:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()

            self.app = app.test_client()
            self.app_context = app.app_context()


    def tearDown(self):
        # Remove db on session close
        with app.app_context():
            db.session.remove()
            db.drop_all()
