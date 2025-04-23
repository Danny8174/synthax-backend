from flask import Flask, request, jsonify
import subprocess
import tempfile
import os

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_code():
    code = request.json.get("code", "")
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".synth", delete=False) as tmp:
        tmp.write(code)
        tmp.flush()
        try:
            result = subprocess.run(["python3", "shared/synthax_cli.py", tmp.name], capture_output=True, text=True, timeout=10)
            return jsonify({"output": result.stdout + result.stderr})
        except Exception as e:
            return jsonify({"output": str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))