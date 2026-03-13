# Budget tracker requirements

## General description
This CLI tool will allow me to track my income and outcome. It will work through CLI and store data both locally and on Google Drive. 
The app will work with multiple currencies:
- USD (baseline)
- EUR
- UAH
- CZK

### Tracking income
A user will be able to:
- add date
- add income sum
- pick the currency

The entry will be saved in a table that would consist of columns:
- date
- income sum (recalculated in USD)

Income in UAH will be tracked in a separate column for proper tax calculations. 

### Tracking spendings
A user will be able to:
- add date
- add category from a preselected list
- add spending
- pick the currency

The entry will be saved in a table that would consist of columns:
- date
- category
- spending sum (recalculated in USD)

### Analytics
The table will calculate:
- income vs spending ratio per month
- precalculated taxes
- there will be a pivot table of spendings by categories