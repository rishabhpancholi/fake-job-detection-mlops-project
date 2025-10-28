# Base python image
FROM python:3.13

# Setting the working directory inside the container
WORKDIR /api

# Copying the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Downloading the small English SpaCy model
RUN python -m spacy download en_core_web_sm

# Copying the FastAPI app code into the container
COPY api/ ./api/

# Command to run the FastAPI app using uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

