import settings

from config import create_app

config_name = settings.APP_ENVIRONMENT_SETTINGS  # config_name = "development"
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
