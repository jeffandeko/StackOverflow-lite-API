from flask_api import FlaskAPI

import settings


class Config(object):
    """Main configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = settings.SECRET


class DevelopmentConfig(Config):
    """Configurations for Development stage."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}


def create_app(config_name):
    """Create a flask app instance."""
    app = FlaskAPI(__name__)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False

    return app
