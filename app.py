from flask import Flask, request, jsonify
from synthax_cli import run_synthax_code
import os

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    input_text = data.get("input", "")
    result = run_synthax_code(input_text)
    return jsonify({"output": result})

# 👇 Add this at the bottom to bind correctly on Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses dynamic ports
    app.run(host="0.0.0.0", port=port)
