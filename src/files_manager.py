import os
from pathlib import Path
from src.constants import *

# Function to create check if the file exist or create it if not
def create_file():
    # Creating a doc folder if it doesn't exist
    if not os.path.exists(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)

    # Creating a file if it doesn't exist
    full_path = os.path.join(DATA_FOLDER, TABLE_NAME)
    if not os.path.exists(full_path):
        Path(full_path).touch()
    
    return full_path