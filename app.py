from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "EngageSense API is running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    if not file.filename:
        return jsonify({"error": "Invalid file"}), 400

    # Read file content
    file_content = file.read().decode("utf-8")

    # Example analysis: Count words and characters
    word_count = len(file_content.split())
    char_count = len(file_content)

    # Simulated emotional/mental analysis (placeholder logic)
    analysis = {
        "emotional": 75,
        "mental": 65,
        "physical": 85,
        "spiritual": 55,
        "word_count": word_count,
        "char_count": char_count,
    }

    return jsonify(analysis)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
