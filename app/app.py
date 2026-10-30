import os
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "local-demo-only-change-me")
    metrics = PrometheusMetrics(app, path="/metrics")
    metrics.info("app_info", "CloudOps demo API", version="1.0.0")

    @app.get("/")
    def index():
        return jsonify(
            name="CloudOps DevOps Platform",
            status="running",
            endpoints=["/healthz", "/metrics", "/api/info"],
        )

    @app.get("/healthz")
    def health():
        return jsonify(status="healthy"), 200

    @app.get("/api/info")
    def info():
        return jsonify(service="cloudops-api", version="1.0.0"), 200

    @app.errorhandler(404)
    def not_found(_error):
        return jsonify(error="not found"), 404

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
