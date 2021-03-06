# encoding=utf-8

import json
from flask import Flask, Response

app = Flask(__name__)


@app.route("/health")
def health():
    result = {'status': 'UP'}
    return Response(json.dumps(result), mimetype='application/json')


@app.route("/hello")
def getUser():
    result = {'name': 'python'}
    return Response(json.dumps(result), mimetype='application/json')


app.run(port=3001, host='0.0.0.0')
