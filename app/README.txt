
Urdu Phishing Detector - Flask Web App

Files created in this folder:
- app.py                 : Flask app (loads model and serves / and /predict)
- templates/index.html   : Simple UI to paste Roman Urdu message and get prediction
- requirements.txt       : Python dependencies

How to run locally (Linux)
--------------------------
1. Create a Python virtual environment (recommended):
   python3 -m venv venv
   source venv/bin/activate

2. Install requirements:
   pip install -r requirements.txt

3. Place your trained HuggingFace model folder here (or set URDU_PHISH_MODEL_PATH):
   - Example: copy model to /mnt/data/urdu_phish_webapp/model
   or set env var:
   export URDU_PHISH_MODEL_PATH=/path/to/your/model

4. Run the app:
   python app.py
   Open http://localhost:5000 in your browser.

Notes
-----
- The app expects a folder with the saved HuggingFace model (i.e., contains config.json, pytorch_model.bin, tokenizer files).
- For production, consider containerizing with Docker and adding input validation + rate limiting.
