# 🕵️‍♂️ Fake Job Detection — End-to-End MLOps Project

**DVC • MLflow • FastAPI • Docker • GitHub Actions • AWS EC2**

This project demonstrates a complete end-to-end MLOps workflow for detecting fake job postings. It covers data ingestion, preprocessing, model training, evaluation, model registry, tracking, deployment, containerization, automated CI/CD, and production-grade best practices.

---

## 🚀 Project Overview

The objective is to build a machine learning system that classifies job postings as **real** or **fake**, and deploy it in a scalable, reproducible production environment.

### This project includes:

- **Data Pipeline Orchestration** using DVC
- **Experiment Tracking & Model Registry** using MLflow
- **Modular ML Pipeline** (Ingestion → Processing → Training → Registry)
- **Model Serving** using FastAPI
- **Containerization** with Docker
- **Deployment** on AWS EC2
- **Automated Testing & CI/CD** using GitHub Actions
- **Streamlit UI** for interactive inference

---

## 🧠 Problem Statement

Fake job postings lead to:

- financial loss
- identity theft
- misuse of personal data
- wasted time and resources

This project uses machine learning to automatically identify fraudulent job postings.

---

## 📘 Dataset Description

Dataset used:  
**Real or Fake Job Posting Prediction**  
https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction

The dataset contains **18 columns**, including job metadata, descriptions, requirements, and a binary label indicating whether a posting is fake or real.

### Columns Overview

| Column Name           | Description                                     |
| --------------------- | ----------------------------------------------- |
| `job_id`              | Unique identifier for each job posting          |
| `title`               | Job title                                       |
| `location`            | Geographical location                           |
| `department`          | Department within the company                   |
| `salary_range`        | Salary range mentioned                          |
| `company_profile`     | Company background                              |
| `description`         | Detailed job description                        |
| `requirements`        | Required skills and qualifications              |
| `benefits`            | Benefits provided                               |
| `telecommuting`       | Remote job indicator (1 = Yes, 0 = No)          |
| `has_company_logo`    | Whether the posting includes a company logo     |
| `has_questions`       | Whether application questions are included      |
| `employment_type`     | Type of employment (Full-time, Part-time, etc.) |
| `required_experience` | Required experience level                       |
| `required_education`  | Minimum required education                      |
| `industry`            | Industry type                                   |
| `function`            | Job function/category                           |
| `fraudulent`          | **Target variable** (1 = Fake, 0 = Real)        |

There are around 18,000 records, out of which only **800** are fraudulent — indicating strong class imbalance.

---

## 🤖 Model Development

### Data Processing

- Data cleaning
- Handling missing values
- Text lemmatization using **spaCy**
- Vectorization using **Bag of Words**

### Model

- **LightGBM Classifier** with class weights for imbalance
- Hyperparameter tuning using **Optuna**
- Metric optimized: **F1-score**

**Final Test F1-score:** `0.92`

---

## ⚙️ MLOps Implementation

### 1. DVC — Data & Pipeline Versioning

- Orchestrates the ML pipeline
- Handles dataset versioning
- Automatically triggers the ML pipeline on each git push when data changes

### 2. MLflow — Experiment Tracking & Model Registry

- Tracks hyperparameter tuning and model performance
- Stores model artifacts
- Maintains a centralized **model registry**
- FastAPI loads models directly from the registry

### 3. Docker — Containerization

- FastAPI service is containerized
- Image pushed to **Amazon ECR**
- EC2 instance pulls and runs the container
- Ensures consistent execution environment

### 4. GitHub Actions — CI/CD Automation

- **CI:** Runs pytest for API endpoint testing, executes DVC pipeline
- **CD:** Builds and pushes Docker image, deploys updated container on EC2

---

## 🎨 Streamlit Interface

The user interface is deployed on Streamlit Cloud:

👉 **Live App:** https://fake-job-detection-app.streamlit.app/

---

## 🔗 Useful Links

- **LinkedIn:** https://www.linkedin.com/in/rishabh-pancholi-9a31b9191/
- **Dagshub Repository:** https://dagshub.com/rishabhpancholi/fake-job-detection-mlops-project

---
