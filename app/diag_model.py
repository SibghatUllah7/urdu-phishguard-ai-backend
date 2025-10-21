# diag_model.py
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import os, json

MODEL_DIR = os.environ.get("URDU_PHISH_MODEL_PATH", "./model")

print("MODEL DIR:", MODEL_DIR)
# load model + tokenizer directly (no Trainer)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
print("\nModel config id2label:")
print(json.dumps(model.config.id2label, indent=2))

# create pipeline
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)

test_messages = [
    "Apka bank account block ho gaya hai, abhi verify karein",    # phishing-like
    "Meeting at SID Labs tomorrow at 10am",                       # safe-like
    "Congratulations! You won free balance — click here",         # phishing-like
    "Class canceled today",                                       # safe-like
    "Please visit http://uet.edu for registration",               # safe-with-link maybe
    "Urgent: verify your easypaisa account now",                  # phishing-like
]

print("\nRunning tests:")
for msg in test_messages:
    res = pipe(msg)[0]
    print("MSG:", msg)
    print("  raw result:", res)
    print("  score: {:.4f}".format(float(res.get("score", 0.0))))
    print("  model_label:", res.get("label"))
    print("  ---")
