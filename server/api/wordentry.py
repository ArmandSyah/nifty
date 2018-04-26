"""
API methods for WordEntry
"""
from flask_restful import Resource, reqparse
from core.models.wordentry import WordEntryModel


class WordEntry(Resource):
    """
    WordEntry contains our HTTP methods and a parser to derive
    data from response body
    """
    parser = reqparse.RequestParser()
    parser.add_argument('score', type=int, required=True,
                        help="Every word must be scored")

    def get(self, word):
        """
        HTTP GET method
        """
        word_entry = WordEntryModel.find_by_word(word)
        if word_entry:
            return word_entry.to_json()
        return {'message': 'Word not found'}, 404

    def post(self, word):
        """
        HTTP POST method
        """
        if WordEntryModel.find_by_word(word):
            return {'message': "An word with name '{}' already exists.".format(word)}, 400
        data = WordEntry.parser.parse_args()
        word_entry = WordEntryModel(word, data['score'])

        try:
            word_entry.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return word_entry.to_json(), 201

    def delete(self, word):
        """
        HTTP DELETE method
        """
        word_entry = WordEntryModel.find_by_name(word)
        if word_entry:
            word_entry.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self, name):
        """
        HTTP PUT method
        """
        data = WordEntry.parser.parse_args()

        word_entry = WordEntryModel.find_by_name(name)

        if word_entry:
            word_entry.update(data['score'])
        else:
            word_entry = WordEntryModel(name, data['score'])

        word_entry.save_to_db()

        return word_entry.to_json()


class WordEntryList(Resource):
    """
    Retrieve entire list of words from db
    """

    def get(self):
        """
        HTTP GET method
        """
        return {'words': [word.to_json() for word in WordEntryModel.query.all()]}
