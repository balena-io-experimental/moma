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

def delayRelaySwitchOff(id_str):
    automationhat.relay[id_str].write(0)
    print "switched off relay: "+ id_str

def delayOutputSwitchOff(id_str):
    automationhat.output[id_str].write(0)
    print "switched off output: "+ id_str

@app.route('/', branch=True)
def root(request):
    f = File("./src/ui/build/index.html")
    f.isLeaf = True
    return f

@app.route("/api/relay/<id>", methods=['PUT', 'GET'])
def toggleRelay(request, id):
    id_str = number_to_word(id)
    if id_str:
        if request.method == 'PUT':
            automationhat.relay[id_str].toggle()
        return json.dumps({"value":automationhat.relay[id_str].read()})
    else:
        return json.dumps({"status": 500})

# URL/api/relay/1/on?time=10
@app.route("/api/relay/<id>/on", methods=['PUT', 'GET'])
def relayOn(request, id):
    id_str = number_to_word(id)
    delay = float(request.args.get('time', [-1])[0])
    if id_str:
        automationhat.relay[id_str].write(1)
        if delay > 0:
            reactor.callLater(delay, delayRelaySwitchOff, id_str)
        return json.dumps({"value":automationhat.relay[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/relay/<id>/off", methods=['PUT', 'GET'])
def relayOff(request, id):
    id_str = number_to_word(id)
    if id_str:
        automationhat.relay[id_str].write(0)
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

@app.route("/api/output/<id>/on", methods=['PUT', 'GET'])
def outputOn(request, id):
    id_str = number_to_word(id)
    delay = float(request.args.get('time', [-1])[0])
    if id_str:
        automationhat.output[id_str].write(1)
        if delay > 0:
            reactor.callLater(delay, delayOutputSwitchOff, id_str)
        return json.dumps({"value":automationhat.output[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/output/<id>/off", methods=['PUT', 'GET'])
def outputOff(request, id):
    id_str = number_to_word(id)
    if id_str:
        automationhat.output[id_str].write(0)
        return json.dumps({"value":automationhat.output[id_str].read()})
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

# TODO: find a better way to return the state, using settings.py
@app.route("/api/state", methods=['GET'])
def getState(request):
    input = automationhat.input.read()
    analog = automationhat.analog.read()
    output = automationhat.output.read()
    relay = automationhat.relay.read()
    return json.dumps({"RELAYS": [
      {
        "name": 'relay 1',
        "value": relay["one"]
      },
      {
        "name": 'relay 2',
        "value": relay["two"]
      },
      {
        "name": 'relay 3',
        "value": relay["three"]
      }
    ],
    "OUTPUTS": [
      {
        "name": 'output 1',
        "value": output["one"]
      },
      {
        "name": 'output 2',
        "value": output["two"]
      },
      {
        "name": 'output 3',
        "value": output["three"]
      }
    ],
    "ANALOGS": [
      {
        "name": 'analog 1',
        "value": analog["one"]
      },
      {
        "name": 'analog 2',
        "value": analog["two"]
      },
      {
        "name": 'analog 3',
        "value": analog["three"]
      }
    ],
    "INPUTS": [
      {
        "name": 'input 1',
        "value": input["one"]
      },
      {
        "name": 'input 2',
        "value": input["two"]
      },
      {
        "name": 'input 3',
        "value": input["three"]
      }
    ]
    })

@app.route("/api/settings")
def settings(request):
    return json.dumps(defaults())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
