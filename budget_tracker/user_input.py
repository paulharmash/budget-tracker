import datetime

def user_input():
    date = date_input()
    category = category_input()
    sum = sum_input()
    currency = currency_input()
    print(f"User's input: {date}, {category}, {sum}, {currency}")
    #TODO - Write data to the table

def date_input():
    t = datetime.datetime.now()
    while True:
        result = input(f"Date: [{t.strftime('%d')}/{t.strftime('%m')}/{t.strftime('%Y')}] OR enter your date: ")
        if result == "":
            return (f"{t.strftime('%d')}/{t.strftime('%m')}/{t.strftime('%Y')}")
        else:
            try:
                valid_date = validate_date(result)
                return valid_date
            except:
                print("Incorrect data format, should be DD/MM/YYYY")

def category_input():
    pass

def sum_input():
    pass

def currency_input():
    pass

def validate_date(date):
    format = "%d/%m/%Y"
    valid_date = datetime.datetime.strptime(date, format)
    return (f"{valid_date.strftime('%d')}/{valid_date.strftime('%m')}/{valid_date.strftime('%Y')}")