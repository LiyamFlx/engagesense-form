from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    """
    Health check endpoint to confirm API is running.
    """
    return jsonify({"message": "EngageSense API is running!"})

@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Analyze uploaded file content and return engagement metrics.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if not file.filename:
        return jsonify({"error": "Invalid file: No filename provided"}), 400

    try:
        # Read file content
        file_content = file.read().decode("utf-8")

        # Example analysis: Count words and characters
        word_count = len(file_content.split())
        char_count = len(file_content)

        # Placeholder for advanced analysis
        analysis = {
            "emotional": 75,  # Replace with real analysis logic
            "mental": 65,     # Replace with real analysis logic
            "physical": 85,   # Replace with real analysis logic
            "spiritual": 55,  # Replace with real analysis logic
            "word_count": word_count,
            "char_count": char_count,
        }

        return jsonify({"success": True, "analysis": analysis}), 200

    except UnicodeDecodeError:
        return jsonify({"error": "Invalid file encoding. Ensure the file is UTF-8 encoded."}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
