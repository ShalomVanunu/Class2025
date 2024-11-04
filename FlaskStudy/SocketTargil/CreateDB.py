import sqlite3

# Create a new SQLite database
conn = sqlite3.connect('credit_db.db')
c = conn.cursor()

# Create the creditnumbers table
c.execute("""CREATE TABLE IF NOT EXISTS creditnumbers
             (name TEXT, creditnum TEXT)""")

# Add default values
c.execute("INSERT INTO creditnumbers (name, creditnum) VALUES (?, ?)", ("shalom", "1234123412341234"))
c.execute("INSERT INTO creditnumbers (name, creditnum) VALUES (?, ?)", ("daniel", "4567456745674567"))

# Save the changes and close the connection
conn.commit()
conn.close()