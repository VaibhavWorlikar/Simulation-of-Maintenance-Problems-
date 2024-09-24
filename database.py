import sqlite3

class DatabaseManager:
    def __init__(self, db_name='sim.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS simulation (
                            Year INTEGER PRIMARY KEY,
                            Maintenance_Cost REAL,
                            Resale_value REAL,
                            Running_Cost REAL,
                            Total_operation_cost REAL,
                            Average_annual_cost REAL,
                            Maintenance_Type TEXT
                        )''')
        self.conn.commit()

    def insert_record(self, year, maintenance_cost, resale_value, running_cost, total_operation_cost, average_annual_cost, maintenance_type):
        self.cursor.execute('''INSERT INTO simulation (Year, Maintenance_Cost, Resale_value, Running_Cost, Total_operation_cost, Average_annual_cost, Maintenance_Type)
                            VALUES (?, ?, ?, ?, ?, ?, ?)''',
                            (year, maintenance_cost, resale_value, running_cost, total_operation_cost, average_annual_cost, maintenance_type))
        self.conn.commit()

    def close(self):
        self.conn.close()
