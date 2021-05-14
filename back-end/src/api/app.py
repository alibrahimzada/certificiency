from __future__ import absolute_import
from flask import Flask
from flask_cors import CORS

# put __init__.py files in each directory

app = Flask(__name__)
CORS(app)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
config = {
    "development": "src.config.DevelopmentConfig",
    "testing": "src.config.TestingConfig",
    "production": "src.config.ProductionConfig"
}

from api.controllers import (user_controller, event_controller, certificate_controller,
                            customer_controller, auth_controller, role_controller, 
                            application_controller, event_category_controller)

app.register_blueprint(user_controller.bp, url_prefix='/api/v1/user')
app.register_blueprint(event_controller.bp, url_prefix='/api/v1/event')
app.register_blueprint(certificate_controller.bp, url_prefix='/api/v1/certificate')
app.register_blueprint(customer_controller.bp, url_prefix='/api/v1/customer')
app.register_blueprint(auth_controller.bp, url_prefix='/api/v1/auth')
app.register_blueprint(role_controller.bp, url_prefix='/api/v1/role')
app.register_blueprint(application_controller.bp, url_prefix='/api/v1/application')
app.register_blueprint(event_category_controller.bp, url_prefix='/api/v1/event_category')
# app.config.from_object(config[os.getenv('FLASK_CONFIGURATION', 'development')])

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
