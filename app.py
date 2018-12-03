# -*- coding:utf-8 -*-

from flask import Flask
from flask import request, Response
import json
import Rules

app = Flask(__name__)


@app.route('/dm', methods=['GET', 'POST'])
def get_intention():
    model = Rules.Model(request.data)
    print(model)
    res = Rules.make_response(model)
    print(res)
    return json.dumps(res)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5050)