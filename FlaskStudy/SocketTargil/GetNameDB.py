import sqlite3


def get_name_by_card_number(card_number):
    # Connect to the SQLite database
    connection = sqlite3.connect('credit_db.db')  # Replace with your database file
    cursor = connection.cursor()

    try:
        # Execute the query to get the name associated with the card number
        cursor.execute("SELECT name FROM creditnumbers WHERE creditnum = ?", (card_number,))

        # Fetch the result
        result = cursor.fetchone()

        # Check if a result was found
        if result:
            return result[0]  # Return the name
        else:
            return "No name found for this card number."

    except sqlite3.Error as e:
        return f"An error occurred: {e}"

    finally:
        # Close the connection
        cursor.close()
        connection.close()


if (__name__) == "__main__" :
    print(get_name_by_card_number(1234123412341234))


# Example usage:
# name = get_name_by_card_number('1234567890123456')
# print(name)
