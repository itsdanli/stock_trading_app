import sqlite3
import alpaca_trade_api as tradeapi
import config

connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("""
               SELECT id, symbol, company FROM stock""")
rows = cursor.fetchall()
api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL)

symbols = [row['symbol'] for row in rows]
stock_dict = {}

for row in rows:

    symbol = row['symbol']
    # symbols.append(symbol)
    stock_dict[symbol] = row['id']
# barsets = api.get_bars('AAPL', tradeapi.TimeFrame.Day, "2023-09-01", "2023-09-01", adjustment='raw').df.reset_index()
# print(barsets.timestamp.dt.date)


chunk_size = 200
for i in range(0, len(symbols), chunk_size):
    symbol_chunk = symbols[i:i+chunk_size]
    barsets = api.get_bars(symbol_chunk, tradeapi.TimeFrame.Day, "2023-09-01", "2023-09-01", adjustment='raw').df.reset_index()
    for symbol in barsets['symbol']:
        line = barsets.loc[barsets['symbol'] == symbol]
        print(stock_dict[symbol], line.timestamp.dt.date, line.open, line.high, line.low, line.close, line.volume)

        '''
        Error with inserting into sqlite database at the moment
        '''
        
        
        cursor.execute("""
                       INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?, ?)
                       """,
                       (stock_dict[symbol], line.timestamp.dt.date, line.open, line.high, line.low, line.close, line.volume))
        
connection.commit()
