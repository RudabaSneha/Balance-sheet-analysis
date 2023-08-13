import requests 
import matplotlib.pyplot as plt

api_key = '07530e619734c86aa889adf3204f2b0f'

company = 'AAPL'
years = 2

balance_sheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit={years}&apikey={api_key}')
balance_sheet = balance_sheet.json()


#print(balance_sheet[0].keys())
#most recent value
total_current_assets = balance_sheet[0]['totalCurrentAssets']
print(f"Total Current Assets of {company}: {total_current_assets:,}")
total_current_liabilities = balance_sheet[0]['totalCurrentLiabilities']
print(f"Total Current liabilities of {company}: {total_current_liabilities:,}")
current_stockholder_equity = total_current_assets - total_current_liabilities
print(f'current stockholder equity: {current_stockholder_equity:,}')

total_debt = balance_sheet[0]['totalDebt']
cash_and_equivalents = balance_sheet[0]['cashAndCashEquivalents']
cash_debt_difference = cash_and_equivalents - total_debt
print(f'cash: {cash_and_equivalents:,}')
print(f'cash debt difference is {cash_debt_difference:,}')

goodwill_and_intangibles = balance_sheet[0]['goodwillAndIntangibleAssets']
total_assets = balance_sheet[0]['totalAssets']
pct_intangible = goodwill_and_intangibles/ total_assets

#format to 2 decimal places
print(f'Percentage intangibles:{pct_intangible * 100: .2f}')

Stockholder_equity = balance_sheet[0]['totalStockholdersEquity']
print(f'stockholder equity: {Stockholder_equity:,} for {company}')