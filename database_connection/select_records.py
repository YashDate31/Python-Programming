import mysql.connector

try:
    # Establish a connection to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query to select records
    cursor.execute("SELECT * FROM your_table")

    # Fetch all the records
    records = cursor.fetchall()

    # Display the records
    print("Records from the table:")
    for record in records:
        print(record)

    # Close the cursor and connection
    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
