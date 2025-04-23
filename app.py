from flask import Flask, request, jsonify
from flask_cors import CORS
from synthax_cli import run_synthax_code
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

@app.route("/", methods=["GET"])
def index():
    return "✅ Synthax backend is running! Try POST /generate"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    input_text = data.get("input", "")  # or use "code" depending on frontend
    result = run_synthax_code(input_text)
    return jsonify({"output": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render-injected port
    app.run(host="0.0.0.0", port=port)
