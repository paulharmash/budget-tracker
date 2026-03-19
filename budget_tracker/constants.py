from pathlib import Path

# Table path
DATA_FOLDER = Path.home() / ".budget-tracker"
TABLE_NAME = "table.csv"
# Test table path
TEST_DATA_FOLDER = "./test_data"
TEST_TABLE_NAME = "test_table.csv"

#Table headers
HEADING_DATE = "Date"
HEADING_TYPE = "Cash flow type"
HEADING_CATEGOTY = "Category"
HEADING_AMOUNT = "Amount"
HEADING_CURRENCY = "Currency"
HEADINGS = [HEADING_DATE, HEADING_TYPE, HEADING_CATEGOTY, HEADING_AMOUNT, HEADING_CURRENCY]

# Income/expences
INCOME = "Income"
EXPENCES = "Expences"
CASH_FLOW_TYPE = [EXPENCES, INCOME]

# Currencies
USD = "USD"
EUR = "EUR"
UAH = "UAH"
CZK = "CZK"
BASELINE = "USD"
CURRENCIES = [USD, EUR, UAH, CZK]

# Categories
FOOD = "Food"
EATING_OUT = "Eating out"
HOME_TRIVIA = "Home trivia"
MEDICINES = "Medicines"
TOILETRY = "Toiletry"
SPORT = "Sport"
RENT = "Rent"
BILLS = "Bills"
TRANSPORTATION = "Transportation"
CLOTHES = "Clothes"
HEALTH = "Health"
DENTIST = "Dentist"
PRESENTS = "Presents"
FUN = "Fun"
VACATION = "Vacation"
BOOKS = "Books"
LAWYER_ACCOUNTANT = "Lawyer/Accountant"
GAS = "Gas"
TREE_LEAF = "TreeLeaf"
PHONE = "Phone"
EQUIPMENT = "Equipment"
EDUCATION = "Education"
TAXES_INSURANCE = "Taxes/insurance"
NETFLIX = "Netflix"
YOUTUBE = "YouTube"
OSVC = "OSVC"
CLAUDE = "Claude"
CATEGORIES = [FOOD, EATING_OUT, HOME_TRIVIA, MEDICINES, TOILETRY, SPORT, RENT, BILLS, TRANSPORTATION, CLOTHES, HEALTH, DENTIST, PRESENTS, FUN, VACATION, BOOKS, LAWYER_ACCOUNTANT, GAS, TREE_LEAF, PHONE, EQUIPMENT, EDUCATION, TAXES_INSURANCE, NETFLIX, YOUTUBE, OSVC, CLAUDE]