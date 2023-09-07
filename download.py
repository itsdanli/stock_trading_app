import yfinance

df = yfinance.download('AAPL', start='2023-01-01', end='2023-08-20')
df.to_csv('AAPL.csv')