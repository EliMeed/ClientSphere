import psycopg  # Import psycopg

# Establish connection to the PostgreSQL database
dataBase = psycopg.connect(
    host="localhost",
    user="postgres",
    password="123",
    port="5432",
    autocommit=True
)

# Create a cursor object using the connection
cur = dataBase.cursor()

# Execute the SQL command to create a database
cur.execute("CREATE DATABASE elederco;")

# Close the cursor and the connection
cur.close()
dataBase.close()

print("Database created successfully")
