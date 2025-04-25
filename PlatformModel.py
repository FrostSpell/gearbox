# Platform: Model ------------------------------------------------------------#
from Platform import Platform


import sqlite3

from contants import PLATFORM_CREATE, PLATFORM_CREATE_TABLE, PLATFORM_DELETE, PLATFORM_READ, PLATFORM_UPDATE
class PlatformModel:
    def __init__(self):
        self.platforms = []
        self.conn = sqlite3.connect('data.db')
        self.create_table()
        self.read_platforms()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute(PLATFORM_CREATE_TABLE)
        self.conn.commit()

    def create_platform(self, platform: Platform):
        """Insert a new platform"""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                PLATFORM_CREATE,
                (platform.name, platform.long_name, platform.url)
            )
            self.conn.commit()
        finally:
            cursor.close()
        self.read_platforms()


    def read_platforms(self):
        """Select all platforms"""
        cursor = self.conn.cursor()
        try:
            cursor.execute(PLATFORM_READ)
            self.platforms = [Platform(*row) for row in cursor.fetchall()]
        finally:
            cursor.close()


    def update_platform(self, new_platform: Platform, old_platform: Platform):
        """Update an existing platform"""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                PLATFORM_UPDATE,
                (new_platform.name, new_platform.long_name, new_platform.url, old_platform.id)
            )
            self.conn.commit()
        finally:
            cursor.close()
        self.read_platforms()


    def delete_platform(self, platform: Platform):
        """Delete a platform by short_name"""
        cursor = self.conn.cursor()
        try:
            cursor.execute(PLATFORM_DELETE, (platform.id))
            self.conn.commit()
        finally:
            cursor.close()
        self.read_platforms()


    def get_platforms(self):
        """Return a list of platforms"""
        return self.platforms