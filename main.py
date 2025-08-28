from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
hits = Counter("http_hits_total", "Total hits")

@app.route("/")
def hello():
    hits.inc()
    return "ok"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

app.run(host="0.0.0.0", port=9123)
