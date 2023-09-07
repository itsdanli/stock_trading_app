import sqlite3
import alpaca_trade_api as tradeapi
import config

connection = sqlite3.connect('app.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("""
               SELECT * FROM stock""")

api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL)
assets = api.list_assets()

rows = cursor.fetchall()
symbols = [row['symbol'] for row in rows]


for asset in assets:
    try:
        if asset.symbol not in symbols and asset.status == 'active' and asset.tradable:
            print(f"Added a new stock {asset.symbol} {asset.name}")
            cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
    except Exception as e:
        print(asset.symbol)
        print(e)
connection.commit()

