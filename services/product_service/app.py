from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest
import time, random, os

app = Flask(__name__)
REQ = Counter("http_requests_total", "Total HTTP requests", ["endpoint"])

@app.get("/")
def root():
    REQ.labels(endpoint="/").inc()
    time.sleep(random.uniform(0,0.05))
    return jsonify(service="product_service", status="ok")

@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type":"text/plain; version=0.0.4"}

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
