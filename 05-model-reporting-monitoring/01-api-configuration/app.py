# -*- coding: utf-8 -*-
"""API configuration simple script.

API request demo command: curl -X GET "127.0.0.1:8000?user=Heber"

Created on: 12/5/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Says hello to user.

    Returns:
        Greeting.

    """
    user = request.args.get('user')

    return 'Hello ' + user + '\n'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
