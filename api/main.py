# General Imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Package Imports
from api.routes import home_router,prediction_router
from api.exception import register_exception_handlers

# Initialize FastAPI
app = FastAPI(
    title="Real/Fake Job Detection API",
    description="API for detecting real or fake job postings using NLP and ML models",
)

# Adding Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Exception Handlers
register_exception_handlers(app)

# Include Routers
app.include_router(home_router)
app.include_router(prediction_router)

