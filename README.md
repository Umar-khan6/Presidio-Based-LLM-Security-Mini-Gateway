# 🔐 Presidio-Based LLM Security Mini-Gateway

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Security](https://img.shields.io/badge/Focus-LLM%20Security-red)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Overview
This project implements a mini security gateway for Large Language Models (LLMs) to protect against:
- Prompt Injection Attacks
- Jailbreak Attempts
- Sensitive Data Leakage

## 🚀 Installation
```bash
git clone https://github.com/Umar-khan6/Presidio-Based-LLM-Security-Mini-Gateway.git
cd Presidio-Based-LLM-Security-Mini-Gateway
pip install -r requirements.txt
python gateway.py
```
## 📂 Project Structure
```bash
Presidio-Based-LLM-Security-Mini-Gateway/
│── README.md              # Project documentation
│── app.py                 # Flask web application (UI interface)
│── config.py              # Configuration settings (thresholds, constants)
│── injection_detector.py  # Detects prompt injection & jailbreak attempts
│── policy_engine.py       # Decision logic (Allow / Mask / Block)
│── presidio_module.py     # Presidio integration & custom PII recognizers
│── requirements.txt       # Project dependencies
```

## 🧠 Pipeline
User Input → Injection Detection → Presidio → Policy Engine → Output

## 📊 Features
- Prompt Injection Detection
- PII Masking (Presidio)
- Policy Engine (Allow/Mask/Block)

