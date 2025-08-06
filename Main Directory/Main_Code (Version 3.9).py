import matplotlib.pyplot as plt, numpy as np, math, mysql.connector as mc, os, platform, datetime, time, subprocess, webbrowser, keyboard, sys, pyfiglet

def show_headers(mode):
    def decorator(func):
        def wrapper(data, *args, **kwargs):
            if mode == "SELECT":
                print("Showing Records:")
            elif mode == "DELETE":
                print("Deleting Records:")
            
            if not data:
                print("No user history to show as no mathematical expressions have been evaluated yet.")
            else:
                print(f"Displaying {len(data)} records:")
            
            print(["Operation Type", "Operation Type Choice", "Function Type", "Function Type Choice", "Function Expression", "Function Expression Choice", "Answer", "Date", "Time"])
            result = func(data, *args, **kwargs)

            if mode == "DELETE":
                print("Showing the Updated Records:")
            
            return result
        return wrapper
    return decorator

class DatabaseManager:
    
    def __init__(self, host_name, user_name, passwd):
        self.host_name = host_name
        self.user_name = user_name
        self.passwd = passwd

    def create_SQL_database(self):
        try:
            print("Connecting to the MySQL Database...")
            time.sleep(2.5)
            obj = mc.connect(host=self.host_name, user=self.user_name, passwd=self.passwd)
            print("Connected successfully.")

            co = obj.cursor()
            co.execute("CREATE DATABASE IF NOT EXISTS calculus_DB;")
            co.execute("USE calculus_DB;")
            co.execute("CREATE TABLE IF NOT EXISTS Calculus_User_History (`Operation Type` VARCHAR(100), `Operation Type Choice` VARCHAR(100), `Function Type` VARCHAR(100), `Function Type Choice` VARCHAR(100),`Function Expression` VARCHAR(100), `Function Expression Choice` VARCHAR(100), `Answer` VARCHAR(100) UNIQUE, `Date` DATE, `Time` TIME);")

            print("Database and table created successfully.")

        except mc.Error as e:
            print("Can't connect to database. Checking for errors...")
            time.sleep(2.5)
            print("Error encountered:", str(e))
            print("Exiting code ...")
            print("Please try again later.")
            os._exit(0)

        finally:
            DatabaseManager.close_resources(co, obj) #type:ignore
 
    def insert_into_SQL_database(self, L):
        try:
            obj = mc.connect(host = self.host_name, user = self.user_name, passwd = self.passwd, database = "calculus_DB")
            co = obj.cursor()
            sql = "INSERT INTO Calculus_User_History (`Operation Type`, `Operation Type Choice`, `Function Type`, `Function Type Choice`, `Function Expression`, `Function Expression Choice`, `Answer`, `Date`, `Time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (L[0], L[1], L[2], L[3], L[4], L[5], L[6], L[7], L[8])
            co.execute(sql, values)
            obj.commit()  
        
        except mc.Error:
            pass

        finally:
            DatabaseManager.close_resources(co, obj)  #type:ignore
    
    @staticmethod
    def close_resources(cursor, connection):
        if cursor is not None:
            try:
                cursor.close()
            except Exception as e:
                print("Error closing cursor:", str(e))
        if connection is not None:
            try:
                if connection.is_connected():
                    connection.close()
            except Exception as e:
                print("Error closing connection:", str(e))

    @staticmethod
    def iterate_data(data):
        for i in list(data):
            i = list(i)
            i[-1] = str(str("0" + str(i[-1])) if int(str(i[-1])[0]) < 10 and str(i[-1])[1] == ":" else str(i[-1]))
            i[-2] = str(i[-2])
            print(i)    
    
    def execute_SQL_choices(self, ch):
        try:
            obj = mc.connect(host=self.host_name, user=self.user_name, passwd=self.passwd, database="calculus_DB")
            co = obj.cursor()
            data, mode, query = [], "", ""

            if ch == 5:
                mode = "SELECT"
                print("SEARCH BY:- ")
            elif ch == 6:
                mode = "DELETE"
                print("DELETE BY:- ")
            else:
                print("Invalid choice. Please Try again.")
                return 

            print("1. All")
            print("2. Operation Type.")
            print("3. Operation Type Choice.")
            print("4. Function Type.")
            print("5. Function Type Choice.")
            print("6. Function Expression.")
            print("7. Function Expression Choice.")
            print("8. Answer.")
            print("9. Date.")
            print("10. Time.")

            choice = int(input("Enter the choice: "))

            if choice == 1:
                query = f"{mode} * FROM Calculus_User_History;"
            
            elif choice == 2:
                Operation_Type = input("Enter the type of operation you want to search: ")
                query = f"{mode} * FROM Calculus_User_History WHERE `Operation Type` = '{Operation_Type.title()}'"
            
            elif choice == 3:
                Operation_Type_Choice_No = input("Enter the choice number of operation you want to search: ")
                query = f"{mode} * FROM Calculus_User_History WHERE `Operation Type Choice` = '{Operation_Type_Choice_No.title()}'"
            
            elif choice == 4:
                Function_Type = input("Enter the type of function you want to search: ")
                query = f"{mode} * FROM Calculus_User_History WHERE `Function Type` = '{Function_Type.title()}'"
            
            elif choice == 5:
                Function_Type_Choice_No = input("Enter the choice number of function you want to search: ")
                query = f"{mode} * FROM Calculus_User_History WHERE `Function Type Choice` = '{Function_Type_Choice_No.title()}'"
            
            elif choice == 6:
                Function_expression = input("Enter the type of function expression you want to search: ")
                query = f"{mode} * FROM Calculus_User_History WHERE `Function Expression` = '{Function_expression.title()}'"
            
            elif choice == 7:
                Function_expression_Choice_No = input("Enter the choice number of function expression you want to search: ")
                query = f"{mode} * FROM Calculus_User_History WHERE `Function Expression Choice` = '{Function_expression_Choice_No.title()}'"
            
            elif choice == 8:
                Answer = input("Enter the answer you want to search: ")
                query = f"{mode} * FROM Calculus_User_History WHERE `Answer` = '{Answer}'"
            
            elif choice == 9:
                print("ENTER DATE RANGE")
                start_date_month = input("Enter Starting Month: ").lower()
                end_date_month = input("Enter Ending Month: ").lower()

                months_dict = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06", "july": "07", "august": "08", "september": "09", "october": "10", "november": "11", "december": "12"}

                if start_date_month in months_dict and end_date_month in months_dict:
                    start_dt_month = months_dict[start_date_month]
                    end_dt_month = months_dict[end_date_month]
                else:
                    print("Invalid Input.")
                    return

                start_date_day = int(input("Enter Starting Day: "))
                end_date_day = int(input("Enter Ending Day: "))
                start_date_year = int(input("Enter Starting Year: "))
                end_date_year = int(input("Enter Ending Year: "))

                if 1 <= start_date_day <= 31 and 1 <= end_date_day <= 31 and start_date_year > 0 and end_date_year > 0:
                    query = (f"{mode} * FROM Calculus_User_History WHERE Date BETWEEN "f"'{start_date_year:04d}-{start_dt_month}-{start_date_day:02d}' AND " f"'{end_date_year:04d}-{end_dt_month}-{end_date_day:02d}'")
                else:
                    print("Invalid Input. Please try again.")
                    return

            elif choice == 10:
                print("ENTER TIME RANGE")
                start_time_hour = int(input("Enter Starting Time Hour: "))
                end_time_hour = int(input("Enter Ending Time Hour: "))

                start_time_minute = int(input("Enter Starting Time Minute: "))
                end_time_minute = int(input("Enter Ending Time Minute: "))

                start_time_seconds = int(input("Enter Starting Time Second: "))
                end_time_seconds = int(input("Enter Ending Time Second: "))

                if 0 <= start_time_hour < 24 and 0 <= end_time_hour < 24 and 0 <= start_time_minute < 60 and 0 <= end_time_minute < 60 and 0 <= start_time_seconds < 60 and 0 <= end_time_seconds < 60:
                    query = (f"{mode} * FROM Calculus_User_History WHERE Time BETWEEN " f"'{start_time_hour:02d}:{start_time_minute:02d}:{start_time_seconds:02d}' AND " f"'{end_time_hour:02d}:{end_time_minute:02d}:{end_time_seconds:02d}'")
                else:
                    print("Invalid Input. Please try again.")
                    return

            else:
                print("Invalid choice. Please Try again.")
                return

            co.execute(query)
            
            if mode == "DELETE":
                query = query.replace("DELETE", "SELECT")
                co.execute(query) 

            data = co.fetchall()
            decorated_iterate_data = show_headers(mode)(self.iterate_data)
            decorated_iterate_data(data)

        except mc.Error as e:
            pass

        finally:
            DatabaseManager.close_resources(co, obj)    #type:ignore

def return_abs_path(pdf_file):
    return os.path.abspath(os.path.join("Python Integral", "Help, Guide and more Info" ,f"{pdf_file + ".pdf"}"))

def masked_input(prompt=""):
    print(prompt, end="", flush=True)
    password = ""

    while True:
        event = keyboard.read_event(suppress=True)  
        if event.event_type != keyboard.KEY_DOWN:  
            continue

        key = event.name
        if key is None:  # Ensure key is not None
            continue

        if key == "enter":
            break
        elif key == "backspace":
            if password:
                sys.stdout.write("\b \b")
                sys.stdout.flush()
                password = password[:-1]
        elif len(key) == 1:  # Safe since key is not None
            password += key
            sys.stdout.write("*")
            sys.stdout.flush()

    return password

def open_pdf(file_path):
    platform_type = detect_platform()
    
    try:
        if platform_type == "Windows":
            subprocess.Popen(["start", "" ,file_path], shell=True)
        elif platform_type == "macOS":
            subprocess.run(["open", file_path], check=True)
        elif platform_type == "Linux Desktop":
            subprocess.run(["xdg-open", file_path], check=True)
        elif platform_type in ["Android", "Java"] :
            os.system(f"am start -a android.intent.action.VIEW -t application/pdf -d file://{file_path}")
        elif platform_type == "iOS or iPadOS":
            file_url = f"file://{os.path.abspath(file_path)}"
            webbrowser.open(file_url)
        else:
            print(f"Unsupported platform: {platform_type}")
        
        print(time.sleep(2.5))
        print(f"Successfully opened {file_path} on {platform_type}.")
    except Exception as e:
        print(f"Failed to open the file on {platform_type}: {e}")

def open_help():
    print("What do you want to open ? :-")
    menu = {1 : "Flow of Control", 2 : "Official Guide and Documentation", 3 : "SYNOPSIS"}

    for i, j in menu.items():
        print(str(i) + ".", j)

    ch4 = int(input("Enter the choice :- "))

    if ch4 in range(1, 4):
        abs_path = return_abs_path(menu[ch4]) 
        print("Opening ... ")
        time.sleep(2.5)
        open_pdf(abs_path)

    else:
        print("Invalid Choice.")

def return_system_info():
    OS = detect_platform()
    print("Checking ...")
    time.sleep(2.5)
    print("Gathering System Information ...")
    sys_info = platform.uname()
    time.sleep(5)
    print("You are using : ")
    print(f"System: {sys_info.system}")
    print(f"Device Name: {sys_info.node}")
    print(f"{OS} Version: {sys_info.release}")
    print(f"{OS} Version: {sys_info.version}")
    print(f"Build / Architecture: {sys_info.machine}")

def is_android():
    os_name = platform.uname()
    if os_name.system == 'Linux':
        if 'ANDROID_ROOT' in os.environ or os.path.exists('/system'):
            return True
    return False

def is_ios_or_ipados():
    os_name = platform.uname()
    if os_name.system == 'Darwin':
        if os_name.machine == 'arm64' and not os.path.exists('/Applications'):
            return True
    return False

def detect_platform():
    os_name = platform.uname()
    if os_name.system == 'Linux':
        if is_android():
            return "Android"
        else:
            return "Linux Desktop"
    elif os_name.system == 'Darwin':
        if is_ios_or_ipados():
            return "iOS or iPadOS"
        else:
            return "macOS"
    elif os_name.system == "Windows":
        return "Windows"
    elif os_name.system == "Java":
        return "Android"
    else:
        return f"Unknown platform: {os_name.system}"

def get_date_time():  
    current_datetime = datetime.datetime.now()

    year = current_datetime.year
    month = current_datetime.month
    day = current_datetime.day
    
    hour = current_datetime.hour
    minute = current_datetime.minute
    second = current_datetime.second

    formatted_date = f"{year:02d}-{month:02d}-{day:02d}"
    formatted_time = f"{hour:02d}:{minute:02d}:{second:02d}"

    return [formatted_date, formatted_time]

def get_sup(x):  
    normal = "abcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    
    return x.translate(res)

def convert_to_Latex_for_differentials(x, mappings):  

    if "√" in x and "/" in x:  
        n = x.index('²')  
        
        if x[n + 1] == ")" or x[n + 1] == "-":  
            x = x.replace('²', r'^{2}')  
        
        expression_list = x.split("/")  
        updated_expression_list = []
    
        for item in expression_list:  
            updated_item = item  
            for key, value in mappings.items():  
                updated_item = updated_item.replace(key, value)  
            updated_expression_list.append(updated_item)  

        st = r"$\dfrac{" + updated_expression_list[0] + "}{" + updated_expression_list[1] + "}$"  

    elif "/" in x:
        expression_list = x.split("/")  
        st = "$" + r'\dfrac{' + expression_list[0] + "}{" + expression_list[1] + "}" + "$"  

    else:  
        if "²" in x:
            n = x.index('²')  
            if x[n + 1] == "(" or x[n + 1] == ")":  
                x = x.replace('²', r'^{2}')  
        
        for key, value in mappings.items():
            x = x.replace(key, value)  
        
        st = "$" + x + "$"  

    print(st)  
    expression = f"{st}"
    return expression  

def convert_to_Latex_for_integrals(x, mappings):  
    
    if "√" in x and "¹" in x:
        expression_list = x[1:-5].split("/")  
        func_end_idx = (expression_list[0].index("¹"))  
        a = expression_list[0][func_end_idx + 1:]  
        updated_expression_list = [a[1:], expression_list[1][:-1]]  

        for i in range(len(updated_expression_list)):
            updated_item = updated_expression_list[i]
            for key, value in mappings.items():
                updated_item = updated_item.replace(key, value)  
            updated_expression_list[i] = updated_item

        st = r"\dfrac" + updated_expression_list[0] + "{" + updated_expression_list[1] + "}"  
        func = expression_list[0][:func_end_idx + 1]  
        
        for key, value in mappings.items():  
            func = func.replace(key, value)  
            func = func.replace('\\\\', '\\')
        num_r = func + "{(" + st + ")}"  
        den_r = expression_list[2]  

        for key, value in mappings.items():  
            den_r = den_r.replace(key, value)
        final_exp = r"\dfrac" + "{" + num_r + "}" + den_r  

        st = '$' + final_exp + x[-4:] + '$'  

    elif "/" in x:
        expression_list = x[1:-5].split("/")  
        updated_expression_list = []

        for item in expression_list:
            updated_item = item
            
            for key, value in mappings.items():  
                updated_item = updated_item.replace(key, value)
                
            updated_item = updated_item.replace('\\\\', '\\')  
            updated_expression_list.append(updated_item)

        st = '$' + r'\dfrac{' + updated_expression_list[0] + "}" + "{" + updated_expression_list[1] + "}" + x[-4:] + '$'  

    else:
        n = x.index('²')  
        if x[n + 1] == "(" or x[n + 2] == "+":  
            x = x.replace('²', r'^{2}')  

        for key, value in mappings.items():
            x = x.replace(key, value)  
        
        st = "$" + x + "$"  

    print(st)
    expression = f"{st}"  
    return expression  

def display_Latex(expression):  
    plt.text(0.5, 0.5, expression, fontsize=15, ha='center', va='center')  
    plt.axis('off')  
    plt.show()

def evaluate_math_expression_to_numpy(x):  
    st = x  
    mappings = {  
        "[": "np.abs(",  
        "]": ")",
        "√": "np.sqrt",  
        "⌊": "np.floor(",  
        "⌋": ")",
        "⌈": "np.ceil(",  
        "⌉": ")",
        "sin(": "np.sin(",  
        "cos(": "np.cos(",
        "tan(": "np.tan(",
        "cot(": "1 / np.tan(",
        "csc(": "1 / np.sin(",
        "sec(": "1 / np.cos(",
        "sin^-1(": "np.arcsin(",
        "cos^-1(": "np.arccos(",
        "tan^-1(": "np.arctan(",
        "cot^-1(": "np.arctan(1 / ",
        "sec^-1(": "np.arccos(1 / ",
        "csc^-1(": "np.arcsin(1 / ",
        "^": "**",  
        "1x": "1 * x",  
        "2x": "2 * x",
        "3x": "3 * x",
        "4x": "4 * x",
        "5x": "5 * x",
        "6x": "6 * x",
        "7x": "7 * x",
        "8x": "8 * x",
        "9x": "9 * x",
        "0x": "0 * x",
        "πx": "np.pi * x",  
        "ex": "np.e * x",  
        "\bπ\b": "np.pi",  
        "\be\b": "np.e",  
        "log(": "np.log(",  
    }

    for key, value in mappings.items():  
        st = st.replace(key, value)
   
    return [st, x]

def decide_range_of_function(a):  
    if "⌊" in a or "⌋" in a or "⌈" in a or "⌉" in a or "[" in a or "]" in a:
        n = np.linspace(-6, 6, 1000)
        m = np.arange(-6, 6, 0.5)

    elif "log" in a:
        n = np.linspace(0.1, 5, 100)
        m = np.arange(0.1, 5, 0.1)

    elif "sin^-1" in a or "cos^-1" in a:
        n = np.linspace(-1, 1, 500)
        m = np.arange(-1, 1, 0.1)

    elif "tan^-1" in a:
        n = np.linspace(-np.pi / 2, np.pi / 2, 500)
        m = np.arange(-np.pi / 2, np.pi / 2, 0.1)

    elif "cot^-1" in a:
        n = np.linspace(-np.pi, np.pi, 500)
        m = np.arange(-np.pi, np.pi, 0.1)

    elif "csc^-1" in a:
        n = np.linspace(-np.pi / 2, np.pi / 2, 500)
        m = np.arange(-np.pi / 2, np.pi / 2, 0.1)

    elif "sec^-1" in a:
        n = np.linspace(-np.pi / 2, np.pi / 2, 500)
        m = np.arange(-np.pi / 2, np.pi / 2, 0.1)

    elif "sin" in a or "cos" in a or "tan" in a or "cot" in a or "sec" in a or "csc" in a:
        n = np.linspace(-10, 10, 1000)
        m = np.arange(-10, 10, 1)

    else:
        n = np.linspace(-100, 100, 1000)
        m = np.arange(-1000, 1000, 50)

    return [m, n]  

def graph_function_for_universal_functions(I):
    s = evaluate_math_expression_to_numpy(I)[0]
    m = evaluate_math_expression_to_numpy(I)[1]
    L = decide_range_of_function(I)

    if "[" in I:  
        I = I.replace("[", "|")
    
    if "]" in I:
        I = I.replace("]", "|")

    print("Displaying Numpy Expression: ")  
    print(s)
    x = L[1]  
    y = eval(s)  

    plt.plot(x, y, label = f'{I}')  
   
    plt.axhline(0, color='black', linewidth=1.5)  
    plt.axvline(0, color='black', linewidth=1.5)
   
    plt.xlabel('x')  
    plt.ylabel(f'{I}')
   
    plt.title(f'Graph of {I}')
    plt.xticks(L[0])  
    plt.grid()  
    plt.legend()  
    plt.show()  

def graph_function_for_polynomials(coefficients, final_exp):
    roots = np.roots(coefficients)  
    min_root = np.min(roots)  
    max_root = np.max(roots)  

    x = np.linspace(min_root - 1, max_root + 1, 1000)  #type:ignore
    y = np.polyval(coefficients, x)  

    plt.plot(x, y, label=f'f(x) = {final_exp}')  
    
    plt.axhline(0, color='black', linewidth=1.5)  
    plt.axvline(0, color='black', linewidth=1.5)  

    plt.xlabel('x')  
    plt.ylabel(f'{final_exp}')
    
    plt.title(f'Graph of {final_exp}')
    plt.ylim(bottom=min(plt.ylim()[0], -1))  
    plt.grid()  
    plt.legend()  
    plt.show()  

print("-" * 80)
print(pyfiglet.figlet_format("CALCULUS", font = "swamp_land"))
print("-" * 80)
print("                 CALCULUS AND GRAPH - FUNCTIONS' VIZUALIZATIONS")
print("-" * 80)
print("\nYou can view more information about this project (including VERSION HISTORY , CHANGELOGS and DOCUMENTATION) at https://github.com/Vaibhav1506/Calculus-Functions-Visualization-Python-MySql-Connectivity.")
print("\nPLEASE READ THE RULES CAREFULLY")
print("-"*50)
print(pyfiglet.figlet_format("RULES", font = "swamp_land"))
print("-"*50)
print("\n1. Please read each and every prompt or text message carefully so as to avoid an error.")
print("2. While taking input please use () parentheses to seperate the numerator and the denominator and other function types to avoid BODMAS/PEMDAS confusion. Use it as much as possible.")
print("3. While entering the values especially in the inverse trigonometric functions ensure that the values fall in their respective domains where they return a definite value and not an undefined one.")
print("4. If you want to give a fractional value please enter that value in decimals correct upto 3 decimal places.")
print("5. Only general linear and implicit functions are present in this program so as to avoid complications.")
print("6. If there is a message being displayed 'Code Terminated' then it either means that an invalid choice has been entered or the code was exited due to the choice of user.")
print("7. For entering trignometric functions with common prefixes / suffixes please use 'csc' for cosecant function to avoid confusion with secant's 'sec'.")
print("8  For exponentials use ^ sign.")
print("9. Modulus or Absolute Value Functions should be given using [] and not ||.")
print("10. GIF or Floor function should be represented within ⌊ ⌋ and SIF or ceiling function should be represented within ⌈ ⌉")
print("11. Polynomial Functions can be evaluated in both the choices given.")
print("12. The First one provides a better visualization of naive or simple functions and their roots.")
print("13. If a power's coefficient is missing or not defined then enter 0 while entering the coefficients. For example :- 5x^2 + 0x + 4")
print("14. The second one provides customization and using other functions implicitly in the polynomial ones.")
print("15. Complex or Special Functions like Lambert W, Riemann Zeta, Gamma functions & Factorial functions are not supported.")
print("16. While defining product between two functions or a constant and a function use * astrick marks. For example 2tan(x) should be written as 2 * tan(x) and sin(x)cos(x) should be written as sin(x) * cos(x).")
print("17. Function parameters or variables should be enclosed within parentheses().")
print("18. For Polynomial Functions where the roots of x are complex numbers it's recommended not to use it in the first choice.")

n = input("Make sure you have read the above mentioned rules. Press Y to proceed (Y/N): ")  

while n.upper() == "Y":
    print("Required for Database connection: (You may need to try one more time again if the first time does not works.)")

    try:
        return_system_info()

        host_name = input("Enter host name: ")
        user_name = input("Enter user name: ")
        passwd = masked_input("Enter password: ")
        
        print("\nChecking Compatibility ...")
        time.sleep(5)
        
        DB_object = DatabaseManager(host_name, user_name, passwd)
        DB_object.create_SQL_database()

        while True:  
            print("SELECT OPERATION TYPE")
            print("MAIN MENU:\n1.Differentiation\n2.Indefinite Integration\n3.Definite Integration\n4.Graphs\n5.Display\n6.Clear\n7.Open Help\n8.Exit")
            try:
                mappings = {  
                    "cos": r"\cos",  
                    "sin": r"\sin",  
                    "tan": r"\tan",  
                    "csc": r"\csc",
                    "sec": r"\sec",
                    "cot": r"\cot",
                    "log": r"\log",
                    "sin⁻¹": r"\sin^{-1}",
                    "cos⁻¹": r"\cos^{-1}",
                    "tan⁻¹": r"\tan^{-1}",
                    "cot⁻¹": r"\cot^{-1}",
                    "sec⁻¹": r"\sec^{-1}",
                    "csc⁻¹": r"\csc^{-1}",
                    "√": r"\sqrt",
                    "⁰": "0",
                    "¹": "1",
                    "²": "2",
                    "³": "3",
                    "⁴": "4",
                    "⁵": "5",
                    "⁶": "6",
                    "⁷": "7",
                    "⁸": "8",
                    "⁹": "9",
                    "ˣ": "x",
                    "⁺": "+",
                    "⁻": "-",
                    "⁼": "=",
                    "⁽": "(",
                    "⁾": ")",
                    "(": r"{(",
                    ")": r")}",
                    "(e": r"(\mathrm{e}^",
                }
                end_dt_month, start_dt_month, DT, ch1, ch2, ch3, func, func_1, func_type, inv, I, LHS = "", "", [], "-", "-", "-", "", "", "", '{}{}'.format(get_sup('-'), get_sup('1')), "", ""
                ch1 = int(input("Enter choice: "))
                
                if ch1 == 1:
                    function = ""
                    print("SELECT FUNCTION TYPE")
                    print("1. Trigonometric \n2. Inverse Trigonometric \n3. Polynomial \n4. Logarithmic \n5. Exponential")  

                    ch2 = int(input("Enter choice: "))
                    a = int(input("Enter value of a: "))
                    c = int(input("Enter value of c: "))

                    choice_type = ["Trigonometric", "Inverse Trigonometric", "Polynomial", "Logarithmic", "Exponential"]            
                    
                    if ch2 == 1:  
                        print("SELECT THE APPROPIATE FUNCTION")
                        print("MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. csc(ax+c)\n 6. sec(ax+c)")  
                        ch3 = int(input("Enter choice: "))
                        exp = f"{a}x+{c}"  

                        expressions_list = [r"\sin{(ax+c)}", r"\cos{(ax+c)}", r"\tan{(ax+c)}", r"\cot{(ax+c)}", r"\csc{(ax+c)}", r"\sec{(ax+c)}"]  
                        expression_list_2 = ["sin(ax+c)", "cos(ax+c)", "tan(ax+c)", "cot(ax+c)", "csc(ax+c)", "sec(ax+c)"]  
                        new_expressions_list = [i.replace("ax+c", exp) for i in expressions_list] 
                        new_expressions_list_2 = [i.replace("ax+c", exp) for i in expression_list_2]  

                        if ch3 == 1:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"{a}cos({exp})"
                        
                        elif ch3 == 2:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"-{a}sin({exp})"
                        
                        elif ch3 == 3:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"{a}sec²({exp})"
                        
                        elif ch3 == 4:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"-{a}csc²({exp})"
                        
                        elif ch3 == 5:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"-{a}csc({exp})cot({exp})"
                        
                        elif ch3 == 6:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"{a}sec({exp})tan({exp})"

                        function = new_expressions_list[ch3 - 1]  
                        func = new_expressions_list_2[ch3 - 1]  

                    elif ch2 == 2:  
                        print("SELECT THE APPROPIATE FUNCTION")
                        print(f"MENU:\n 1. sin{inv}(ax+c)\n 2. cos{inv}(ax+c)\n 3. tan{inv}(ax+c)\n 4. cot{inv}(ax+c)\n 5. csc{inv}(ax+c)\n 6. sec{inv}(ax+c)")  
                        ch3 = int(input("Enter choice: "))
                        exp = f"{a}x+{c}"  

                        expressions_list = [r"\sin^{-1}{(ax+c)}", r"\cos^{-1}{(ax+c)}", r"\tan^{-1}{(ax+c)}", r"\cot^{-1}{(ax+c)}", r"\csc^{-1}{(ax+c)}", r"\sec^{-1}{(ax+c)}"]  
                        expression_list_2 = [f"sin{inv}(ax+c)", f"cos{inv}(ax+c)", f"tan{inv}(ax+c)", f"cot{inv}(ax+c)", f"csc{inv}(ax+c)", f"sec{inv}(ax+c)"]  
                        new_expressions_list = [i.replace("ax+c", exp) for i in expressions_list]  
                        new_expressions_list_2 = [i.replace("ax+c", exp) for i in expression_list_2]
                
                        if ch3 == 1:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"{a}/√(1-({exp})²)"
                        
                        elif ch3 == 2:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"-{a}/√(1-({exp})²)"
                        
                        elif ch3 == 3:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"{a}/(1+({exp})²)"
                        
                        elif ch3 == 4:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"-{a}/(1+({exp})²)"
                        
                        elif ch3 == 5:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"-1/|x|√(({exp})²-1)"
                        
                        elif ch3 == 6:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"1/|x|√(({exp})²-1)"

                        function = new_expressions_list[ch3 - 1]  
                        func = new_expressions_list_2[ch3 - 1]  

                    elif ch2 == 3:  
                        exp = f"{a}x + {c}"                          
                        print("Record added to database.")
                        I = str(a)
                        function = exp 
                        func = exp  

                    elif ch2 == 4:  
                        exp = f"{a}x + {c}"
                        I = f"{a}/{a}x+{c}"
                        function = r"\log" + "{(" + exp + ")}"  
                        func = "log(ax+c)".replace("ax+c", exp)  

                    elif ch2 == 5:  
                        exp = f"{a}x + {c}"
                        I = f'{a}(e' + '{}{}{}{}{}{}'.format(get_sup('('), get_sup(str(a)), get_sup('x'), get_sup('+'), get_sup(str(c)), get_sup(')')) + ")" 
                        function = r"\mathrm{e}^{" + exp + "}"  
                        func = "e" + get_sup(exp)  

                    LHS = r"\dfrac{d}{dx} \left(" + " " + function + " " + r"\right) " + " " + "="  
                    func_type = choice_type[ch2 - 1]  
                    DT = get_date_time()  
                    
                elif ch1 == 2:
                    integrand = ""  
                    print("SELECT FUNCTION TYPE")
                    print("1. Trigonometric \n2. Inverse Trigonometric \n3. Polynomial \n4. Logarithmic \n5. Exponential")  

                    ch2 = int(input("Enter choice: "))
                    choice_type = ["Trigonometric", "Inverse Trigonometric", "Polynomial", "Logarithmic","Exponential"]  
                    
                    if ch2 == 1:  
                        a = int(input("Enter value of a: "))
                        c = int(input("Enter value of c: "))

                        print("SELECT THE APPROPIATE FUNCTION")
                        print(f"MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. csc(ax+c)\n 6. sec(ax+c)\n 7. sec(ax+c)tan(ax+c)\n 8. csc(ax+c)cot(ax+c)\n 9. csc{get_sup('2')}(ax+c)\n 10. sec{get_sup('2')}(ax+c)")
                        ch3 = int(input("Enter choice: "))

                        exp = f"{a}x+{c}"  
                        
                        expressions_list = [r"\sin{(ax+c)}", r"\cos{(ax+c)}", r"\tan{(ax+c)}", r"\cot{(ax+c)}", r"\csc{(ax+c)}", r"\sec{(ax+c)}", r"\sec{(ax+c)}\tan{(ax+c)}", r"\csc{(ax+c)}\cot{(ax+c)}", r"\csc^{2}{(ax+c)}", r"\sec^{2}{(ax+c)}"]  
                        expression_list_2 = ["sin(ax+c)", "cos(ax+c)", "tan(ax+c)", "cot(ax+c)", "csc(ax+c)", "sec(ax+c)", "sec(ax+c)tan(ax+c)", "csc(ax+c)cot(ax+c)", f"csc{get_sup('2')}(ax+c)", f"sec{get_sup('2')}(ax+c)"]  
                        new_expressions_list = [i.replace("ax+c", exp) for i in expressions_list]  
                        new_expressions_list_2 = [i.replace("ax+c", exp) for i in expression_list_2]  
                        
                        if ch3 == 1:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(-cos({exp})/{a}) + C"
                        
                        elif ch3 == 2:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(sin({exp})/{a}) + C"
                        
                        elif ch3 == 3:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(-log(|cos({exp})|)/{a}) + C"  
                        
                        elif ch3 == 4:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(log(|sin({exp})|)/{a}) + C"  
                        
                        elif ch3 == 5:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(-log(|csc({exp}) + cot({exp})|)/{a}) + C"
                        
                        elif ch3 == 6:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(-log(|tan({exp}) + sec({exp})|)/{a}) + C"
                        
                        elif ch3 == 7:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(sec({exp})/{a}) + C"
                        
                        elif ch3 == 8:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(-csc({exp})/{a}) + C"
                        
                        elif ch3 == 9:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(-cot({exp})/{a}) + C"
                        
                        elif ch3 == 10:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(tan({exp})/{a}) + C"

                        integrand = new_expressions_list[ch3 - 1]  
                        func = new_expressions_list_2[ch3 - 1]  

                    elif ch2 == 2:  
                        print("SELECT THE APPROPIATE FUNCTION")
                        print(f"MENU:\n 1. 1/√(1 - (ax + c){get_sup('2')})\n 2. -1/√(1 - (ax+c){get_sup('2')})\n 3. 1/(b + (ax+c){get_sup('2')})\n 4. -1/(b + (ax+c){get_sup('2')})\n 5. 1/((ax+c)√((ax+c){get_sup('2')} - 1)\n 6. -1/((ax+c)√((ax+c){get_sup('2')}) - 1")

                        a = int(input("Enter value of a: "))
                        c = int(input("Enter value of c: "))
                        b = int(input("Enter value of b (valid only for 3. and 4.):"))  
                        ch3 = int(input("Enter choice: "))
                        exp = f"{a}x+{c}"  

                        expressions_list = [r"\dfrac{1}{\sqrt{1 - (ax + c)^{2}}}", r"\dfrac{-1}{\sqrt{1 - (ax + c)^{2}}}", r"\dfrac{1}{b + (ax + c)^{2}}", r"\dfrac{-1}{b + (ax + c)^{2}}", r"\dfrac{1}{(ax + c)\sqrt{(ax + c)^2 - 1}}", r"\dfrac{-1}{(ax + c)\sqrt{(ax + c)^2 - 1}}"]  
                        expression_list_2 = [f"1/√(1 - (ax + c){get_sup('2')})", f"-1/√(1 - (ax + c){get_sup('2')})", f"1/(b + (ax + c){get_sup('2')})", f"-1/(b + (ax + c){get_sup('2')})", f"1/((ax + c)√((ax + c){get_sup('2')} - 1)", f"-1/((ax + c)√((ax + c){get_sup('2')}) - 1"]  
                        new_expressions_list = [i.replace("ax + c",exp) for i in expressions_list]  
                        new_expressions_list_2 = [k.replace("ax + c",exp) for k in expression_list_2]
                        final_expressions_list = [j.replace("b",f"{b}") for j in new_expressions_list]
                        final_expressions_list_2 = [l.replace("b",f"{b}") for l in new_expressions_list_2]
                        
                        if ch3 == 1:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(sin{inv}({exp})/{a}) + C"
                        
                        elif ch3 == 2:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(cos{inv}({exp})/{a}) + C"
                        
                        elif ch3 == 3:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(tan{inv}(({exp})/√({b}))/({a}√({b}))) + C"
                        
                        elif ch3 == 4:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(cot{inv}(({exp})/√({b}))/({a}√({b}))) + C"
                        
                        elif ch3 == 5:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(sec{inv}({exp})/{a}) + C"
                        
                        elif ch3 == 6:
                            func = new_expressions_list_2[ch3 - 1]  
                            I = f"(csc{inv}({exp})/{a}) + C"

                        integrand = final_expressions_list[ch3 - 1]  
                        func = final_expressions_list_2[ch3 - 1]  

                    elif ch2 == 3:  
                        a = int(input("Enter value of a: "))
                        c = int(input("Enter value of c: "))
                        integrand = f"{a}x + {c}"                          
                        I = f"{int(a / 2) if a % 2 == 0 else (a / 2)}x{get_sup(str(2))} + {c}x + C"  
                        func = integrand  

                    elif ch2 == 4:  
                        print("SELECT THE APPROPIATE FUNCTION")
                        print(f"MENU:\n1. log(ax + c) \n2. 1/(ax + c) \n3. a{get_sup('x')}")
                        ch3 = int(input("Enter choice: "))
                        a = int(input("Enter value of a: "))
                        c = int(input("Enter value of c (only for 1. and 2.): "))
                        exp = f"{a}x+{c}"  

                        expressions_list = [r"\log{(ax + c)}", r"\dfrac{1}{(ax + c)}", r"a^{x}"]  
                        expression_list_2 = ["log(ax + c)", "1/(ax + c)", f"a{get_sup('x')}"]  
                        new_expressions_list = [i.replace("ax + c", exp) for i in expressions_list]
                        new_expressions_list[2] = new_expressions_list[2].replace("a", f"{a}")
                        new_expressions_list_2 = [j.replace("ax + c", exp) for j in expression_list_2]  
                        new_expressions_list_2[2] = new_expressions_list_2[2].replace("a", f"{a}")
                        
                        if ch3 == 1:
                            func = new_expressions_list_2[ch3 - 1]
                            I = f"((({exp})(log({exp})-1))/{a}) + C"
                        
                        elif ch3 == 2:
                            func = new_expressions_list_2[ch3 - 1]
                            I = f"(log(|({exp})|)/{a}) + C"
                        
                        elif ch3 == 3:
                            func = new_expressions_list_2[ch3 - 1]
                            I = f"({a}{get_sup('x')}/log({a})) + C"

                        integrand = new_expressions_list[ch3 - 1]
                        func = new_expressions_list_2[ch3 - 1]

                    elif ch2 == 5:  
                        a = int(input("Enter value of a: "))
                        c = int(input("Enter value of c: "))
                        exp = f"{a}x + {c}"
                        I = '((e' + f'{get_sup("(")}' + f'{get_sup(exp)}' + f'{get_sup(")")}' + f")/{a}) + C"  
                        int_integrand = r"\mathrm{e}^{ax + c}"  
                        integrand = int_integrand.replace("ax + c", exp)  
                        func = "e" + get_sup(exp)  

                    LHS = r"\int \left(" + " " + integrand + " " + r"\right) \, dx" + " " + "="  
                    func_type = choice_type[ch2 - 1]  
                    DT = get_date_time()  

                elif ch1 == 3:
                    integrand = ""
                    print("SELECT FUNCTION TYPE")
                    print("1.Trigonometric\n2.Inverse Trigonometric\n3.Polynomial\n4.Logarithmic\n5.Exponential")

                    ch2 = int(input("Enter choice: "))
                    a = int(input("Enter value of a: "))
                    c = int(input("Enter value of c: "))

                    lwr_bound = int(input("Enter lower bound: "))  
                    upr_bound = int(input("Enter upper bound: "))  

                    choice_type = ["Trigonometric", "Inverse Trigonometric", "Polynomial", "Logarithmic", "Exponential"]      
                    
                    if ch2 == 1:  
                        print("SELECT APPROPIATE FUNCTION")
                        print("MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. csc(ax+c)\n 6. sec(ax+c)\n 7. sec(ax+c)tan(ax+c)\n 8. csc(ax+c)cot(ax+c)\n 9. csc\u00b2(ax+c)\n 10. sec\u00b2(ax+c)")
                        ch3 = int(input("Enter choice: "))
                        exp = f"{a}x + {c}"
                        exp_lwr = (a * lwr_bound) + c  
                        exp_upr = (a * upr_bound) + c  

                        expressions_list = [r"\sin{(ax+c)}", r"\cos{(ax+c)}", r"\tan{(ax+c)}", r"\cot{(ax+c)}", r"\csc{(ax+c)}", r"\sec{(ax+c)}", r"\sec{(ax+c)}\tan{(ax+c)}",r"\csc{(ax+c)}\cot{(ax+c)}", r"\csc^{2}{(ax+c)}", r"\sec^{2}{(ax+c)}"]  
                        expression_list_2 = ["sin(ax+c)", "cos(ax+c)", "tan(ax+c)", "cot(ax+c)", "csc(ax+c)", "sec(ax+c)", "sec(ax+c)tan(ax+c)", "csc(ax+c)cot(ax+c)", "csc\u00b2(ax+c)\n 10. sec\u00b2(ax+c)"]  
                        new_expressions_list = [i.replace("ax+c", exp) for i in expressions_list]  
                        new_expressions_list_2 = [i.replace("ax+c", exp) for i in expression_list_2 ]  
                        
                        if ch3 == 1:  
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            I = (-math.cos(exp_upr) / a) - (-math.cos(exp_lwr) / a)
                        
                        elif ch3 == 2:
                            func_1 = new_expressions_list_2[ch3 - 1]                              
                            I = (math.sin(exp_upr) / a) - (math.sin(exp_lwr) / a)
                        
                        elif ch3 == 3:
                            func_1 = new_expressions_list_2[ch3 - 1]           
                            I = (-math.log(abs(math.cos(exp_upr))) / a) - (-math.log(abs(math.cos(exp_lwr))) / a)
                        
                        elif ch3 == 4:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            I = (math.log(abs(math.sin(exp_upr))) / a) - (math.log(abs(math.sin(exp_lwr))) / a)
                        
                        elif ch3 == 5:
                            func_1 = new_expressions_list_2[ch3 - 1]                              
                            I = (-math.log(abs(1 / math.sin(exp_upr) + 1 / math.tan(exp_upr))) / a) - (-math.log(abs(1 / math.sin(exp_lwr) + 1 / math.tan(exp_lwr))) / a)
                        
                        elif ch3 == 6:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            I = (-math.log(abs((math.tan(exp_upr) + 1 / math.cos(exp_upr)))) / a) - (-math.log(abs((math.tan(exp_lwr) + 1 / math.cos(exp_lwr)))) / a)
                        
                        elif ch3 == 7:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            I = (1 / math.cos(exp_upr) / a) - (1 / math.cos(exp_lwr) / a)
                        
                        elif ch3 == 8:
                            func_1 = new_expressions_list_2[ch3 - 1]            
                            I = (-1 / math.sin(exp_upr) / a) - (-1 / math.sin(exp_lwr) / a)
                        
                        elif ch3 == 9:
                            func_1 = new_expressions_list_2[ch3 - 1]           
                            I = (-1 / math.tan(exp_upr) / a) - (-1 / math.tan(exp_lwr) / a)
                        
                        elif ch3 == 10:
                            func_1 = new_expressions_list_2[ch3 - 1] 
                            I = (math.tan(exp_upr) / a) - (math.tan(exp_lwr) / a)

                        integrand = new_expressions_list[ch3 - 1]  
                        func_1 = new_expressions_list_2[ch3 - 1]  

                    elif ch2 == 2:  
                        print("SELECT APPROPIATE FUNCTION")
                        print("MENU:\n 1. 1/√(1 - (ax + c)\u00b2)\n 2. -1/√(1 - (ax + c)\u00b2)\n 3. 1/(b + (ax + c)\u00b2)\n 4. -1/(b + (ax + c)\u00b2)\n 5. 1/((ax + c)√((ax + c)\u00b2 - 1)\n 6. -1/((ax + c)√((ax + c)\u00b2) - 1")
                        b = int(input("Enter value of b (valid only for 3. and 4.):"))
                        ch3 = int(input("Enter choice: "))
                        exp_lwr = (a * lwr_bound) + c  
                        exp_upr = (a * upr_bound) + c  
                        exp = f"{a}x + {c}"  

                        expressions_list = [r"\dfrac{1}{\sqrt{1 - (ax + c)^{2}}}", r"\dfrac{-1}{\sqrt{1 - (ax + c)^{2}}}", r"\dfrac{1}{b + (ax + c)^{2}}", r"\dfrac{-1}{b + (ax + c)^{2}}", r"\dfrac{1}{(ax + c)\sqrt{(ax + c)^2 - 1}}", r"\dfrac{-1}{(ax + c)\sqrt{(ax + c)^2 - 1}}"]  
                        expression_list_2 = ["1/√(1 - (ax + c)\u00b2)", "-1/√(1 - (ax + c)\u00b2)", "1/(b + (ax + c)\u00b2)", "-1/(b + (ax + c)\u00b2)", "1/((ax + c)√((ax + c)\u00b2 - 1)", "-1/((ax + c)√((ax + c)\u00b2) - 1"]  
                        new_expressions_list = [i.replace("ax + c", exp) for i in expressions_list]  
                        new_expressions_list_2 = [k.replace("ax + c", exp) for k in expression_list_2]
                        final_expressions_list = [j.replace("b", f"{b}") for j in new_expressions_list]
                        final_expressions_list_2 = [l.replace("b", f"{b}") for l in new_expressions_list_2]
                        
                        if ch3 == 1:  
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            I = (math.asin(exp_upr) / a) - (math.asin(exp_lwr) / a)
                        
                        elif ch3 == 2:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            I = -(math.acos(exp_upr) / a) - -(math.acos(exp_lwr) / a)
                        
                        elif ch3 == 3:
                            func_1 = new_expressions_list_2[ch3 - 1]    
                            I = (math.atan((exp_upr) / math.sqrt(b)) / (a * math.sqrt(b))) - (math.atan((exp_lwr) / math.sqrt(b)) / (a * math.sqrt(b)))
                        
                        elif ch3 == 4:
                            func_1 = new_expressions_list_2[ch3 - 1]      
                            I = (math.atan(math.sqrt(b) / (exp_upr)) / (a * math.sqrt(b))) - (math.atan(math.sqrt(b) / (exp_lwr)) / (a * math.sqrt(b)))  
                        
                        elif ch3 == 5:
                            func_1 = new_expressions_list_2[ch3 - 1]    
                            I = (math.acos(1 / exp_upr) / a) - (math.acos(1 / exp_lwr) / a)  
                        
                        elif ch3 == 6:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            I = (math.asin(1 / exp_upr) / a) - (math.asin(1 / exp_lwr) / a)  

                        integrand = final_expressions_list[ch3 - 1]  
                        func_1 = new_expressions_list_2[ch3 - 1]  

                    elif ch2 == 3:  
                        integrand = f"{a}x + {c}"  
                        func_1 = integrand                          
                        I = ((a / 2) * ((upr_bound ** 2) - (lwr_bound ** 2))) + c * (upr_bound - lwr_bound)

                    elif ch2 == 4:  
                        print("SELECT APPROPIATE FUNCTION")
                        print(f"MENU:\n1. log(ax + c) \n2. 1/(ax + c) \n3. a{get_sup('x')}")
                        ch3 = int(input("Enter choice: "))

                        exp = f"{a}x + {c}"
                        exp_lwr = (a * lwr_bound) + c  
                        exp_upr = (a * upr_bound) + c  

                        expressions_list = [r"\log{(ax + c)}", r"\dfrac{1}{(ax + c)}", r"a^{x}"]  
                        expression_list_2 = ["log(ax + c)", "1/(ax + c)", f"a{get_sup('x')}"]  
                        new_expressions_list = [i.replace("ax + c", exp)  for i in expressions_list]  
                        new_expressions_list[2] = new_expressions_list[2].replace("a", f"{a}")  
                        new_expressions_list_2 = [j.replace("ax + c", exp) for j in expression_list_2]  
                        new_expressions_list_2[2] = new_expressions_list_2[2].replace("a", f"{a}")  
                        
                        if ch3 == 1:  
                            func_1 = new_expressions_list_2[ch3 - 1]                  
                            I = (((exp_upr) * (math.log(exp_upr) - 1)) / a) - (((exp_lwr) * (math.log(exp_lwr) - 1)) / a)
                        
                        elif ch3 == 2:
                            func_1 = new_expressions_list_2[ch3 - 1]                   
                            I = (math.log(abs(exp_upr)) / a) - (math.log(abs(exp_lwr)) / a)
                        
                        elif ch3 == 3:
                            func_1 = new_expressions_list_2[ch3 - 1]   
                            I = (math.pow(a, upr_bound) / math.log(a)) - (math.pow(a, lwr_bound) / math.log(a))

                        integrand = new_expressions_list[ch3 - 1]  
                        func_1 = new_expressions_list_2[ch3 - 1]  

                    elif ch2 == 5:  
                        exp = f"{a}x + {c}"
                        exp_lwr = (a * lwr_bound) + c  
                        exp_upr = (a * upr_bound) + c  
                        func_1 = "e" + get_sup(exp)                          
                        I = ((math.pow((math.e), exp_upr)) / (a)) - ((math.pow((math.e), exp_lwr)) / (a))
                        int_integrand = r"\mathrm{e}^{ax + c}"  
                        integrand = int_integrand.replace("ax + c", exp)  

                    LHS_int = r"\int_{lwr_bound}^{upr_bound} \left(" + " " + integrand + " " + r"\right) \, dx" + " " + "= $"  
                    LHS_mod = LHS_int.replace("lwr_bound", f"{lwr_bound}")  
                    LHS = LHS_mod.replace("upr_bound", f"{upr_bound}")  
                    func = func_1 + f" from {lwr_bound} to {upr_bound}"  
                    func_type = choice_type[ch2 - 1]  
                    DT = get_date_time()

                elif ch1 == 4:
                    print("MENU")  
                    print("1. Polynomial Function (recommended for better visualization of Polynomial Functions)")
                    print("2. Other Functions (Trigonometric, Inverse, Exponential, etc.)")

                    ch2 = int(input("Enter choice: "))
                    choice_type = ["Polynomial Function", "Basic Mathematical Function"]

                    if ch2 == 1:  
                        deg = int(input("Enter degree (highest power of polynomial): "))  
                        coefficients = []  
                        st = ""

                        for i in range(deg, 0, -1):  
                            coeff = int(input(f"Enter the coefficient of x^{i} : "))  
                            st += str(coeff) + f"x^{i} + "  
                            coefficients.append(coeff)  

                        const = int(input("Enter constant (last number) of polynomial: "))  
                        coefficients.append(const)  

                        I = st + str(const)  

                        graph_function_for_polynomials(coefficients, I)

                    elif ch2 == 2:  
                        I = input("Enter the function: ")  
                        graph_function_for_universal_functions(I)  

                    else:
                        print("Invalid Choice.")  

                    func_type = choice_type[ch2 - 1]  
                    DT = get_date_time()

                elif ch1 == 5:  
                    DB_object.execute_SQL_choices(ch1)
                
                elif ch1 == 6:
                    DB_object.execute_SQL_choices(ch1)
                
                elif ch1 == 7:
                    open_help()

                elif ch1 == 8:
                    print("Exiting ... ")
                    os._exit(0)
                
                else:
                    print("Invalid Choice. Please try again.")
        
                if ch1 in range(1, 6):

                    if I != "":
                        print("Displaying Latest Mathematical Notation ...")
                        print("Answer:", I)
                        L = []
                        
                        if ch1 == 1:
                            L = ["Differentiation", ch1 , func_type, ch2 , func, ch3, I, DT[0], DT[1]]
                        
                        elif ch1 == 2:
                            L = ["Indefinite Integration", ch1 , func_type, ch2 ,func, ch3,  I, DT[0], DT[1]]
                        
                        elif ch1 == 3:
                            L = ["Definite Integration", ch1 , func_type, ch2,  func, ch3, I, DT[0], DT[1]]
                        
                        elif ch1 == 4:
                            L = ["Graph", func_type, ch1,  I, ch2 , "-", I, DT[0], DT[1]]

                        DB_object.insert_into_SQL_database(L)
 
                    else:
                        print("Displaying latest mathematical notation evaluated ...")
                        print("No Mathematical Expression has been evaluated since user has not entered any expression.")  

                    if ch1 == 1:  
                        print("Displaying Latex Notation ... ")

                        RHS = convert_to_Latex_for_differentials(I, mappings)[1:]  
                        final_exp = "$" + LHS + " " + RHS  

                        display_Latex(final_exp)  

                    elif ch1 == 2 or ch1 == 3:  
                        print("Displaying LaTeX Notation ...")

                        if type(I) == int or type(I) == float:  
                            RHS = str(I)  
                        
                        else:
                            RHS = convert_to_Latex_for_integrals(I, mappings)[1:]  
                            
                        final_exp = "$" + LHS + " " + RHS  
                        
                        display_Latex(final_exp)  

            except (ValueError, KeyboardInterrupt, ZeroDivisionError, UnboundLocalError, NameError) as e:  
                print(e)

    except (UnboundLocalError, ValueError, KeyboardInterrupt, NameError) as e:
        print("Unexpected Error occured. Please try again.")
        print("Error encountered :", str(e))
        os._exit(0)

else:
    print("Code Exited due to non - agreement of user.")