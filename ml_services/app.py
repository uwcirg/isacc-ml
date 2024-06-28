from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from ml_services import api


def create_app(testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask('isacc_ml_services')
    app.config.from_object('isacc_ml_services.config')
    app.config['TESTING'] = testing

    register_blueprints(app)
    configure_proxy(app)

    return app


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(api.views.base_blueprint)
    app.register_blueprint(api.ml_utils.blueprint)


def configure_proxy(app):
    """Add werkzeug fixer to detect headers applied by upstream reverse proxy"""
    if app.config.get('PREFERRED_URL_SCHEME', '').lower() == 'https':
        app.wsgi_app = ProxyFix(
            app=app.wsgi_app,

            # trust X-Forwarded-Host
            x_host=1,

            # trust X-Forwarded-Port
            x_port=1,
        )
