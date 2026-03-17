import datetime
import questionary

from budget_tracker.constants import CATEGORIES, CASH_FLOW_TYPE, CURRENCIES

def user_input():
    date = date_input()
    cash_flow_type = income_expences_choice()
    category = category_input()
    amount = amount_input()
    currency = currency_input()
    print(f"User's input: {date}, {cash_flow_type}, {category}, {amount}, {currency}")
    #TODO - Write data to the table
    #Note - I'm passing strings here, might want to change to something else later

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