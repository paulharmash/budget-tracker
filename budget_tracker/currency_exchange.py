import requests
from budget_tracker.constants import BASELINE

def currency_exchange(date, amount, currency):
    converted_date_list = date.split("/")
    converted_date = f"{converted_date_list[2]}-{converted_date_list[1]}-{converted_date_list[0]}"

    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{converted_date}/v1/currencies/{BASELINE.lower()}.json"
    try:
        rates_obj = requests.get(url, timeout=1, verify=True)
        rates_obj.raise_for_status()
    except (requests.exceptions.RequestException):
        return None
    
    rates_json = rates_obj.json()
    conversion_rate = rates_json[BASELINE.lower()][currency.lower()] 
    converted_sum = round((float(amount) / conversion_rate), 2)

    return str(converted_sum)

if __name__ == "__main__":
    currency_exchange("17/03/2026", "100", "USD")