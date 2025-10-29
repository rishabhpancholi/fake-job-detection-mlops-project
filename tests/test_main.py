# General Imports
import pytest
from fastapi.testclient import TestClient

# Package Imports
from api import app

client = TestClient(app)


def test_health_check():
    """Test the health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Health check OK"}


def test_predict_endpoint():
    """Test the prediction endpoint"""
    # Example payload - modify according to your model input schema
    payload = {
                "salary_range": "Not Mentioned",
                "telecommuting": 0,
                "has_company_logo": 0,
                "has_questions": 0,
                "employment_type": "Full-time",
                "required_experience": "Internship",
                "required_education": "Bachelor's Degree",
                "text": "string"
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200

