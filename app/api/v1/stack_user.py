import logging

from app.api.v1 import api
from app.api.v1.serializers import stack_user
from app.stack_user.models import StackUser

log = logging.getLogger(__name__)

ns = api.namespace('api/v1/users', description='Operations related to Users')

UserMaker = StackUser(api)


@ns.route('/')
class UsersList:
    """Shows a list of all users, and lets you POST to add new user"""

    @ns.doc('list_users')
    @ns.marshal_list_with(stack_user)
    def get(self):
        """List all users"""
        return UserMaker.users

    @ns.doc('create_user')
    @ns.expect(stack_user)
    @ns.marshal_with(stack_user, code=201)
    def post(self):
        """Create a new user"""
        return UserMaker.create_user(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'User not found')
@ns.param('id', 'The user identifier')
class User(Resource):
    """Show a single user item and lets you delete them"""

    @ns.doc('get_user')
    @ns.marshal_with(stack_user)
    def get(self, id):
        """Fetch a given resource"""
        return UserMaker.get_user(id)

    @ns.doc('delete_user')
    @ns.response(204, 'User deleted')
    def delete(self, id):
        """Delete a user given its identifier"""
        UserMaker.delete_user(id)
        return '', 204

    @ns.expect(stack_user)
    @ns.marshal_with(stack_user)
    def put(self, id):
        """Update a user given its identifier"""
        return UserMaker.update_user(id, api.payload)
