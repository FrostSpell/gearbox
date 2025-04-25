PLATFORM_CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS platforms (
id INTEGER PRIMARY KEY,
short_name TEXT NOT NULL,
long_name TEXT NOT NULL,
url TEXT NOT NULL)'''

PLATFORM_CREATE = '''INSERT INTO platforms
(short_name, long_name, url)
VALUES (?, ?, ?)'''

PLATFORM_READ = 'SELECT id, short_name, long_name, url FROM platforms'

PLATFORM_UPDATE = '''UPDATE platforms
SET short_name = ?, long_name = ?, url = ?
WHERE id = ?'''

PLATFORM_DELETE = 'DELETE FROM platforms WHERE id = ?'
