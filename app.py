# -*- coding:utf-8 -*-

from flask import Flask
from flask import request, Response
import json
import Rules

app = Flask(__name__)


@app.route('/dm', methods=['GET', 'POST'])
def get_intention():
    print(request.form["utt"])
    print(request.form["user_key"])
    model = Rules.Model(request.form)

    res = Rules.make_response(model)
    print(res)
    return json.dumps(res)

@app.route('/nlu')
def get_intention_only():
    sent = request.args.get('sent')
    print("User utterance:", sent)
    # on local
    #intention = train.decode(sent)
    # on server
    req = {
        'utt': sent,
        'user_key': 'onlyNLU',
        'code': '0000',
        'options': 0,
    }

    model = Rules.Model(json.dumps(req))
    intention = model.intention
    print("Output:", intention)

    return intention


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3103)