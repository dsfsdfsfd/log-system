import os
from pathlib import Path
from dotenv import load_dotenv

# Get the project root directory (2 levels up from this file)
PROJECT_ROOT = Path(__file__).parents[2]

# Load environment variables from .env file
dotenv_path = PROJECT_ROOT / '.env'
load_dotenv(dotenv_path)

# Configuration with defaults
class Config:
    # Log file URL
    LOG_URL = os.getenv('LOG_URL')
    
    # Data directory for storing log files
    DATA_DIR = os.getenv('DATA_DIR', 'data')
    
    # Absolute path to the data directory
    DATA_PATH = PROJECT_ROOT / DATA_DIR
    
    # Other configuration options can be added here
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    