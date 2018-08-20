class StackUser:
    def __init__(self, user, api):
        self.stack_user = None
        self.user = user
        self.api = api
        self.users = [
            {
                "id": 1,
                "name": "Jeff Andeko",
                "email": "j.andeko.j@gmail.com",
                "password": "andelaproject1"
            }
        ]

    def get_user(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        self.api.abort(404, "User {} doesn't exist".format(user_id))

    def create_user(self, data):
        user = dict()
        user['name'] = str(data.get('name'))
        user['email'] = str(data.get('email'))
        user['password'] = str(data.get('password'))

        """ The code ensures table id column value is unique """
        try:
            user['id'] = int(self.user[-1].get('id')) + 1
        except Exception as e:
            user['id'] = 1

            self.users.append(user)

        return user

    def update_user(self, id, data):
        user = self.get_user(id)
        user.update(data)
        return user

    def delete_user(self, id):
        user = self.get_user(id)
        self.users.remove(user)
