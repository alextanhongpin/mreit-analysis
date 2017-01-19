from flask import Flask

app = Flask(__name__, instance_relative_config=True)
# $ export FLASK_APP=app

# Setting up the config
app.config.from_object('config')
app.config.from_pyfile('config.py')

# print(app.config['DEBUG'])

from app.views import *

initViews(app)
# This is how you import dependencies
# from app.util import Greet
# import app.data as _

# url_for('static', filename='data.json')

