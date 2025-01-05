from flask import Flask, request, jsonify
from prometheus_client import Counter, Histogram, generate_latest
import logging

app = Flask(__name__)

# Prometheus counters and histograms
REQUEST_COUNT = Counter("request_count", "Total Request Count", ["method", "endpoint", "status_code"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request Latency", ["method", "endpoint"])

# Logging setup
logging.basicConfig(level=logging.INFO)

@app.route("/")
def hello_world():
    with REQUEST_LATENCY.labels(method="GET", endpoint="/").time():
        REQUEST_COUNT.labels(method="GET", endpoint="/", status_code=200).inc()
        app.logger.info("Hello, World! endpoint hit.")
        return "Hello, World!"

@app.route("/login", methods=["POST"])
def login():
    with REQUEST_LATENCY.labels(method="POST", endpoint="/login").time():
        data = request.get_json()
        if not data:
            REQUEST_COUNT.labels(method="POST", endpoint="/login", status_code=400).inc()
            app.logger.warning("Invalid request, no JSON data.")
            return jsonify({"error": "Invalid request. JSON data is required."}), 400

        username = data.get("username")
        password = data.get("password")
        if username == "test_user" and password == "secure_password":
            REQUEST_COUNT.labels(method="POST", endpoint="/login", status_code=200).inc()
            app.logger.info(f"Login successful for {username}.")
            return jsonify({"message": "Login successful"}), 200
        else:
            REQUEST_COUNT.labels(method="POST", endpoint="/login", status_code=401).inc()
            app.logger.warning(f"Invalid login attempt for {username}.")
            return jsonify({"error": "Invalid credentials"}), 401

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}

# 404 error handling
@app.errorhandler(404)
def page_not_found(e):
    app.logger.error(f"Page not found: {request.url}")
    return jsonify({"error": "Page not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
