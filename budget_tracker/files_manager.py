import os
import csv

from pathlib import Path
from budget_tracker.constants import *

# Function to create check if the file exist or create it if not
def create_file(data_folder, table_name):
    # Creating a doc folder if it doesn't exist
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    # Creating a file if it doesn't exist
    full_path = os.path.join(data_folder, table_name)
    if not os.path.exists(full_path):
        Path(full_path).touch()
        # Adding headings
        with open(full_path, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(HEADINGS)
   
    return full_path