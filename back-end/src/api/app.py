from __future__ import absolute_import
from flask import Flask
# from flask_cors import CORS

# put __init__.py files in each directory

app = Flask(__name__)
#CORS(app, origins='*')
# CORS(app)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
config = {
    "development": "src.config.DevelopmentConfig",
    "testing": "src.config.TestingConfig",
    "production": "src.config.ProductionConfig"
}

# app.config.from_object(config[os.getenv('FLASK_CONFIGURATION', 'development')])

@app.route('/')
def hello():
    return {"test": "Hello World!"}

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
