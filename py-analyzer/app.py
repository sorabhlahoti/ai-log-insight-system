from flask import Flask, request, jsonify
import redis
import json
from model import model

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/analyze', methods=['GET'])
def analyze():
    logs = [json.loads(log) for log in r.lrange('logs', 0, -1)]
    features = [[float(log.get('metric', 0)), float(log.get('error_rate', 0)), float(log.get('latency', 0))] for log in logs]
    preds = model.predict(features)
    anomalies = [log for log, p in zip(logs, preds) if p == -1]
    return jsonify({'anomalies': anomalies})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
