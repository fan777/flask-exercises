from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    # TODO -- write tests for every view function / feature!

    def setUp(self):
        self.client = app.test_client()

    def test_homepage(self):

        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
