import datetime
import questionary
import csv

from budget_tracker.constants import *
from budget_tracker.files_manager import create_file

def user_input():

    path = create_file(DATA_FOLDER, TABLE_NAME)
    row = []

    row.append(date_input())
    row.append(income_expences_choice())
    row.append(category_input())
    row.append(amount_input())
    row.append(currency_input())

    # Call here currency exchange function and append to the row too
    # row.append(currency_exchange(row[0], row[3], row[4]))
    # row.append(BASELINE)
    
    write_row(row, path)
    
def write_row(row, path):
    with open(path, "a") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row)

def date_input():
    t = datetime.datetime.now()
    return questionary.text("Press ENTER to chose today or enter the date in format DD/MM/YYYY", 
                            default=date_formatter(t), 
                            validate=validation).ask()
    
def income_expences_choice():
    return questionary.select("Pick the type",
                       choices=CASH_FLOW_TYPE).ask()                

def category_input():
    return questionary.select("Pick the category",
                       choices=CATEGORIES).ask()

def amount_input():
    return questionary.text("Enter the amount",
                            validate=lambda entry: True if entry.isdigit() else "Please enter an integer"
                            ).ask()

def currency_input():
    return questionary.select("Pick the currency",
                       choices=CURRENCIES).ask()
    
def validation(entry):
    try:
        datetime.datetime.strptime(entry, "%d/%m/%Y")
        return True
    except ValueError:
        return "Please enter the date in format DD/MM/YYYY"
    
def date_formatter(date):
    return f"{date.strftime('%d')}/{date.strftime('%m')}/{date.strftime('%Y')}"
