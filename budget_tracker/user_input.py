import datetime
import questionary

from budget_tracker.constants import CATEGORIES, TYPE

def user_input():
    date = date_input()
    type = income_expences_choice()
    category = category_input()
    amount = amount_input()
    currency = currency_input()
    print(f"User's input: {date}, {type}, {category}, {amount}, {currency}")
    #TODO - Write data to the table
    #Note - I'm passing strings here, might want to change to something else later

def date_input():
    t = datetime.datetime.now()
    while True:
        result = input(f"Date: [{t.strftime('%d')}/{t.strftime('%m')}/{t.strftime('%Y')}] or enter custom date: ")
        if result == "":
            return (f"{t.strftime('%d')}/{t.strftime('%m')}/{t.strftime('%Y')}")
        else:
            try:
                valid_date = validate_date(result)
                return valid_date
            except:
                print("Incorrect data format, should be DD/MM/YYYY")

def income_expences_choice():
    return questionary.select("Pick the category",
                       choices=TYPE).ask()                

def category_input():
    return questionary.select("Pick the category",
                       choices=CATEGORIES).ask()

def amount_input():
    return questionary.text("Enter the amount",
                            validate=lambda entry: True if entry.isdigit() else "Please enter an integer"
                            ).ask()

def currency_input():
    pass

def validate_date(date):
    format = "%d/%m/%Y"
    valid_date = datetime.datetime.strptime(date, format)
    return (f"{valid_date.strftime('%d')}/{valid_date.strftime('%m')}/{valid_date.strftime('%Y')}")