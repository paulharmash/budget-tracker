# Budget Tracker

A CLI tool for tracking personal income and expenses across multiple currencies (USD, EUR, UAH, CZK). Data is stored locally in CSV format.
Data is also converted to USD based on the currency exchange rate on the date provided by the user. 

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/paulharmash/budget-tracker.git
   cd budget-tracker
   ```

2. Create and activate a virtual environment:
   ```
   python3 -m venv venv && source venv/bin/activate
   ```

3. Install the package:
   ```
   pip install -e .
   ```

4. Run the app:
   ```
   budget-tracker
   ```