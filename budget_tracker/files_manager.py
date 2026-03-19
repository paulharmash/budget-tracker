import os
import csv

from pathlib import Path
from budget_tracker.constants import *

def create_file(data_folder, table_name):
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    full_path = os.path.join(data_folder, table_name)
    if not os.path.exists(full_path):
        Path(full_path).touch()
        with open(full_path, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(HEADINGS)
   
    return full_path