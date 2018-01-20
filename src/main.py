from flask import Flask, jsonify, request
from flask_apscheduler import APScheduler
from datetime import date, datetime, timedelta
import automationhat
from flask_cors import CORS, cross_origin
import json
from settings import defaults

# Configure periodic jobs here.
class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'main:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 3600
        },
        {
            'id': 'wifi_setup',
            'func': 'main:wifi_setup',
            'args': (1,1),
            'trigger': 'interval',
            'seconds': 10
        }
    ]
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 10}
    }

    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }
    SCHEDULER_API_ENABLED = True

app = Flask(__name__, static_url_path='', static_folder='ui/build')
CORS(app)

val = 0

def job1(a,b):
    print('Tick! The time is: %s' % datetime.now())
    return None

def wifi_setup(a,b):
    print('Checking AP mode selection pin')
    print(automationhat.input.read[2])
    return None

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

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route("/api/relay/<id>", methods=['PUT', 'GET'])
def toggleRelay(id):
    id_str = number_to_word(id)
    if id_str:
        if request.method == 'PUT':
            automationhat.relay[id_str].toggle()
        return json.dumps({"value":automationhat.relay[id_str].read()})
    else:
        return json.dumps({"status": 500})

# URL/api/relay/1/on?time=30
@app.route("/api/relay/<id>/on", methods=['PUT', 'GET'])
def relayOn(id):
    id_str = number_to_word(id)
    delay = int(request.args.get('time', default=-1))
    if id_str:
        automationhat.relay[id_str].write(1)
        if delay > 0:
            # schedule the relay to switch of in <delay> time from now.
            sched_time = datetime.now() + timedelta(seconds=delay)
            job_name = 'relay_'+id_str+'off'
            try:
              scheduler.add_job(id=job_name, func=delayRelaySwitchOff, trigger='date', run_date=sched_time, args=[id_str])
            except:
              return json.dumps({"status": 500}, {"info": "Job already scheduled on this resource"})

        return json.dumps({"value":automationhat.relay[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/relay/<id>/off", methods=['PUT', 'GET'])
def relayOff(id):
    id_str = number_to_word(id)
    if id_str:
        automationhat.relay[id_str].write(0)
        return json.dumps({"value":automationhat.relay[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/output/<id>", methods=['PUT', 'GET'])
def toggleOutput(id):
    id_str = number_to_word(id)
    if id_str:
        if request.method == 'PUT':
            automationhat.output[id_str].toggle()
        return json.dumps({"value": automationhat.output[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/output/<id>/on", methods=['PUT', 'GET'])
def outputOn(id):
    id_str = number_to_word(id)
    delay = int(request.args.get('time', default=-1))
    if id_str:
        automationhat.output[id_str].write(1)
        if delay > 0:
            # schedule the relay to switch of in <delay> time from now.
            sched_time = datetime.now() + timedelta(seconds=delay)
            job_name = 'output_'+id_str+'off'
            try:
              scheduler.add_job(id=job_name, func=delayOutputSwitchOff, trigger='date', run_date=sched_time, args=[id_str])
            except:
              return json.dumps({"status": 500}, {"info": "Job already scheduled on this resource"})

        return json.dumps({"value":automationhat.output[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/output/<id>/off", methods=['PUT', 'GET'])
def outputOff(id):
    id_str = number_to_word(id)
    if id_str:
        automationhat.output[id_str].write(0)
        return json.dumps({"value":automationhat.output[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/analog/<id>", methods=['GET'])
def readAnalog(id):
    id_str = number_to_word(id)
    if id_str:
        return json.dumps({"value": automationhat.analog[id_str].read()})
    else:
        return json.dumps({"status": 500})

@app.route("/api/input/<id>", methods=['GET'])
def readInput(id):
    id_str = number_to_word(id)
    if id_str:
        return json.dumps({"value": automationhat.input[id_str].read()})
    else:
        return json.dumps({"status": 500})

# TODO: find a better way to return the state, using settings.py
@app.route("/api/state", methods=['GET'])
def getState():
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
def settings():
    return json.dumps(defaults())

if __name__ == "__main__":
  app.config.from_object(Config())

  scheduler = APScheduler()

  scheduler.init_app(app)
  scheduler.start()
  app.run(host='0.0.0.0', port=80)
