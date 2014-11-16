import unittest
from flask import current_app
from app import create_app
from app.extensions import db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = db

    def tearDown(self):
        self.db.connection.drop_database(
            current_app.config['MONGODB_SETTINGS']['DB'])
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

