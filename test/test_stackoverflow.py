import json
import unittest

from alembic.testing.config import db
from app.api.v1.stack_question import ns as questions_namespace

from app.api.v1 import api
from app.api.v1.stack_user import ns as users_namespace
from config import create_app

""" Base Test case class, initialize variables and settings """


class StackTestCase(unittest.TestCase):
    """A base test case."""
    endpoint = 'app/api/v1/stack/questions'

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")

        api.init_app(self.app)
        api.add_namespace(questions_namespace)
        api.add_namespace(users_namespace)

        self.client = self.app.test_client()

    def test_get_all_questions(self):
        """Test the user can get all questions (GET request)."""
        response = self.client.get(self.endpoint)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_get_one_question(self):
        response = self.client.get(self.endpoint + '1/')
        self.assertEqual(response.status_code, 200)

    def test_question_not_exist(self):
        response = self.app.get(self.endpoint)
        self.assertEqual(response.status_code, 404)

    def test_post_questions(self):
        # missing value field = bad
        stack_question = {
            "id": 1,
            "title": "What is Python",
            "description": "give your answer in words",
            "answers": []
        }

        response = self.client.post(self.endpoint, data=json.dumps(stack_question), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response = self.client.post(self.endpoint, data=json.dumps(stack_question), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_question_update(self):
        stack_question = {"value": 30}
        response = self.client.put(self.endpoint, data=json.dumps(stack_question), content_type='application/json')
        self.assertEqual(response.status_code, 'you question has been updated successfully', 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['stack_question']['value'], 30)

    def test_update_error(self):
        """ you cannot edit non-existing question"""
        stack_question = {"value": 30}
        response = self.app.put(self.endpoint, data=json.dumps(stack_question), content_type='application/json')
        self.assertEqual(response.status_code, 'you cannot edit non existing question', 404)
        stack_question = {"value": 'string'}
        response = self.app.put(self.endpoint, data=json.dumps(stack_question), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete(self):
        response = self.app.delete(self.endpoint)
        self.assertEqual(response.status_code, 204)
        response = self.app.delete(self.endpoint)
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        """The function leaves the test code clean after testing enhancing flexibility """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
