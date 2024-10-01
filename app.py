import psutil
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    message = None
    if cpu_metric > 80 or mem_metric > 80:
        message = "High CPU or Memory Detected, scale up!!!"
    return jsonify(cpu_metric=cpu_metric, mem_metric=mem_metric, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
