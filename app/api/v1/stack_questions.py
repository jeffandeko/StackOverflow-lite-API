import logging

from flask_restplus import Resource

from app.api.v1 import api
from app.api.v1.serializers import stack_question
from app.instances.models import StackQuestion

log = logging.getLogger(__name__)

ns = api.namespace('api/v1/questions', description='Operations related to Questions')

Question_create = StackQuestion(api)


@ns.route('/')
class StackQuestion(Resource):
    """Shows a list of all questions, and lets you POST to add new question"""

    @ns.doc('list_questions')
    @ns.marshal_list_with(stack_question)
    def get_questions(self):
        """List all questions"""
        return Question_create.questions

    @ns.doc('create_question')
    @ns.expect(stack_question)
    @ns.marshal_with(stack_question, code=201)
    def post_questions(self):
        """Create a new question"""
        return Question_create.create_questions(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Question not found')
@ns.param('id', 'The question identifier')
class StackQuestionItem(Resource):
    """ The class Shows a single question item and lets you delete them"""

    @ns.doc('get_question')
    @ns.marshal_with(stack_question)
    def get_questions(self, id):
        """Fetch a given resource"""
        return Question_create.get_questions(id)

    @ns.doc('delete_question')
    @ns.response(204, 'Question deleted')
    def delete_questions(self, id):
        """Delete a question given its identifier"""
        Question_create.delete_questions(id)
        return '', 204

    @ns.expect(stack_question)
    @ns.marshal_with(stack_question)
    def put_questions(self, id):
        """Update a question given its identifier"""
        return Question_create.update_questions(id, api.payload)


@ns.route('/<int:id>/answer')
@ns.response(404, 'Answer not found, try again!')
@ns.param('id', 'The question Id')
class QuestionAnswer(Resource):
    """Show a single question answer and lets you delete them"""

    @ns.doc('that_get_answer')
    @api.marshal_with(stack_question, as_list=True)
    def get_questions(self, id):
        """Fetch a given question\'s answers """
        return Question_create.get_answers(id)

    @ns.doc('that_create_answer')
    @ns.marshal_with(stack_question, code=201)
    def post_questions(self, id):
        """Create a new answer"""
        return Question_create.create_answer(id, api.payload), 201
