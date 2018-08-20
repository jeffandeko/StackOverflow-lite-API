from flask_restplus import fields

from app.api.v1 import api

stack_question = api.model('StackQuestion', {
    'id': fields.Integer(readOnly=True, description=' This the question unique identifier'),
    'title': fields.String(required=True, description='This is the title of tehe Question'),
    'description': fields.String(required=True, description='The question details'),
    'answers': fields.List(cls_or_instance=fields.Raw)
})

stack_answer = api.model('StackAnswer', {
    'id': fields.Integer(readOnly=True, description='This is the question unique identifier'),
    'answer': fields.String(required=True, description='This is the answer given'),
    'user': fields.String(required=True, description='This is the name of the user')
})

stack_user = api.model('StackUser', {
    'id': fields.Integer(readOnly=True, description='This is the user unique identifier'),
    'name': fields.String(required=True, description='This is the name of the user'),
    'email': fields.String(required=True, description='This is the email details'),
    'password': fields.String(required=True, description='This is the password details')
})
