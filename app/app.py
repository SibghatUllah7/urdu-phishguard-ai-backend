from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__, template_folder="templates")

# Load model from local path
MODEL_DIR = os.environ.get("URDU_PHISH_MODEL_PATH", "./model")
nlp = None

def get_pipeline():
    global nlp
    if nlp is None:
        print("🔁 Loading model from:", MODEL_DIR)
        nlp = pipeline("text-classification", model=MODEL_DIR, tokenizer=MODEL_DIR)
    return nlp

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")  # ✅ Make sure this file exists under templates/

@app.route("/predict", methods=["POST"])
def predict():
    data = None
    if request.is_json:
        data = request.json.get("message")
    else:
        data = request.form.get("message")

    if not data:
        return jsonify({"error": "No message provided"}), 400

    pipe = get_pipeline()
    result = pipe(data)[0]
    label = "PHISHING" if result["label"] == "LABEL_1" else "SAFE"

    return jsonify({"label": label, "confidence": float(result["score"])})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
