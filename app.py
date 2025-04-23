from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Add this
from synthax_cli import run_synthax_code

app = Flask(__name__)
CORS(app)  # ✅ Add this too

@app.route("/", methods=["GET"])
def index():
    return "✅ Synthax backend is running! Try POST /generate"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    input_text = data.get("input", "")  # or data.get("code", "") if frontend sends { code }
    result = run_synthax_code(input_text)
    return jsonify({"output": result})
