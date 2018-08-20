import settings
from app.api.v1 import api
from app.api.v1.stack_user import ns as users_namespace
from config import create_app

config_name = settings.APP_ENVIRONMENT_SETTINGS  # config_name = "development"
app = create_app(config_name)

api.init_app(app)

api.add_namespace(users_namespace)

if __name__ == '__main__':
    app.run()
