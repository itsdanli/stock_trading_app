

'
 CREATE TABLE IF NOT EXISTS stock (
    id INTEGER PRIMARY KEY,
   symbol TEXT NOT NULL UNIQUE,
   company TEXT NOT NULL
   );
   '
   '
CREATE TABLE IF NOT EXISTS stock_price (
    id INTEGER PRIMARY KEY,
    stock_id INTEGER,
    date NOT NULL,
    open NOT NULL,
    high NOT NULL,
    low NOT NULL,
    close NOT NULL,
    adjusted_close NOT NULL,
    volume NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stock (id)
)

CRUD Operations
CRUD stands for Create, Read, Update, and Delete. These operations are building blocks for web and mobile applications. If you can design user interfaces, create API's and write queries that perform these basic operations you can build your own applications or be employed for your entire career

Inserting into table
 INSERT INTO stock (symbol, company) VALUES ('MSFT', 'Microsoft');

Updating into table
 UPDATE stock set symbol = 'AMDA' WHERE id = 4;