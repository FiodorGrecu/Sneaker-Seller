import sqlite3
import os

class Listing:

    tablename = "listings"
    dbpath = ""

    def __init__(self, pk, **kwargs):
        self.pk = kwargs.get("pk")
        self.sneaker = kwargs.get("sneaker", "")
        self.year_released = kwargs.get("year_released", 0)
        self.version_number = kwargs.get("version_number", "")
        self.sports_personality = kwargs.get("sports_personality", "")
        self.original_price = kwargs.get("original_price", 0.0)
        self.current_price = kwargs.get("current_price", 0.0)
        self.manufacturer = kwargs.get("manufacturer", "")
        self.phone = kwargs.get("phone", 0)
        self.email = kwargs.get("email", "")


    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename} (
                    sneaker, year_released, version_number, sports_personality,
                    original_price, current_price, manufacturer, phone, email
                    ) VALUES (?,?,?,?,?,?,?,?,?):"""
            values = (self.sneaker, self.year_released, self.version_number, 
                    self.sports_personality, self.original_price, self.current_price,
                    self.manufacturer, self.phone, self.email)
            cursor.execute(sql, values)
            return True
        return False
