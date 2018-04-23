from flask_restful import Resource, reqparse
from core.models.wordentry import WordEntryModel
from core.nifty import tokenize, analyze


class Sentence(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sentence', type=str, required=True,
                        help="This is required")

    def post(self):
        data = Sentence.parser.parse_args()
        sentence = data['sentence']
        sentence = tokenize(sentence)
        word_entries = [WordEntryModel.find_by_word(word) for word in sentence]
        word_entries = [word for word in word_entries if word]
        average = analyze(word_entries)
        return {'average': average}
