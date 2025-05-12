import requests
import os
import sys
from pathlib import Path
from log_system.config import Config

# Add the src directory to the Python path
src_path = Path(__file__).parents[4]
sys.path.insert(0, str(src_path))

def download_log_file(url, save_path=None):
    """
    Download log file from the given URL and save it to the specified path.
    
    Args:
        url (str): URL of the log file to download
        save_path (str, optional): Path where the log file should be saved.
                                   If None, uses the filename from the URL.
    
    Returns:
        str: Path to the saved log file
    """
    try:
        # Send GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Extract filename from URL if save_path is not provided
        if save_path is None:
            filename = url.split('/')[-1]
            save_path = os.path.join(Config.DATA_PATH, filename)
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save the file
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Log file successfully downloaded to: {save_path}")
        return save_path
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the log file: {e}")
        return None

if __name__ == "__main__":
    # Get URL from config
    log_url = Config.LOG_URL
    if not log_url:
        print("Error: LOG_URL environment variable not found in .env file")
        exit(1)
        
    filename = log_url.split('/')[-1]
    save_to = os.path.join(Config.DATA_PATH, filename)
    
    download_log_file(log_url, save_to)