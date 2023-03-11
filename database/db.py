import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('users.db')

# Create a cursor
cursor = conn.cursor()

# Execute a SQL command to create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
  username TEXT NOT NULL,
  email TEXT PRIMARY KEY,
  latitude TEXT NOT NULL,
  longitude TEXT NOT NULL,
  printername TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()