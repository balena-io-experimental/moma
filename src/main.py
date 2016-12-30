# from flask import Flask, jsonify, request
from klein import run, route, Klein
from twisted.internet import defer, task, reactor
from twisted.web.static import File
import json

import automationhat
from settings import defaults
# from flask_cors import CORS, cross_origin

# app = Flask(__name__, static_url_path='', static_folder='ui/build')
# CORS(app)

app = Klein()

val = 0

def number_to_word(id):
    if int(id) == 1:
        return "one"
    elif int(id) == 2:
        return "two"
    elif int(id) == 3:
        return "three"
    else:
        return None

@app.route('/', branch=True)
def root(request):
    f = File("./src/ui/build/index.html")
    f.isLeaf = True
    return f

@app.route("/api/relay/<id>", methods=['PUT', 'GET'])
def toggle(request, id):
    id_str = number_to_word(id)
    if id_str:
        if request.method == 'PUT':
            automationhat.relay[id_str].toggle()
        return json.dumps({"value":automationhat.relay[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/output/<id>", methods=['PUT', 'GET'])
def toggleOutput(request, id):
    id_str = number_to_word(id)
    if id_str:
        if request.method == 'PUT':
            automationhat.output[id_str].toggle()
        return json.dumps({"value": automationhat.output[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/analog/<id>", methods=['GET'])
def readAnalog(request, id):
    id_str = number_to_word(id)
    if id_str:
        return json.dumps({"value": automationhat.analog[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/input/<id>", methods=['GET'])
def readInput(request, id):
    id_str = number_to_word(id)
    if id_str:
        return json.dumps({"value": automationhat.input[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/settings")
def settings(request):
    return json.dumps(defaults())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
