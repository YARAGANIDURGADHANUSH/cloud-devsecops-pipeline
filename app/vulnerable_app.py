from flask import Flask, jsonify
import os

app = Flask(__name__)

# 🚨 SECURITY COMPROMISE: Simulated Hardcoded Cloud Secrets
# This matches regex signatures for static credential leak detection.
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevSecOps Pipeline Dashboard</title>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0b1220;
                color: #ffffff;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            .card {
                background: #111a2e;
                width: 720px;
                max-width: 92%;
                padding: 34px;
                border-radius: 18px;
                box-shadow: 0 12px 35px rgba(0,0,0,0.45);
                text-align: center;
                border: 1px solid rgba(255,255,255,0.08);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>⚠️ Vulnerable Pipeline Audit Simulation Active</h1>
            <p>This deployment is currently configured to test vulnerability thresholds.</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "vulnerable_audit_active"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)