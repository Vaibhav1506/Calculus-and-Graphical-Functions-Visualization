import mysql.connector as mc
import sys

def create_SQL_database(host_name, user_name, password):
    try:
        print("Connecting to the MySQL Database ... ")

        obj = mc.connect(host = host_name, user = user_name, passwd = password)

        # Checking whether the connection is established
        if not obj.is_connected():
            print("Database connection was not successful.")
            print("Exiting code ...")
            sys.exit()
        
        else:
            print("Connected successfully. Database has been created.")

        co = obj.cursor()

        # Create the database if it doesn't exist
        co.execute("CREATE DATABASE IF NOT EXISTS calculus_DB;")
        co.execute("USE calculus_DB;")

        # Create the table if it doesn't exist
        co.execute("""CREATE TABLE IF NOT EXISTS Calculus_User_History 
                    (`Operation Type` VARCHAR(100) ,
                    `Operation Type Choice` VARCHAR(100) ,
                    `Function Type` VARCHAR(100) ,
                    `Function Type Choice` VARCHAR(100) ,
                    `Function Expression` VARCHAR(100) ,
                    `Function Expression Choice` VARCHAR(100) ,
                    `Answer` VARCHAR(100) UNIQUE);""")

        obj.commit()  # Required after a database modification

    except mc.Error as e:
        print("Error encountered was: ", str(e))
    
    finally:
        co.close()  # Close the cursor
        obj.close()  # Close the connection

def insert_into_SQL_database(host_name, user_name, password, L):
    try:
        obj = mc.connect(host = host_name, user = user_name, passwd = password, database = "calculus_DB")
        co = obj.cursor()
        sql = "INSERT INTO Calculus_User_History (`Operation Type`, `Operation Type Choice`, `Function Type`, `Function Type Choice`, `Function Expression`, `Function Expression Choice`, `Answer`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (L[0], L[1], L[2], L[3], L[4], L[5], L[6])
        co.execute(sql, values)
        obj.commit()  # Add this line to commit the changes
    
    except mc.Error:
        pass
    
    finally:
        co.close()  # Close the cursor
        obj.close()  # Close the connection

def execute_SQL_choices(ch, host_name, user_name, password):
    obj = mc.connect(host=host_name, user=user_name, passwd=password, database="calculus_DB")

    co = obj.cursor()

    # Executes SQL queries
    if ch == 6:  # Show all user history
        data = []
        query = "SELECT * FROM Calculus_User_History"
        co.execute(query)
        data = co.fetchall()

        if data == []:
            print(["Operation Type", "Operation Type Choice", "Function Type", "Function Type Choice", "Function Expression", "Function Expression Choice", "Answer"])
            print("No User history to show as no mathematical expressions have been evaluated.")
        
        else:
            print(["Operation Type", "Operation Type Choice", "Function Type", "Function Type Choice", "Function Expression", "Function Expression Choice", "Answer"])
            print(f"Displaying {len(data)} records: ")
            for i in data:
                print(list(i))
        
        obj.close()  # Close the connection when done

    elif ch == 7:
        data = []
        print("SEARCH BY:- ")
        print("1. Operation Type.")
        print("2. Function Type.")
        print("3. Function Expression.")
        ch1 = int(input("Enter choice:"))

        if ch1 == 1:
            Operation_Type = input("Enter the type of operation you want to search: ")
            query = "SELECT * FROM Calculus_User_History WHERE `Operation Type` = '{}'".format(Operation_Type.title())
            co.execute(query)
            data = co.fetchall()
            print(f"Showing data with Operation Type as {Operation_Type.title()} ... ")
            print(["Operation Type", "Operation Type Choice", "Function Type", "Function Type Choice", "Function Expression", "Function Expression Choice", "Answer"])
            if data == []:
                print("No records were found.")
            else:
                print(f"Displaying {len(data)} records: ")
                for i in data:
                    print(list(i))

        elif ch1 == 2:
            Function_Type = input("Enter the type of function you want to search: ")
            query = "SELECT * FROM Calculus_User_History WHERE `Function Type` = '{}'".format(Function_Type.title())
            co.execute(query)
            data = co.fetchall()
            print(f"Showing data with Function Type as {Function_Type.title()}")
            print(["Operation Type", "Operation Type Choice", "Function Type", "Function Type Choice", "Function Expression", "Function Expression Choice", "Answer"])
            if data == []:
                print("No records were found.")
            else:
                print(f"Displaying {len(data)} records: ")
                for i in data:
                    print(list(i))

        elif ch1 == 3:
            Function_expression = input("Enter the type of function you want to search: ")
            query = "SELECT * FROM Calculus_User_History WHERE `Function Expression` = '{}'".format(Function_expression.title())
            co.execute(query)
            data = co.fetchall()
            print(f"Showing data with Function Expression as {Function_expression.title()}")
            print(["Operation Type", "Operation Type Choice", "Function Type", "Function Type Choice", "Function Expression", "Function Expression Choice", "Answer"])
            if data == []:
                print("No records were found.")
            else:
                print(f"Displaying {len(data)} records: ")
                for i in data:
                    print(list(i))

def check_duplicates(x, host_name, user_name, password):
    obj = mc.connect(host=host_name, user=user_name, passwd=password, database="calculus_DB")
    co = obj.cursor()
    data = []
    query = "SELECT * FROM Calculus_User_History"
    co.execute(query)
    data = co.fetchall()
    C, ans = 0, ""
    for i in data:
        if x == i[4]:
            ans = i[6]
            break
    return [C, ans]
    
print(check_duplicates("sin(5x+4)", "localhost", "root", "Vaibhav0304000910!"))