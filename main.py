import mysql.connector
import uuid
import datetime


# pip install mysql-connector-python

def dbConnect():
    try:
        global connection
        connection = mysql.connector.connect(
            host=f"{hostname}",
            user=f'{username}',
            password=f'{password}',
            database=f'{databasename}')
        #print("Connected")
    except mysql.connector.Error as err:
        print("Connection failed")


def dbClose():
    connection.close()
    print("Closed")

def signplayer():
    try:
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
            while temp != []:
                num = input("That Number is already in use. Please Enter a different number\n")
                cursor.execute(f"SELECT * FROM currentplayer WHERE number ={num}")
                temp = cursor.fetchall()

            playerID = generate_unique_id()

            #add to player Table
            cursor.execute(f'INSERT INTO player Values ({playerID},"{fname}","{lname}");')
            connection.commit()
            #Checking position
            position = input("What position is this player:\n "
                            "(qb) QuarterBack\n"
                            "(rb) RunningBack\n"
                            "(wr) Wide receiver\n"
                            "(def) Defensive Player\n")

            if position == 'qb':
                depth = input("what is this Quarterback's depth?")
                comp = input("How many completions does this quaterback have?")
                passyards = input("How many passing yards does this quaterback have?")
                QBR = input("How many Interceptions does this quaterback have?")
                td = input("How many Touchdowns does this quaterback have?")

                #calculating completion percentage
                perc = ((int)(comp))/((int)(passyards))

                cursor.execute(f"INSERT INTO QB Values ({playerID},{depth},{perc},{passyards},{QBR},{td});")
                connection.commit()
            elif position == 'rb':
                depth = input("what is this RunningBack's depth?")
                yards = input("How many rushing Yards does this RunningBack have?")
                ra = input("How many rushing attempts does this RunningBack have?")
                td = input("How many Touchdowns does this RunningBack have?")

                #calulate yards per carry
                ypc = (int(yards))/(int(ra))

                cursor.execute(f"INSERT INTO RB Values ({playerID},{depth},{ypc},{yards},{ra},{td});")
                connection.commit()

            elif position == 'wr':
                depth = input("what is this Wide Reciever's depth?")
                recy = input("How many recieving Yards does this Wide Reciever have?")
                targ = input("How many rushing targets does this Wide Reciever have?")
                ypcch = input("How many yards per catch does this Wide Reciever have?")
                td = input("How many Touchdowns does this Wide Reciever have?")

                cursor.execute(f"INSERT INTO WR Values ({playerID},{depth},{recy},{targ},{ypcch},{td});")
                connection.commit()

            elif position == 'def':
                pos = input("What is this players position?")
                depth = input("what is this player's depth?")
                tack = input("How many tackles does this Player have?")
                sack = input("How many Sacks does this Player have?")
                ints = input("How many interceptions does this Player have?")
                fumb = input("How many Fumbles does this Player have?")

                cursor.execute(f"INSERT INTO Defense Values ({playerID},{depth},'{pos}',{tack},{sack},{ints},{fumb});")
                connection.commit()

            contractID = generate_unique_id()

            startdate = currentdate()

            end = None
            while end is None:
                end = enddate()

            sal = input("what is this player's salary")
            print(f"startdate: {startdate}\n EndDate: {end}")
            cursor.execute(f'INSERT INTO contract Values ({contractID},"{startdate}","{end}",{sal},"player");')

            fname = input("First name of this Player's coach:\n")
            lname = input("Last name of this Player's coach:\n")
            cursor.execute(f'SELECT CoachID FROM coach where coach.Fname = "{fname}" AND coach.Lname = "{lname}"')
            coach = cursor.fetchall()
            
            cursor.execute(f"INSERT INTO currentPlayer Values ({playerID},{contractID},{coach},{num});")
            connection.commit()
            print("Player added to database!")
            valid = False
        cursor.close()

        connection.close()
        print("Closed")
        dbClose()
    except Exception as e: 
        print("An error occured")

def releaseplayer():
    try: 
        dbConnect()
        # Create a cursor object
        cursor = connection.cursor()

        # Get info needed to delete player from all tables
        num = int(input("what number is the player you want to release?"))

        num = input("What is the players Number?\n")
        cursor.execute(f"SELECT * FROM currentplayer WHERE number ={num}")
        temp = cursor.fetchall()
        
        #checking the number is not already in use
        checknum = False
        while temp == []:
            num = input("No Player has that number. Please Enter a different number\n")
            cursor.execute(f"SELECT * FROM currentplayer WHERE number ={num}")
            temp = cursor.fetchall()

        cursor.execute(f"Select PlayerID,ContractID From CurrentPlayer Where Number = {num}")
        temp = cursor.fetchall()
        pID = temp[0][0]
        conID = temp[0][1]
        

        cursor.execute(f"Delete From contract Where ContractID = {conID}")


        cursor.execute(f"Delete From qb Where PlayerID = {pID}")
        cursor.execute(f"Delete From rb Where PlayerID = {pID}")
        cursor.execute(f"Delete From wr Where PlayerID = {pID}")
        cursor.execute(f"Delete From defense Where PlayerID = {pID}")

        connection.commit()

        # cursor.execute(f"Select contractID From CurrentPlayer Where Number = {num}")
        # conID = cursor.fetchall()

        # cursor.execute(f"Remove From currentPlayer = {num}")


        

        # Close the cursor
        cursor.close()

        # Close the connection
        connection.close()
        print("Closed")
        dbClose()
    except Exception as e:
        print("an error occured\n ")

def updateplayer():
    try: 
        dbConnect()
        # Create a cursor object
        cursor = connection.cursor()

        #get info about player
        num = int(input("what number is the player you want to update?"))
        cursor.execute(f"Select PlayerID From CurrentPlayer Where Number = {num}")
        temp = cursor.fetchall()
        pID = temp[0][0]
        
        #find the position of the player
        cursor.execute(f"select * from qb where PlayerID = {pID}")
        temp = cursor.fetchall() 
        if temp != []:
            position = 'qb'

        cursor.execute(f"select * from wr where PlayerID = {pID}")
        temp = cursor.fetchall() 
        if temp != []:
            position = 'wr'

        cursor.execute(f"select * from rb where PlayerID = {pID}")
        temp = cursor.fetchall() 
        if temp != []:
            position = 'rb'

        cursor.execute(f"select * from defense where PlayerID = {pID}")
        temp = cursor.fetchall() 
        if temp != []:
            position = 'def'      

        if position == 'qb':
            depth = input("what is this Quarterback's depth?")
            comp = input("How many completions does this quaterback have?")
            passyards = input("How many passing yards does this quaterback have?")
            QBR = input("How many Interceptions does this quaterback have?")
            td = input("How many Touchdowns does this quaterback have?")

            #calculating completion percentage
            perc = ((int)(comp))/((int)(passyards))
            if perc == 1:
                perc = .99

            cursor.execute(f"DELETE FROM QB where PlayerID = {pID}")
            connection.commit()
            cursor.execute(f"INSERT INTO QB Values ({pID},{depth},{perc},{passyards},{QBR},{td});")
            connection.commit()
        elif position == 'rb':
            depth = input("what is this RunningBack's depth?")
            yards = input("How many rushing Yards does this RunningBack have?")
            ra = input("How many rushing attempts does this RunningBack have?")
            td = input("How many Touchdowns does this RunningBack have?")

            #calulate yards per carry
            ypc = (int(yards))/(int(ra))

            cursor.execute(f"DELETE FROM RB where PlayerID = {pID}")
            connection.commit()
            cursor.execute(f"INSERT INTO RB Values ({pID},{depth},{ypc},{yards},{ra},{td});")
            connection.commit()

        elif position == 'wr':
            depth = input("what is this Wide Reciever's depth?")
            recy = input("How many recieving Yards does this Wide Reciever have?")
            targ = input("How many rushing targets does this Wide Reciever have?")
            ypcch = input("How many yards per catch does this Wide Reciever have?")
            td = input("How many Touchdowns does this Wide Reciever have?")

            cursor.execute(f"DELETE FROM WR where PlayerID = {pID}")
            connection.commit()
            cursor.execute(f"INSERT INTO WR Values ({pID},{depth},{recy},{targ},{ypcch},{td});")
            connection.commit()

        elif position == 'def':
            pos = input("What is this players position?")
            depth = input("what is this player's depth?")
            tack = input("How many tackles does this Player have?")
            sack = input("How many Sacks does this Player have?")
            ints = input("How many interceptions does this Player have?")
            fumb = input("How many Fumbles does this Player have?")

            cursor.execute(f"DELETE FROM Defense where PlayerID = {pID}")
            connection.commit()
            cursor.execute(f"INSERT INTO Defense Values ({pID},{depth},'{pos}',{tack},{sack},{ints},{fumb});")
            connection.commit()


        # Close the cursor
        cursor.close()

        # Close the connection
        connection.close()
        print("Closed")
        dbClose()

    except Exception as e:
        connection.rollback()
        print("an error occured during resign process transaction rolled back")

def resignplayer():
    try:
        dbConnect()
        # Create a cursor object
        cursor = connection.cursor()
        cursor.execute("START TRANSATION")

        num = input("what is the number of the player you want to resign?")

        cursor.execute(f"Select PlayerID FROM CurrentPlayer where PlayerID = {pID}")
        temp = cursor.fetchall()
        pID = temp[0][0]

        cursor.execute(f"Select contractID FROM CurrentPlayer where PlayerID = {pID}")
        temp = cursor.fetchall()
        contractID = temp[0][0]

        newEndDate = input("What is the new end date of this player?")
        newSalary = input("what is the new salary for this player?")

        cursor.execute(f"UPDATE contract where ContractID = {contractID} set endDate = {newEndDate}, salary = {newSalary}")

    except Exception as e:
        connection.rollback()
        print("an error occured during resign process transaction rolled back")

    
    
            

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


    fname = input("Trade target first name:\n")
    lname = input("Trade target last name:\n")
    curretTeam = input("Trade target's current team:\n")


    validtrade = None
    while validtrade is None:
            try:
                whotradefname = input("Who do you want to trade first name:\n")
                whotradelname = input("Who do you want to trade last name:\n")
                cursor.execute(f'SELECT playerID FROM player WHERE Fname = "{whotradefname}" and Lname = "{whotradelname}"')
                whotradeid = cursor.fetchone()
                whotradeid = whotradeid[0]
                print(whotradeid)
                validtrade = True
                additionalOffers = input("Any additional offers:\n")
                status = "Pending"
                newPlayerID = generate_unique_id()
                tradeID = generate_unique_id()
                print(newPlayerID)
                # Execute a query
                cursor.execute(f'INSERT INTO Player values({newPlayerID}, "{fname}", "{lname}")')
                connection.commit()
                cursor.execute(f'INSERT INTO TradeTarget values({newPlayerID}, "{fname}", "{lname}", "{curretTeam}")')
                connection.commit()
                cursor.execute(
                    f'INSERT INTO TradeProposal values({tradeID}, {whotradeid}, {newPlayerID}, "{status}", "{additionalOffers}")')
                connection.commit()
                # Close the cursor
                cursor.close()
            except:
                print("Invalid input, try again\n")
    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


def accepttrade():
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()
    validtrade = None
    while validtrade is None:
            try:
                whotradefname = input("Who do you want to accept from trade first name:\n")
                whotradelname = input("Who do you want to accept from trade last name:\n")
                cursor.execute(f'SELECT playerID FROM player WHERE Fname = "{whotradefname}" and Lname = "{whotradelname}"')
                whotradeid = cursor.fetchone()
                whotradeid = whotradeid[0]
                print(whotradeid)
                cursor.execute(f'SELECT tradeID FROM tradeproposal WHERE NewPlayer = {whotradeid} AND Status = "Pending"')
                thetradeid = cursor.fetchone()
                thetradeid = thetradeid[0]
                print(thetradeid)
                cursor.execute(f'UPDATE TradeProposal SET Status = "Accepted" WHERE TradeID = {thetradeid}')
                connection.commit()
                print("Accepted")
                cursor.execute(f'SELECT oldplayer from tradeproposal where TradeID = {thetradeid}')
                removetradedplayer = cursor.fetchone()
                removetradedplayer = removetradedplayer[0]
                print("oldplayer fetched")
                cursor.execute(f'SELECT contractid from currentplayer where playerid = {removetradedplayer}')
                removedcontractid = cursor.fetchone()
                removedcontractid = removedcontractid[0]
                cursor.execute(f'REMOVE FROM contract where contractid = {removedcontractid}')
                connection.commit()


                salary = float(input("What is the players salary\n"))
                salary = "{:10.2f}".format(salary)
                contractend = enddate()
                contractstart = currentdate()
                contractid = generate_unique_id()
                cursor.execute(f'INSERT INTO contract values({contractid}, "{contractstart}", "{contractend}", "{salary}", "Player")')
                cursor.commit()
                position = input("What position is the traded player (qb, rb, wr, defense):\n")
                if position != "qb" and position != "rb" and position != "wr" and position != "defense":
                    raise Exception
                number = input("What number is the traded player:\n")
                cursor.execute(f'SELECT * from currentplayer where number = {number}')
                numcheck = cursor.fetchall()
                if numcheck != []:
                    raise Exception
                coachfname = input("First name of the players coach")
                coachlname = input("Last name of the players coach")
                cursor.execute(f'SELECT coachID FROM coach WHERE Fname = "{coachfname}" and Lname = "{coachlname}"')
                coachid = cursor.fetchone()
                coachid = coachid[0]
                cursor.execute(f'INSERT INTO currentplayer values({whotradeid}, {contractid}, {coachid}, {number})')
                cursor.commit()
                cursor.execture(f'INSERT into {position} (PlayerID) value {whotradeid}')
                cursor.commit()


                validtrade = True
            except:
                print("Invalid input, try again\n")

    cursor.close()

    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


def removetrade():
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    validtrade = None
    while validtrade is None:
            try:
                whotradefname = input("Who do you want to remove from trade first name:\n")
                whotradelname = input("Who do you want to remove from trade last name:\n")
                cursor.execute(f'SELECT playerID FROM player WHERE Fname = "{whotradefname}" and Lname = "{whotradelname}"')
                whotradeid = cursor.fetchone()
                whotradeid = whotradeid[0]
                print(whotradeid)
                cursor.execute(f'SELECT tradeID FROM tradeproposal WHERE NewPlayer = {whotradeid} AND Status = "Pending"')
                thetradeid = cursor.fetchone()
                thetradeid = thetradeid[0]
                print(thetradeid)
                cursor.execute(f'DELETE FROM tradeproposal WHERE tradeID = {thetradeid}')
                connection.commit()
                cursor.execute(f'DELETE FROM player where playerid = {whotradeid}')
                connection.commit()
                validtrade = True
            except:
                print("Invalid input, try again\n")

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()
    print("Closed")
    dbClose()


def signcoach():
    dbConnect()
    # Create a cursor object
    fname = input("First name of coach who you want to hire:\n")
    lname = input("Last name of coach who you want to hire:\n")
    title = input("What is the coaches title\n")
    salary = float(input("What is the coaches salary\n"))
    salary = "{:10.2f}".format(salary)

    contractenddate = None
    while contractenddate is None:
        contractenddate = enddate()
    startdate = currentdate()
    coachID = generate_unique_id()
    contractID = generate_unique_id()
    cursor = connection.cursor()

    isheadcoach = None
    while isheadcoach != "Y" and isheadcoach != "N":
        isheadcoach = input("Is the coach a headcoach (Y/N):")
    
    supervisorid = None
    if isheadcoach == "Y":
        pass
    else:
        cursor.execute("SELECT * FROM coach")
        records = cursor.fetchall()
        print("Coach list:")
        for record in records:
            print(record)
        while supervisorid is None:
            try:
                supervisorfname = input("First name of coaches supervisor")
                supervisorlname = input("Last name of coaches supervisor")
                cursor.execute(f'SELECT coachID FROM coach WHERE Fname = "{supervisorfname}" and Lname = "{supervisorlname}"')
                supervisorid = cursor.fetchone()
                supervisorid = supervisorid[0]
            except:
                print("Invalid input, try again\n")
            


    cursor.execute(f'INSERT INTO contract values ({contractID}, "{startdate}", "{contractenddate}", {salary}, "Coach")')
    connection.commit()
    cursor.execute(f'INSERT INTO coach values ({coachID},"{fname}","{lname}","{supervisorid}","{title}",{contractID})')
    connection.commit()

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
    isvalidquery = None
    while isvalidquery is None:
        try:
            fname = input("First name of coach who you want to fire:\n")
            lname = input("Last name of coach who you want to fire:\n")
            cursor.execute(f'SELECT ContractID FROM coach where coach.Fname = "{fname}" AND coach.Lname = "{lname}"')
            contractIDDelete = cursor.fetchone()
            contractIDDelete = contractIDDelete[0]
            print(contractIDDelete)
            cursor.execute(f'DELETE FROM contract where contract.ContractID = {contractIDDelete}')
            connection.commit()
            isvalidquery = True
        except:
            print("Invalid coach, please try again")
            # Close the cursor
    cursor.close()

    # Close the connection
    dbClose()


def viewrosterstats(position):
    dbConnect()
    # Create a cursor object
    cursor = connection.cursor()

    if position == "1":
        pos = "qb"
    elif position == "2":
        pos = "rb"
    elif position == "3":
        pos = "wr"
    elif position == "4":
        pos = "defense"

    cursor.execute(
        f'SELECT * FROM player JOIN currentplayer ON player.playerID = currentplayer.PlayerID JOIN {pos} ON currentplayer.PlayerID = {pos}.PlayerID')
    # Execute a query
    records = cursor.fetchall()
    print("Stats retrieved:")
    for record in records:
        print(record)

    # Close the cursor
    cursor.close()

    # Close the connection
    dbClose()

def generate_unique_id():
    #generates a unique interger id that is 5 characters
    return int(uuid.uuid4().int % 1e5)

def currentdate():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    return formatted_date

def enddate():
    enddate = input("Which date does the contract end (YYYY-MM-DD):\n")
    try:
        datetime.datetime.strptime(enddate, "%Y-%m-%d")
        return enddate
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

def login():
    loggedin = None
    while loggedin is None:
        try:
            global hostname 
            global username
            global password
            global databasename
            hostname = input("What is the hostname\n")
            username = input("what is the username\n")
            password = input("What is the password\n")
            databasename = input("What is the database schema name\n")
            dbConnect()
            loggedin = True
        except:
            pass

if __name__ == '__main__':
    userQuit = False
    login()
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


