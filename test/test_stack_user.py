import json
import unittest

from alembic.testing.config import db

import app.api.v1.stack_user
from app.api.v1 import api
from app.api.v1.stack_questions import ns as questions_namespace
from config import create_app

""" Base Test case class, initialize variables and settings """


class StackUserTestCase(unittest.TestCase):
    """A base test case."""
    endpoint = 'app/api/v1/stack/stack_users'

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")

        api.init_app(self.app)
        api.add_namespace(questions_namespace)
        api.add_namespace(app.api.v1.stack_user.ns)

        self.client = self.app.test_client()

    def test_home(self):
        home = self.client.get('/')
        self.assertEqual(home.status_code, 200)

    def test_getting_user_id(self):
        result = self.client.get(self.endpoint + '/user/1')
        self.assertEqual(result.status_code, 200)

    def test_register_user(self):
        """Test API can create a user (POST request)"""
        user = {'id': 1, 'name': 'andeko', 'email': 'j.andeko.j@gmail.com', 'password': '123457andela#'}
        response = self.client.post(self.endpoint, data=json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')

    def tearDown(self):
        """The function leaves the test code clean after testing enhancing flexibility """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
