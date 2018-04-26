from app import APP
from db import db
from core.nifty import set_up_words

db.init_app(APP)


@APP.before_first_request
def create_tables():
    db.create_all()
    set_up_words()
