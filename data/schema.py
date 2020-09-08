import sqlite3
import os

'''
pk INTEGER
sneaker VARCHAR
year_released INTEGER
version_number VARCHAR
sports_personality VARCHAR
original_price FLOAT
current_price FLOAT
manufacturer VARCHAR
phone INTEGER 
email VARCHAR
'''


PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, "listings.db")
print(DATAPATH)

def schema(dbpath=DATAPATH):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()

        sql = """CREATE TABLE IF NOT EXISTS listings (
                pk INTEGER,
                sneaker VARCHAR,
                year_released INTEGER,
                version_number VARCHAR,
                sports_personality VARCHAR,
                original_price FLOAT,
                current_price FLOAT,
                manufacturer VARCHAR,
                phone INTEGER,
                email VARCHAR
            );"""

        cursor.execute(sql)
if __name__ == "__main__":
    schema()
