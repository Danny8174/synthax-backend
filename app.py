from flask import Flask, request, jsonify
from synthax_cli import run_synthax_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    input_text = data.get("input", "")
    result = run_synthax_code(input_text)
    return jsonify({"output": result})

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    input_text = data.get("input", "")
    result = run_synthax_code(input_text)
    return jsonify({"output": result})
