# Mobile Security Risk Assessment Showcase

## Overview

This project demonstrates a lightweight security analysis pipeline for mobile devices using machine learning and a local Large Language Model (LLM).

Rather than making security decisions with an LLM, the application uses an Isolation Forest model to detect anomalous device configurations. The LLM is only intended to explain non-critical findings and recommend security improvements.

The application uses mocked mobile SDK data and runs entirely from the command line.

---

## Architecture

```
Mock Device
      │
      ▼
Feature Encoding
      │
      ▼
Isolation Forest
      │
      ▼
Risk Assessment
      │
      ├── Critical
      │      │
      │      └── No LLM recommendation
      │
      └── Low / Medium
             │
             ▼
       Local LLM (next phase)
             │
             ▼
      Security Recommendations
```

---

## Project Structure

```
mobile-security-showcase/

app.py
detector.py
mock_devices.py
train.py
requirements.txt
model.pkl
README.md
```

---

## Device Features

Each mocked device contains the following information:

- Android OS version
- Network type
- VPN enabled
- Developer mode
- Root access
- Bootloader status
- Screen lock
- Google Play Protect
- USB debugging
- Unknown sources enabled

---

## Machine Learning

The anomaly detector is built using scikit-learn's Isolation Forest.

Synthetic normal devices are generated during training and used to establish a baseline of expected device configurations.

Incoming devices receive:

- anomaly score
- risk classification
- recommendation eligibility

The model is responsible for deciding whether a device should be considered abnormal.

---

## Running

Install dependencies.

```
pip install -r requirements.txt
```

Train the model.

```
python train.py
```

Run the application.

```
python app.py
```

---

## Current Status

Implemented

- Mock mobile SDK
- Synthetic training data
- Isolation Forest training
- Feature encoding
- CLI output
- Risk classification

Planned

- Local LLM integration
- Security recommendation generation
- Prompt engineering
- Recommendation guardrails

---

## Technologies

- Python
- scikit-learn
- NumPy
- Joblib

The project intentionally avoids unnecessary infrastructure such as databases, web frameworks, or cloud services to keep the focus on the machine learning inference pipeline.