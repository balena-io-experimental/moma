from flask import Flask, jsonify
import automationhat
from settings import defaults

app = Flask(__name__, static_url_path='')

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


@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/api/relay/<id>", methods=['PUT', 'GET'])
def toggle(id):
    id_str = number_to_word(id)
    if id_str:
        automationhat.relay[id_str].toggle()
        return jsonify(active=automationhat.relay[id_str].read())
    else:
        return jsonify(result={"status": 500})

@app.route("/api/analog/<id>", methods=['GET'])
def readAnalog(id):
    id_str = number_to_word(id)
    if id_str:
        return jsonify(value=automationhat.analog[id_str].read())
    else:
        return jsonify(result={"status": 500})

@app.route("/api/input/<id>", methods=['GET'])
def readInput(id):
    id_str = number_to_word(id)
    if id_str:
        return jsonify(value=automationhat.input[id_str].read())
    else:
        return jsonify(result={"status": 500})

@app.route("/api/settings")
def settings():
    return jsonify(defaults())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)