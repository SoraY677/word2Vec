from flask import Flask, jsonify, request
import json
from gensim.models import KeyedVectors

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

wv = KeyedVectors.load_word2vec_format('./model.vec.pt', binary=True)


@app.route('/moderation')
def index():
    param_plus = request.args.get('plus')
    param_minus = request.args.get('minus')
    result = wv.most_similar(positive=param_plus, negative=param_minus)[0][0]
    return jsonify({
        "result": result}
    )


if __name__ == '__main__':
    app.run()
