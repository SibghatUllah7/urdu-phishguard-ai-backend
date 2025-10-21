<<<<<<< HEAD
# urdu-phishguard-ai-backend[Uploading README.md…]()
# 🇵🇰 Urdu-PhishGuard-AI  
### **AI-Powered Urdu Phishing Message Detector**  
**🔒 Developed Independently Developers by _Sibghat Ullah_ & Zaryab khattak
=======
# 🇵🇰 Urdu-PhishGuard-AI  
### **AI-Powered Urdu Phishing Message Detector**  
**🔒 Developed Independently by _Sibghat Ullah_**
>>>>>>> 6345da9 (Initial commit - Urdu PhishGuard AI backend)

---

## 📌 Overview

Urdu-PhishGuard-AI is a **Multilingual BERT-based phishing detection system** designed to analyze **Urdu and Roman-Urdu messages** and classify them as either:

- ✅ **SAFE** — Normal user communication
- ⚠ **SUSPICIOUS (Needs Review)** — Requires manual inspection
- 🚨 **PHISHING (Malicious Intent)** — High confidence threat

> 🎯 **Built fully from scratch — dataset, training, model tuning, and Flask deployment were done without institutional assistance.**

---

## 🧠 Tech Stack

| Component            | Technology Used                     |
|---------------------|------------------------------------|
| 🔤 Language Model    | `BERT Multilingual (bert-base-multilingual-cased)` |
| 🐍 Backend API       | `Flask (Python)`                   |
| 🎛 Threshold Logic   | Confidence Scoring + Manual Review Flag |
| 🗂 Dataset Format    | CSV → `text`, `label`, `needs_review` |
| 🌐 Deployment Mode   | Web UI + API mode (JSON result)    |
<<<<<<< HEAD
| 🎛 UI Layer          | HTML / JavaScript / AJAX → Flask /react  |
=======
| 🎛 UI Layer          | HTML / JavaScript / AJAX → Flask   |
>>>>>>> 6345da9 (Initial commit - Urdu PhishGuard AI backend)

---

## 🚀 Features

✅ Detects **Urdu + Roman Urdu phishing messages**  
✅ **Hybrid Logic** → AI + Manual Review Threshold  
✅ Web UI + JSON API mode  
✅ Lightweight — works on **CPU**  
✅ Model can be deployed to **HuggingFace / Streamlit / NCCS Demo**

---

## 📁 Folder Structure
Urdu-PhishGuard-AI/
│
├── app/ # Flask Web App (Run app.py)
├── data/ # Training + Extended Dataset
├── model/ # Trained Model (config.json + weights)
├── notebooks/ # Google Colab Training Notebook
├── README.md # You're reading this 🙂
├── LICENSE # MIT License © 2025 – Sibghat Ullah
├── credits.txt # Explicit Author Notice
├── requirements.txt # pip dependencies
└── merge_package.sh # Automation script
