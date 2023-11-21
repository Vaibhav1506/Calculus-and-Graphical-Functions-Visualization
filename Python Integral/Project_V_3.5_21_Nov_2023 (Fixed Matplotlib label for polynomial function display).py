import matplotlib.pyplot as plt, numpy as np, math, mysql.connector as mc, os   #type:ignore

def create_SQL_database(host_name, user_name, password):
    try:
        print("Connecting to the MySQL Database ... ")

        obj = mc.connect(host = host_name, user = user_name, passwd = password)

        if not obj.is_connected():
            print("Failed to connect to database.")
        else:
            print("Connected successfully. Database has been created.")

        co = obj.cursor()
        co.execute("CREATE DATABASE IF NOT EXISTS calculus_DB;")
        co.execute("USE calculus_DB;")
        co.execute("CREATE TABLE IF NOT EXISTS Calculus_User_History (`Operation Type` VARCHAR(100) ,`Operation Type Choice` VARCHAR(100) ,`Function Type` VARCHAR(100) ,`Function Type Choice` VARCHAR(100) ,`Function Expression` VARCHAR(100) , `Function Expression Choice` VARCHAR(100) , `Answer` VARCHAR(100) UNIQUE);")
        obj.commit()  

    except mc.Error as e:
        print("Can't connect to database. Checking for Errors ...")
        print("Error encountered was: ", str(e))
        print("Exiting code ...")
        os._exit(0)
    
    finally:
        co.close()  #type:ignore
        obj.close()   #type:ignore

def insert_into_SQL_database(host_name, user_name, password, L):
    try:
        obj = mc.connect(host = host_name, user = user_name, passwd = password, database = "calculus_DB")
        co = obj.cursor()
        sql = "INSERT INTO Calculus_User_History (`Operation Type`, `Operation Type Choice`, `Function Type`, `Function Type Choice`, `Function Expression`, `Function Expression Choice`, `Answer`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (L[0], L[1], L[2], L[3], L[4], L[5], L[6])
        co.execute(sql, values)
        obj.commit()  
    
    except mc.Error:
        pass

    finally:
        co.close()  #type:ignore
        obj.close()  #type:ignore

def check_duplicates(x, host_name, user_name, password):
    obj = mc.connect(host=host_name, user=user_name, passwd=password, database="calculus_DB")
    co = obj.cursor()
    table = []
    query = "SELECT * FROM Calculus_User_History"
    co.execute(query)
    table = co.fetchall()
    
    C, ans = 0, ""
    
    for row in table:
        if x == row[4]:
            ans = row[6]
            C += 1
            break 

    return [C, ans]

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

    x = np.linspace(min_root - 1, max_root + 1, 1000)  
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
print("CALCULUS AND GRAPH - FUNCTIONS VIZUALIZATION PYTHON - MYSQL CONNECTIVITY PROJECT")
print("-" * 80)
print("1. While taking input use () parentheses to seperate the numerator and the denominator and other function types to avoid BEDMAS confusion.")
print("2. While entering the values ensure that the values fall in their respective domains where they return a defined value.")
print("3. If you want to give a fractional value enter that value in decimals correct upto 3 decimal places.")
print("4. Only general linear and implicit functions are present in this program so as to avoid complications.")
print("5. For entering trignometric functions use 'csc' for cosecant function.")
print("6  For exponentials use ^ sign.")
print("7. Modulus or Absolute Value Functions should be given using [] and not ||.")
print("8. GIF or Floor function should be represented within ⌊ ⌋ and SIF or ceiling function should be represented within ⌈ ⌉")
print("9. While entering implicit functions make sure they are closed within (). For example for |sin|x|| we have to enter [sin([x])].")
print("10. Polynomial Functions can be evaluated in both the choices given.")
print("11. The First one provides a better visualization of naïve or simple functions and their roots.")
print("12. If a power's coefficient is missing or not defined then enter 0 while entering the coefficients.")
print("13. The second one provides customization and using other functions implicitly in the polynomial ones.")
print("14. Complex or Special Functions like Lambert W, Riemann Zeta, Gamma functions & Factorial functions are not supported.")
print("15. While defining product between two functions or a constant and a function use * asterisk marks.")
print("16. For Polynomial Functions where the roots of x are complex numbers it's recommended not to use it in the first choice.")


n = input("Make sure you have read the above mentioned rules. Press Y to proceed (Y/N): ")  

while n.upper() == "Y":
    print("Required for Database connection: (You may need to try one more time again if the first time does not works.)")

    try:
        host_name = input("Enter host name: ")
        user_name = input("Enter user name: ")
        passwd = input("Enter password: ")
        
        create_SQL_database(host_name, user_name, passwd)

        while True:  
            print("SELECT OPERATION TYPE")
            print("MAIN MENU:\n1.Differentiation\n2.Indefinite Integration\n3.Definite Integration\n4.Graphs\n5.Exit")  

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
                ch1, ch2, ch3, func, func_1, func_type, inv, I, LHS = "-", "-", "-", "", "", "", '{}{}'.format(get_sup('-'), get_sup('1')), "", ""
                ch1 = int(input("Enter choice: "))
                
                if ch1 == 1:
                    function = ""
                    print("SELECT FUNCTION TYPE")
                    print("1. Trigonometric \n2. Inverse Trigonometric \n3. Polyomial \n4. Logarithmic \n5. Exponential")  

                    ch2 = int(input("Enter choice: "))
                    a = int(input("Enter value of a: "))
                    c = int(input("Enter value of c: "))

                    choice_type = ["Trigonometric", "Inverse Trigonometric", "Polyomial", "Logarithmic", "Exponential"]            
                    
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
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]                            
                            else:
                                print("Record added to database.")
                                I = f"{a}cos({exp})"
                        
                        elif ch3 == 2:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"-{a}sin({exp})"
                        
                        elif ch3 == 3:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"{a}sec²({exp})"
                        
                        elif ch3 == 4:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"-{a}csc²({exp})"
                        
                        elif ch3 == 5:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"-{a}csc({exp})cot({exp})"
                        
                        elif ch3 == 6:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
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
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"{a}/√(1-({exp})²)"
                        
                        elif ch3 == 2:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"-{a}/√(1-({exp})²)"
                        
                        elif ch3 == 3:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"{a}/(1+({exp})²)"
                        
                        elif ch3 == 4:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"-{a}/(1+({exp})²)"
                        
                        elif ch3 == 5:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"-1/|x|√(({exp})²-1)"
                        
                        elif ch3 == 6:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"1/|x|√(({exp})²-1)"

                        function = new_expressions_list[ch3 - 1]  
                        func = new_expressions_list_2[ch3 - 1]  

                    elif ch2 == 3:  
                        exp = f"{a}x + {c}"
                        func = exp  
                        
                        if check_duplicates(function, host_name, user_name, passwd)[0] == 1:
                            print("Record fetched from database")
                            I = check_duplicates(function, host_name, user_name, passwd)[1]   
                        else:
                            print("Record added to database.")
                            I = str(a)
                        
                        function = exp  
                        func = exp  

                    elif ch2 == 4:  
                        exp = f"{a}x + {c}"
                        func = "log(ax+c)".replace("ax+c", exp)  
                        
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            print("Record fetched from database")
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            print("Record added to database.")
                            I = f"{a}/{a}x+{c}"
                        
                        function = r"\log" + "{(" + exp + ")}"  
                        func = "log(ax+c)".replace("ax+c", exp)  

                    elif ch2 == 5:  
                        exp = f"{a}x + {c}"
                        func = "e" + get_sup(exp)  
                        
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            print("Record fetched from database")
                            I = check_duplicates(func, host_name, user_name, passwd)[1]             
                        else:
                            print("Record added to database.")
                            I = f'{a}(e' + '{}{}{}{}{}{}'.format(get_sup('('), get_sup(str(a)), get_sup('x'), get_sup('+'), get_sup(str(c)), get_sup(')')) + ")"  
                        
                        function = r"\mathrm{e}^{" + exp + "}"  
                        func = "e" + get_sup(exp)  

                    LHS = r"\dfrac{d}{dx} \left(" + " " + function + " " + r"\right) " + " " + "="  
                    func_type = choice_type[ch2 - 1]  

                elif ch1 == 2:
                    integrand = ""  

                    print("SELECT FUNCTION TYPE")
                    print("1. Trigonometric \n2. Inverse Trigonometric \n3. Polyomial \n4. Logarithmic \n5. Exponential")  

                    ch2 = int(input("Enter choice: "))
                    choice_type = ["Trigonometric", "Inverse Trigonometric", "Polyomial", "Logarithmic","Exponential"]  
                    
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
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(-cos({exp})/{a}) + C"
                        
                        elif ch3 == 2:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(sin({exp})/{a}) + C"
                        
                        elif ch3 == 3:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(-log(|cos({exp})|)/{a}) + C"  
                        
                        elif ch3 == 4:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(log(|sin({exp})|)/{a}) + C"  
                        
                        elif ch3 == 5:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(-log(|csc({exp}) + cot({exp})|)/{a}) + C"
                        
                        elif ch3 == 6:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(-log(|tan({exp}) + sec({exp})|)/{a}) + C"
                        
                        elif ch3 == 7:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(sec({exp})/{a}) + C"
                        
                        elif ch3 == 8:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(-csc({exp})/{a}) + C"
                        
                        elif ch3 == 9:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(-cot({exp})/{a}) + C"
                        
                        elif ch3 == 10:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
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
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(sin{inv}({exp})/{a}) + C"
                        
                        elif ch3 == 2:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(cos{inv}({exp})/{a}) + C"
                        
                        elif ch3 == 3:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(tan{inv}(({exp})/√({b}))/({a}√({b}))) + C"
                        
                        elif ch3 == 4:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(cot{inv}(({exp})/√({b}))/({a}√({b}))) + C"
                        
                        elif ch3 == 5:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(sec{inv}({exp})/{a}) + C"
                        
                        elif ch3 == 6:
                            func = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(csc{inv}({exp})/{a}) + C"

                        integrand = final_expressions_list[ch3 - 1]  
                        func = final_expressions_list_2[ch3 - 1]  

                    elif ch2 == 3:  
                        a = int(input("Enter value of a: "))
                        c = int(input("Enter value of c: "))
                        integrand = f"{a}x + {c}"  
                        func = integrand  
                        
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            print("Record fetched from database.")
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            print("Record added to database.")
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
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"((({exp})(log({exp})-1))/{a}) + C"
                        
                        elif ch3 == 2:
                            func = new_expressions_list_2[ch3 - 1]
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"(log(|({exp})|)/{a}) + C"
                        
                        elif ch3 == 3:
                            func = new_expressions_list_2[ch3 - 1]
                            if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = f"({a}{get_sup('x')}/log({a})) + C"

                        integrand = new_expressions_list[ch3 - 1]
                        func = new_expressions_list_2[ch3 - 1]

                    elif ch2 == 5:  
                        a = int(input("Enter value of a: "))
                        c = int(input("Enter value of c: "))
                        exp = f"{a}x + {c}"
                        func = "e" + get_sup(exp)  

                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            print("Record fetched from database.")
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            print("Record added to database.")
                            I = '((e' + f'{get_sup("(")}' + f'{get_sup(exp)}' + f'{get_sup(")")}' + f")/{a}) + C"  

                        int_integrand = r"\mathrm{e}^{ax + c}"  
                        integrand = int_integrand.replace("ax + c", exp)  
                        func = "e" + get_sup(exp)  

                    LHS = r"\int \left(" + " " + integrand + " " + r"\right) \, dx" + " " + "="  
                    func_type = choice_type[ch2 - 1]  
                
                elif ch1 == 3:
                    integrand = ""
                    print("SELECT FUNCTION TYPE")
                    print("1.Trigonometric\n2.Inverse Trigonometric\n3.Polyomial\n4.Logarithmic\n5.Exponential")

                    ch2 = int(input("Enter choice: "))
                    a = int(input("Enter value of a: "))
                    c = int(input("Enter value of c: "))

                    lwr_bound = int(input("Enter lower bound: "))  
                    upr_bound = int(input("Enter upper bound: "))  

                    choice_type = ["Trigonometric", "Inverse Trigonometric", "Polyomial", "Logarithmic", "Exponential"]      
                    
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
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (-math.cos(exp_upr) / a) - (-math.cos(exp_lwr) / a)
                        
                        elif ch3 == 2:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (math.sin(exp_upr) / a) - (math.sin(exp_lwr) / a)
                        
                        elif ch3 == 3:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (-math.log(abs(math.cos(exp_upr))) / a) - (-math.log(abs(math.cos(exp_lwr))) / a)
                        
                        elif ch3 == 4:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (math.log(abs(math.sin(exp_upr))) / a) - (math.log(abs(math.sin(exp_lwr))) / a)
                        
                        elif ch3 == 5:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (-math.log(abs(1 / math.sin(exp_upr) + 1 / math.tan(exp_upr))) / a) - (-math.log(abs(1 / math.sin(exp_lwr) + 1 / math.tan(exp_lwr))) / a)
                        
                        elif ch3 == 6:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (-math.log(abs((math.tan(exp_upr) + 1 / math.cos(exp_upr)))) / a) - (-math.log(abs((math.tan(exp_lwr) + 1 / math.cos(exp_lwr)))) / a)
                        
                        elif ch3 == 7:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (1 / math.cos(exp_upr) / a) - (1 / math.cos(exp_lwr) / a)
                        
                        elif ch3 == 8:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (-1 / math.sin(exp_upr) / a) - (-1 / math.sin(exp_lwr) / a)
                        
                        elif ch3 == 9:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (-1 / math.tan(exp_upr) / a) - (-1 / math.tan(exp_lwr) / a)
                        
                        elif ch3 == 10:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
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
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (math.asin(exp_upr) / a) - (math.asin(exp_lwr) / a)
                        
                        elif ch3 == 2:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = -(math.acos(exp_upr) / a) - -(math.acos(exp_lwr) / a)
                        
                        elif ch3 == 3:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (math.atan((exp_upr) / math.sqrt(b)) / (a * math.sqrt(b))) - (math.atan((exp_lwr) / math.sqrt(b)) / (a * math.sqrt(b)))
                        
                        elif ch3 == 4:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (math.atan(math.sqrt(b) / (exp_upr)) / (a * math.sqrt(b))) - (math.atan(math.sqrt(b) / (exp_lwr)) / (a * math.sqrt(b)))  
                        
                        elif ch3 == 5:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (math.acos(1 / exp_upr) / a) - (math.acos(1 / exp_lwr) / a)  
                        
                        elif ch3 == 6:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (math.asin(1 / exp_upr) / a) - (math.asin(1 / exp_lwr) / a)  

                        integrand = final_expressions_list[ch3 - 1]  
                        func_1 = new_expressions_list_2[ch3 - 1]  

                    elif ch2 == 3:  
                        integrand = f"{a}x + {c}"  
                        func_1 = integrand  
                        
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            print("Record fetched from database.")
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            print("Record added to database.")
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
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (((exp_upr) * (math.log(exp_upr) - 1)) / a) - (((exp_lwr) * (math.log(exp_lwr) - 1)) / a)
                        
                        elif ch3 == 2:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (math.log(abs(exp_upr)) / a) - (math.log(abs(exp_lwr)) / a)
                        
                        elif ch3 == 3:
                            func_1 = new_expressions_list_2[ch3 - 1]  
                            if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                                print("Record fetched from database.")
                                I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                            else:
                                print("Record added to database.")
                                I = (math.pow(a, upr_bound) / math.log(a)) - (math.pow(a, lwr_bound) / math.log(a))

                        integrand = new_expressions_list[ch3 - 1]  
                        func_1 = new_expressions_list_2[ch3 - 1]  

                    elif ch2 == 5:  
                        exp = f"{a}x + {c}"
                        exp_lwr = (a * lwr_bound) + c  
                        exp_upr = (a * upr_bound) + c  
                        func_1 = "e" + get_sup(exp)  
                        
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            print("Record fetched from database.")
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            print("Record added to database.")
                            I = ((math.pow((math.e), exp_upr)) / (a)) - ((math.pow((math.e), exp_lwr)) / (a))

                        int_integrand = r"\mathrm{e}^{ax + c}"  
                        integrand = int_integrand.replace("ax + c", exp)  

                    LHS_int = r"\int_{lwr_bound}^{upr_bound} \left(" + " " + integrand + " " + r"\right) \, dx" + " " + "= $"  
                    LHS_mod = LHS_int.replace("lwr_bound", f"{lwr_bound}")  
                    LHS = LHS_mod.replace("upr_bound", f"{upr_bound}")  
                    func = func_1 + f" from {lwr_bound} to {upr_bound}"  
                    func_type = choice_type[ch2 - 1]  
                
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
                
                elif ch1 == 5:  
                    print("Exiting ...")
                    os._exit(0)

                else:
                    print("Invalid Choice. Please try again.")
        
                if ch1 in range(1, 6):

                    if I != "":
                        
                        print("Displaying Latest Mathematical Notation ...")
                        print("Answer:", I)
                        L = []
                        
                        if ch1 == 1:
                            L = ["Differentiation", ch1 , func_type, ch2 , func, ch3, I]
                            insert_into_SQL_database(host_name, user_name, passwd, L)
                        
                        elif ch1 == 2:
                            L = ["Indefinite Integration", ch1 , func_type, ch2 ,func, ch3,  I]
                            insert_into_SQL_database(host_name, user_name, passwd, L)
                        
                        elif ch1 == 3:
                            L = ["Definite Integration", ch1 , func_type, ch2,  func, ch3, I]
                            insert_into_SQL_database(host_name, user_name, passwd, L)
                        
                        elif ch1 == 4:
                            L = ["Graph", func_type, ch1,  I, ch2 , "-", I]
                            insert_into_SQL_database(host_name, user_name, passwd, L)

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

            except (ValueError, KeyboardInterrupt, ZeroDivisionError, UnboundLocalError, NameError):  
                print("Invaild Input. Please try again")
        
    except (UnboundLocalError, ValueError, KeyboardInterrupt, NameError) as e:
        print("Unexpected Error occured. Please try again.")
        print("Error encountered :", str(e))
        os._exit(0)

else:
    print("Code Exited due to non - agreement of user.")  