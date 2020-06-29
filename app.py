# imports
from flask import Flask, jsonify
from process_utility import Process

# instantiating the Flask class
app = Flask(__name__)

# creating instance of the process utility
util_object = Process()



@app.route('/start_process/<int:process_id>', methods=["POST"])
def start_process(process_id):
    """
    API to start the process based on the process id(PID)
    :return:
    """
    return jsonify(util_object.start(process_id))


@app.route("/terminate_process", methods=["POST"])
def terminate_process():
    """
    API to terminate the running or paused process
    :return:
    """
    return jsonify(util_object.terminate())


@app.route("/pause_process", methods=["POST"])
def pause_process():
    """
    API to pause the running process
    :return:
    """
    return jsonify(util_object.pause())


@app.route("/resume_process/<int:process_id>", methods=["POST"])
def resume_process(process_id):
    """
    API to resume the paused process based on the process id(PID)
    :return:
    """
    return jsonify(util_object.resume(process_id))


if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')