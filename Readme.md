# Online Recruitment Fraud Detection using Deep Learning

An intelligent AI-based system designed to detect fraudulent job postings on online recruitment platforms. This project uses BERT, RoBERTa, SMOBD-SMOTE, and CNN2D to analyze job descriptions and classify them as genuine or fraudulent, helping protect job seekers from scams.

---

## Project Structure

```
Online-Recruitment-Fraud-Detection/
│
├── app.py                     # Main Flask application
├── FraudJobDetection.ipynb    # Model training & experimentation
├── FraudJobDetection.html     # Exported notebook
├── DatasetLink.txt            # Dataset reference links
├── signup.db                  # SQLite database
├── testData.xlsx              # Sample test data
├── .gitignore                 # Git ignored files
│
├── Dataset/                   # Training datasets
├── model/                     # Saved trained models
├── static/                    # CSS, JS, UI assets
├── templates/                 # HTML files (frontend)
│
└── README.md                  # Project documentation
```

---

## Prerequisites

Make sure the following are installed:

| Requirement | Version | Download           |
| ----------- | ------- | ------------------ |
| Python      | 3.8+    | https://python.org |
| pip         | Latest  | Comes with Python  |

---

## Step-by-Step Setup & Execution

### Step 1 — Clone or Download the Project

```bash
git clone <your-repo-link>
cd Online-Recruitment-Fraud-Detection
```

Or download the ZIP file and extract it.

---

### Step 2 — Install Required Libraries

Run the following command:

```bash
pip install flask pandas numpy scikit-learn tensorflow transformers openpyxl
```

---

### Step 3 — Prepare Dataset

* Place datasets inside the Dataset/ folder
* Refer to dataset links from DatasetLink.txt
* Ensure data is properly formatted (CSV/Excel)

---

### Step 4 — Train the Model (Optional)

If you want to retrain the model:

1. Open:

```
FraudJobDetection.ipynb
```

2. Run all cells step by step
3. Save the trained model inside the model/ folder

If a trained model is already available, this step can be skipped.

---

### Step 5 — Run the Application

```bash
python app.py
```

---

### Step 6 — Open in Browser

```
http://127.0.0.1:5000/
```

---

## How to Use the System

### User Side

1. Open the application in browser
2. Register using the signup form
3. Login with your credentials
4. Enter or upload job posting data
5. Click Predict
6. View result:

   * Genuine Job
   * Fraudulent Job

---

### Testing with Sample Data

* Use testData.xlsx for testing
* Upload it through the UI or input manually

---

## Features Overview

| Feature            | Description                             |
| ------------------ | --------------------------------------- |
| Fraud Detection    | Classifies job postings as fake or real |
| Transformer Models | Uses BERT & RoBERTa for NLP             |
| Data Balancing     | SMOBD-SMOTE improves minority detection |
| Feature Extraction | CNN2D enhances performance              |
| Web Interface      | Flask-based simple UI                   |
| High Accuracy      | Achieves ~98.7% accuracy                |

---

## Models Used

* BERT (Baseline)
* RoBERTa
* BERT + SMOBD-SMOTE
* RoBERTa + SMOBD-SMOTE
* BERT + SMOBD-SMOTE + CNN2D (Final Model)

---

## Dependencies Summary

```
flask
pandas
numpy
scikit-learn
tensorflow
transformers
openpyxl
```

---

## Common Errors & Fixes

### ModuleNotFoundError

Install missing module:

```bash
pip install <module-name>
```

---

### Model Not Loading

Ensure model file exists inside model/ folder
Check correct file path in app.py

---

### App Not Opening

Make sure Flask is installed
Check if port 5000 is free

---

### Prediction Not Working

Ensure input format is correct
Check if model is properly loaded

---
