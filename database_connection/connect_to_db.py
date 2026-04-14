import mysql.connector

try:
    # Establish a connection to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password"
    )

    print("Successfully connected to MySQL database!")

    # Close the connection
    connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")

