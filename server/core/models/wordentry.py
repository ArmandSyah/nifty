"""
Model representation of our WordEntry object
"""
from db import db


class WordEntryModel(db.Model):
    """
    SQL Model for WordEntry
    """
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
        """
        SQLAlchemy query for WordEntry by word
        """
        return cls.query.filter_by(word=word).first()

    @classmethod
    def find_by_id(cls, _id):
        """
        SQLAlchemy query for WordEntry by id
        """
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        """
        SQLAlchemy commands for adding/updating row in database
        """
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        """
        SQLAlchemy commands for deleting row in database
        """
        db.session.delete(self)
        db.session.commit()

    def update(self, score):
        """
        Updates WordEntry's total score, frequency and average
        """
        self.total_score += score
        self.frequency += 1
        self.average = self.total_score / self.frequency
