# Platform: Model ------------------------------------------------------------#
from Platform import Platform

import sqlite3

class PlatformModel:
    def __init__(self):
        self.platforms = []
        self.conn = sqlite3.connect('data.db')
        self.create_table()
        self.read_platforms()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS platforms (
                            id INTEGER PRIMARY KEY,
                            short_name TEXT NOT NULL,
                            long_name TEXT NOT NULL,
                            url TEXT NOT NULL)''')
        self.conn.commit()

    def create_platform(self, short_name, long_name, url):
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO platforms (short_name, long_name, url) VALUES (?, ?, ?)',
            (short_name, long_name, url)
        )
        self.conn.commit()
        self.read_platforms()

    def read_platforms(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, short_name, long_name, url FROM platforms')
        self.platforms = [Platform(*row) for row in cursor.fetchall()]

    def update_platform(self, new_platform: Platform, old_platform: Platform):
        cursor = self.conn.cursor()
        cursor.execute(
            'UPDATE platforms SET short_name = ?, long_name = ?, url = ? WHERE id = ?',
            (new_platform.name, new_platform.long_name, new_platform.url, old_platform.id)
        )
        self.conn.commit()
        self.read_platforms()

    def delete_platform(self, short_name):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM platforms WHERE short_name = ?', (short_name,))
        self.conn.commit()
        self.read_platforms()

    def get_platforms(self):
        return self.platforms