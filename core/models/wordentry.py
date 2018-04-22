from db import db


class WordEntryModel(db.Model):
    __tablename__ = 'wordentries'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), unique=True)
    total_score = db.Column(db.Integer)
    frequency = db.Column(db.Integer)
    average = db.Column(db.Float(precision=2))

    def __init__(self, word: str, total_score: int, **kwargs):
        self.word = word.lower()
        self.total_score = total_score
        self.frequency = 1
        self.average = total_score

    def to_json(self):
        """
        returns json representation of WordEntryModel
        """
        return {'word': self.word, 'total': self.total_score,
                'frequency': self.frequency, 'average': self.average}

    @classmethod
    def find_by_word(cls, word):
        return cls.query.filter_by(word=word).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, score):
        self.total_score += score
        self.frequency += 1
        self.average = self.total_score / self.frequency
