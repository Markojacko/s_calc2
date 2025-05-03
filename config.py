import os
from dotenv import load_dotenv

load_dotenv()

# Configuration variables
AWS_AZ = os.getenv("AWS_AZ", "us-east-1a")
AZURE_LOCATION = os.getenv("AZURE_LOCATION", "East US")
GCP_REGION = os.getenv("GCP_REGION", "us-central1")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
