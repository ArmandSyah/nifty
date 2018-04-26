"""
    File for starting up Flask application and defining our routes
"""
import os
from flask import Flask
from flask_restful import Api

from api.wordentry import WordEntry, WordEntryList
from api.sentence import Sentence
from core.nifty import set_up_words

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DB_URI') or 'sqlite:///data.db'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
APP.secret_key = os.environ.get('SECRET_KEY') or 'default'
API = Api(APP)


@APP.shell_context_processor
def make_shell_context():
    """
        Sets up Shell Command for 'flask shell' to handle db setup 
    """
    return {'setup_words': set_up_words}


@APP.cli.command()
def initdb():
    set_up_words()


API.add_resource(WordEntry, '/wordentry/<string:word>')
API.add_resource(WordEntryList, '/wordentries')
API.add_resource(Sentence, '/sentence')

if __name__ == '__main__':
    from db import db
    db.init_app(APP)
    APP.run(port=5000)
else:
    from db import db, migrate
    db.init_app(APP)
    migrate.init_app(APP, db)
