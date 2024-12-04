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

    #userInput
    valid = True
    while valid:
        fname = input("What is the players First Name?\n")
        lname = input("What is the players Last Name?\n")
        num = input("What is the players Number?\n")
        cursor.execute(f"SELECT * FROM currentplayer WHERE number ={num}")
        temp = cursor.fetchall()
        
        #checking the number is not already in use
        checknum = False
        while temp != "[]":
            num = input("That Number is already in use. Please Enter a different number\n")
            cursor.execute(f"SELECT * FROM currentplayer WHERE number ={num}")
            temp = cursor.fetchall()
       
        #TODO logic to find lowest playerID not in use
        #for now:
        PlayerID = 25

        #add to player Table
        cursor.execute(f"INSERT INTO Player Values ({PlayerID},{fname},{lname});")

        #TODO: input validation for this
        #Checking position
        position = input("What position is this player:\n "
                         "(qb) QuarterBack\n"
                         "(rb) RunningBack\n"
                         "(wr) Wide reciever\n"
                         "(def) Defensive Player\n")

        if position == 'qb':
            depth = input("what is this Quarterback's depth?")
            comp = input("How many completions does this quaterback have?")
            passyards = input("How many passing yards does this quaterback have?")
            QBR = input("How many Interceptions does this quaterback have?")
            td = input("How many Touchdowns does this quaterback have?")

            #TODO: put this is a try catch
            cursor.execute(f"INSERT INTO QB Values ({PlayerID},{depth},{comp},{passyards},{QBR},{td});")

        elif position == 'rb':
            depth = input("what is this RunningBack's depth?")
            ypc = input("How many Yards per Carry does this RunningBack have?")
            ra = input("How many rushing attempts does this RunningBack have?")
            td = input("How many Touchdowns does this RunningBack have?")

            #TODO: put this is a try catch
            cursor.execute(f"INSERT INTO RB Values ({PlayerID},{depth},{ypc},{ra},{td});")

        elif position == 'wr':
            depth = input("what is this Wide Reciever's depth?")
            recy = input("How many recieving Yards does this Wide Reciever have?")
            targ = input("How many rushing targets does this Wide Reciever have?")
            ypcch = input("How many yards per catch does this Wide Reciever have?")
            td = input("How many Touchdowns does this Wide Reciever have?")

            #TODO: put this is a try catch
            cursor.execute(f"INSERT INTO WR Values ({PlayerID},{depth},{recy},{targ},{ypcch},{td});")

        elif position == 'def':
            depth = input("what is this Wide Reciever's depth?")
            pos = input("What is this players position?")
            tack = input("How many tackles does this Player have?")
            sack = input("How many Sacks does this Player have?")
            ints = input("How many interceptions does this Player have?")
            fumb = input("How many Fumbles does this Player have?")

            #TODO: put this is a try catch
            cursor.execute(f"INSERT INTO Defense Values ({PlayerID},{depth},{pos},{tack},{sack},{ints},{fumb});")

        #TODO logic to find lowest contractID not in use
        #for now:
        contractID = 25

        #TODO: make this current date with datetime stuff
        startdate = 12/4/2024

        enddate = input("when does this player's contract end?")
        sal = input("what is this player's salary")
        cursor.execute(f"INSERT INTO contract Values ({contractID},{startdate},{enddate},{sal},player);")

        cursor.execute(f"SELECT * from coach")
        temp = cursor.fetchall()
        print(temp)
        coach = input("which coach will be this player's coach?")
        
        cursor.execute(f"INSERT INTO currentPlayer Values ({PlayerID},{contractID},{coach},{num});")2
        
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


