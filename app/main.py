from flask import Flask, jsonify

app = Flask(__name__)

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
            h1 {
                margin: 0;
                font-size: 28px;
            }
            .subtitle {
                margin-top: 10px;
                opacity: 0.9;
                font-size: 15px;
                line-height: 1.5;
            }
            .status {
                margin: 18px auto 0;
                display: inline-block;
                padding: 8px 14px;
                border-radius: 999px;
                background: rgba(34,197,94,0.15);
                color: #22c55e;
                font-weight: bold;
                font-size: 14px;
            }
            .buttons {
                margin-top: 22px;
            }
            a.btn {
                display: inline-block;
                margin: 8px;
                padding: 12px 18px;
                background: #1f6feb;
                color: white;
                border-radius: 12px;
                text-decoration: none;
                font-weight: 700;
                transition: 0.2s ease;
            }
            a.btn:hover {
                background: #388bfd;
                transform: translateY(-1px);
            }
            .grid {
                margin-top: 26px;
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 12px;
                text-align: left;
            }
            .box {
                background: rgba(255,255,255,0.04);
                padding: 14px;
                border-radius: 14px;
                border: 1px solid rgba(255,255,255,0.06);
            }
            .box h3 {
                margin: 0 0 6px 0;
                font-size: 14px;
                opacity: 0.95;
            }
            .box p {
                margin: 0;
                font-size: 13px;
                opacity: 0.85;
            }
            .footer {
                margin-top: 20px;
                font-size: 12px;
                opacity: 0.7;
            }
            code {
                background: rgba(255,255,255,0.08);
                padding: 2px 6px;
                border-radius: 6px;
            }

            @media (max-width: 600px) {
                .grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>✅ Cloud-Based Secure DevOps Pipeline</h1>
            <div class="subtitle">
                This service is deployed on <b>AWS EC2</b> using <b>Docker</b>.<br/>
                CI/CD is automated with <b>GitHub Actions</b> and security scanning is done with <b>Trivy</b>.
            </div>

            <div class="status">Status: Running ✅</div>

            <div class="buttons">
                <a class="btn" href="/health">Health Check</a>
                <a class="btn" href="https://github.com/YARAGANIDURGADHANUSH/cloud-devsecops-pipeline" target="_blank">GitHub Repo</a>
                <a class="btn" href="https://hub.docker.com/r/ydurgadhanush/devsecops-pipeline" target="_blank">Docker Hub</a>
            </div>

            <div class="grid">
                <div class="box">
                    <h3>CI Pipeline</h3>
                    <p>Build → Test → Docker Build → Trivy Scan → Artifact Upload</p>
                </div>
                <div class="box">
                    <h3>Security</h3>
                    <p>Image vulnerability scanning with <code>HIGH</code>/<code>CRITICAL</code> checks.</p>
                </div>
                <div class="box">
                    <h3>Deployment</h3>
                    <p>Docker container running on AWS EC2 with port mapping.</p>
                </div>
                <div class="box">
                    <h3>Endpoints</h3>
                    <p><code>/</code> Dashboard • <code>/health</code> Health JSON</p>
                </div>
            </div>

            <div class="footer">
                DevSecOps Demo Project • Built by Durga Dhanush
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

