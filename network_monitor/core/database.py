import sqlite3
from datetime import datetime

class SQLDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS active_hosts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            host TEXT,
            hostname TEXT,
            port INTEGER,
            proto TEXT,
            service TEXT,
            state TEXT,
            timestamp TEXT
            )
        ''')
        self.conn.commit()
    
    def fill_db(self, host=None, hostname=None, port=None, proto=None, service=None, state=None):
        if isinstance(service, dict):
            service = service.get("name", "")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('''
            INSERT INTO active_hosts (host, hostname, port, proto, service, state, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (host, hostname, port, proto, service, state, timestamp))
        self.conn.commit()

    def close(self):
        self.conn.close()

