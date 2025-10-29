# General Imports
from fastapi import APIRouter

home_router = APIRouter()

# Home Route
@home_router.get("/",tags=["Home"])
def home()->dict:
    """Returns a welcome message"""
    return {"message":"Welcome to the Real Fake Job Detection API"}

@home_router.get("/health",tags=["Health"])
def health()->dict:
    """Returns a health check message"""
    return {"message":"Health check OK"}