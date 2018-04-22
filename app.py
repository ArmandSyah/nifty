import os
from flask import Flask
from core.nifty import set_up_words

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DB_URI') or 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY') or 'default'


@app.shell_context_processor
def make_shell_context():
    return {'setup_words': set_up_words}


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000)
else:
    from db import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)
