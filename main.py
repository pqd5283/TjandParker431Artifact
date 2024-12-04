import mysql.connector


# pip install mysql-connector-python

def dbConnect():
    try:
        global connection
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='TjandParker',
            database='footballmanager')
        print("Connected")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def dbClose():
    connection.close()
    print("Closed")


def signplayer():
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM currentplayer")
    records = cursor.fetchall()
    print("Data retrieved from currentplayer table:")
    for record in records:
        print(record)

    cursor.close()

    connection.close()
    print("Closed")
    dbClose()


def releaseplayer():
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM currentplayer")
    records = cursor.fetchall()
    print("Data retrieved from currentplayer table:")
    for record in records:
        print(record)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


def updateplayer():
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM currentplayer")
    records = cursor.fetchall()
    print("Data retrieved from currentplayer table:")
    for record in records:
        print(record)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


def resignplayer():
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM currentplayer")
    records = cursor.fetchall()
    print("Data retrieved from currentplayer table:")
    for record in records:
        print(record)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


def proposetrade():
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM currentplayer")
    records = cursor.fetchall()
    print("Data retrieved from currentplayer table:")
    for record in records:
        print(record)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


def accepttrade():
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM currentplayer")
    records = cursor.fetchall()
    print("Data retrieved from currentplayer table:")
    for record in records:
        print(record)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


def removetrade():
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM currentplayer")
    records = cursor.fetchall()
    print("Data retrieved from currentplayer table:")
    for record in records:
        print(record)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


def signcoach():
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM currentplayer")
    records = cursor.fetchall()
    print("Data retrieved from currentplayer table:")
    for record in records:
        print(record)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


def firecoach():
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM currentplayer")
    records = cursor.fetchall()
    print("Data retrieved from currentplayer table:")
    for record in records:
        print(record)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


def viewrosterstats(position):
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query

    cursor.execute("SELECT * FROM currentplayer")
    records = cursor.fetchall()
    print("Data retrieved from currentplayer table:")
    for record in records:
        print(record)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


if __name__ == '__main__':
    userQuit = False
    while not userQuit:

        selection = input(
            "Hello! Welcome to the NFL General Manager Database Tool. What would you like to do? "
            "\n (1) View roster stats"
            "\n (2) Update Players"
            "\n (3) Update Coaches "
            "\n (4) Open Trade Portal\n (5) Quit \n")

        ##input validation
        while (selection != "1") and (selection != "2") and (selection != "3") and (selection != "4") and (selection != "5"):
            selection = input("What would you like to do? \n (1) View roster stats"
                              "\n (2) Update Players"
                              "\n (3) Update Coaches "
                              "\n (4) Open Trade Portal\n (5) Quit \n")
        ##View roster stats
        if selection == "1":
            position = input("what position would you like to view"
                             " \n(1) Quarterbacks \n(2) Running-backs "
                             "\n(3) Wide receivers \n(4) defensive Players \n(5) GoBack")

            ##input validation
            while (position  != "1") and (position  != "2") and (position  != "3") and (position  != "4") and (position  != "5"):
                position = input("what position would you like to view"
                                  "\n(1) Quarterbacks \n(2) Runningbacks "
                                  "\n(3) Wide receivers \n(4) defensive Players\n(5) Go Back\n")
            if position =="5":
                continue

            viewrosterstats(position)

        ## edit players
        elif selection == "2":
            option = input("what would you like to do with players"
                             " \n(1) Sign Player \n(2) Update Player"
                             "\n(3) Remove Player \n(4) Resign Player \n(5) GoBack")

            ##input validation
            while (option  != "1") and (option  != "2") and (option  != "3") and (option  != "4") and (option  != "5"):
                option = input("what would you like to do with players"
                                " \n(1) Sign Player \n(2) Update Player"
                                "\n(3) Release Player \n(4) Resign Player \n(5) GoBack")
            #signs new player
            if option == "1":
                signplayer()
            #update player depth
            elif option == "2":
                updateplayer()
            #release player
            elif option == "3":
                releaseplayer()
            #update player
            elif option == "4":
                resignplayer()

            elif option == "5":
                continue

        ## edit coaches
        elif selection == "3":
            option = input("what would you like to do with coaching staff"
                           " \n(1) Hire Coach \n(2) Fire Coach \n(3) GoBack")

            ##input validation
            while (option != "1") and (option != "2") and (option != "3"):
                option = input("what would you like to do with coach"
                                " \n(1) Hire Coach \n(2) Fire Coach \n(3) GoBack")
            #hires new coach
            if option == "1":
                signcoach()

            #fires coach
            elif option == "2":
                firecoach()

            elif option == "3":
                continue

        elif selection == "4":
            option = input("what would you like to do in the trade portal"
                           " \n(1) Propose Trade \n(2) Accept Trade \n(3) Remove Trade \n(4) GoBack")

            ##input validation
            while (option != "1") and (option != "2") and (option != "3") and (option != "4"):
                option = input("What would you like to do in the trade portal"
                                "\n(1) Propose Trade \n(2) Accept Trade \n(3) Remove Trade \n(4) GoBack")
            # Propose trade
            if option == "1":
                proposetrade()

            # Accept Trade
            elif option == "2":
                accepttrade()

            #Remove Trade
            elif option == "3":
                removetrade()

            #Go back
            elif option == "4":
                continue


        elif selection == "5":
            print("\nExiting now \n")
            userQuit = True


