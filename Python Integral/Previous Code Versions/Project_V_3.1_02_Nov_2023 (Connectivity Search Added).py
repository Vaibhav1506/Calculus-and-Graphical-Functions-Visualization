import matplotlib.pyplot as plt  # importing libraries for necessary functions as
import numpy as np  # numpy is automatically needed in graphs in matplotlib.
import math  # math is used for handling the calculations in definite integrals.
import sys  # Used here for exiting the program with a success code.
import mysql.connector as mc #Used for MYSQL database connection.

# Before proceeding to the python let's just learn something brief about LaTeX.
# LaTeX is a typesetting system commonly used for academic and professional documents.
# It offers powerful features for creating structured documents, mathematical equations,
# figures, tables, bibliographies, and more. LaTeX source code is written in plain text
# and is processed to produce beautifully formatted documents.It is helpful in writing math
# equations like fractions, square root , integrals , differentials and so on.
# Some basics about the LaTeX :- (the prefix is always a "/" so these are stored in raw string to override Python Escape Sequence System)
# For fraction of form numerator by denominator it can be represented as \dfrac{num_r}{den_r}
# For integrals of form ∫f(x) dx it can be represented as \int f(x) \, dx
# Definite Integrals can be represented as \int{lower_limit}^{upper_limit}
# Square root like √(x) can be represented as \sqrt{x}
# All Trigonometric Ratios (Inverse ones as well) can be represented by putting a "\" before them
# For powers or superscripts we can use ^{x}
# Logarithm (natural base e) can be represented as \log
# Mathematical constants like e (Euler's number = 2.71... ) can be represented as \mathrm{e}
# General form for values inside functions is that those should be enclosed within curly braces {}
# While writing expressions the whole expression should be enclosed with $$ (both at start and end).

# USER DEFINED FUNCTIONS

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
        co.execute("CREATE TABLE IF NOT EXISTS Calculus_User_History (`Operation Type` VARCHAR(100) ,`Operation Type Choice` VARCHAR(100) ,`Function Type` VARCHAR(100) ,`Function Type Choice` VARCHAR(100) ,`Function Expression` VARCHAR(100) , `Function Expression Choice` VARCHAR(100) , `Answer` VARCHAR(100) UNIQUE);")

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

def get_sup(x):  # Function to convert to superscript
    normal = "abcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

def convert_to_Latex_for_differentials(x):  # Function for differentials conversion to LaTeX.
    mappings = {  # Mappings corresponding to the LATEX notation for diff. mathematical notations.
        "cos": r"\cos",  # Converts a mathematical expression to LaTeX format. The mappings here correspondingly
        "sin": r"\sin",  # point to their values as represented in LaTeX format. For e.g: sin(x) is written as
        "tan": r"\tan",  # $\sin{(x)}$.
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

    if "√" in x and "/" in x:  # Checks if there is square root and fractions in the expression.
        n = x.index(
            '²')  # Finds the index of any squared expression or value in the expression. Comes handy in converting the inverse trigonometric expressions' differentials.
        if x[n + 1] == ")" or x[
            n + 1] == "-":  # Checks if there is any parentheses or minus sign after the squaring so as to not count other instances.
            x = x.replace('²', r'^{2}')  # Replaces with the LaTeX format of the square , i.e. , a^{2}.
        expression_list = x.split(
            "/")  # Splits the expression on basis of the fraction to seperate numerator and denominator into list elements.
        updated_expression_list = []

        for item in expression_list:  # Iterating in the list splitted earlier.
            updated_item = item  # Assigning a variable for each iterated item.
            for key, value in mappings.items():  # Iterating through the mappings simultaneously.
                updated_item = updated_item.replace(key, value)  # Replacing the values.
            updated_expression_list.append(updated_item)  # Append the updated item to the new list

        st = r"$\dfrac{" + updated_expression_list[0] + "}{" + updated_expression_list[1] + "}$"  # final expression

    elif "/" in x:
        expression_list = x.split("/")  # Split the expression correctly into numerator and denominator in list.
        st = "$" + r'\dfrac{' + expression_list[0] + "}{" + expression_list[
            1] + "}" + "$"  # Final expression in form of $\dfrac{num_r}{den_r}

    else:  # where num_r is the expression_list[0] and den_r is the expression_list[1]
        if "²" in x:  # Checking the squaring index in the string.
            n = x.index('²')  # Finding the index
            if x[n + 1] == "(" or x[n + 1] == ")":  # Condition if there is parentheses after this
                x = x.replace('²', r'^{2}')  # Replacement as earlier
        for key, value in mappings.items():
            x = x.replace(key, value)  # Same replacement as earlier
        st = "$" + x + "$"  # final expression

    print(st)  # printing
    expression = f"{st}"
    return expression  # storing and returning the expression in another variable and taking it in f string format

def convert_to_Latex_for_integrals(x):  # Function for differentials conversion to LaTeX.
    mappings = {  # Mappings corresponding to the LATEX notation for diff. mathematical notations.
        "cos": r"\cos",  # Converts a mathematical expression to LaTeX format. The mappings here correspondingly
        "sin": r"\sin",  # point to their values as represented in LaTeX format. For e.g: sin(x) is written as
        "tan": r"\tan",  # $\sin{(x)}$.
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

    if "√" in x and "¹" in x:
        expression_list = x[1:-5].split("/")  # Split the expression correctly into numerator and denominator.
        # The slicing is for omitting the + C which is the constant of the integration.
        func_end_idx = (expression_list[0].index(
            "¹"))  # Finding the "1" superscript for the inverse tangent functions so as to locate their terminating point.
        a = expression_list[0][
            func_end_idx + 1:]  # Taking the remaining part of the function after the tangent part enclosed in parentheses.
        # Typically if tan^-1(x) is the expression then x is being taken in this variable along with ).
        updated_expression_list = [a[1:], expression_list[1][:-1]]  # Created new list using a such that it omits ) in both cases.

        for i in range(len(updated_expression_list)):
            updated_item = updated_expression_list[i]
            for key, value in mappings.items():
                updated_item = updated_item.replace(key, value)  # Usual replacement
            updated_expression_list[i] = updated_item

        st = r"\dfrac" + updated_expression_list[0] + "{" + updated_expression_list[1] + "}"  # final strin in form of the fraction part as told earlier.
        func = expression_list[0][:func_end_idx + 1]  # taking function part
        for key, value in mappings.items():  # replacement occuring
            func = func.replace(key, value)  # omitting the "\" escape sequence
            func = func.replace('\\\\', '\\')
        num_r = func + "{(" + st + ")}"  # final expression for numerator

        den_r = expression_list[2]  # final expression for denominator
        for key, value in mappings.items():  # performing replacement in denominator
            den_r = den_r.replace(key, value)
        final_exp = r"\dfrac" + "{" + num_r + "}" + den_r  # final expression

        st = '$' + final_exp + x[-4:] + '$'  # final latex expression

    elif "/" in x:
        expression_list = x[1:-5].split("/")  # Split the expression correctly in same way to emit + C
        updated_expression_list = []

        for item in expression_list:
            updated_item = item
            for key, value in mappings.items():  # Performing replacements.
                updated_item = updated_item.replace(key, value)

                # Replace double backslashes with a single backslash
            updated_item = updated_item.replace('\\\\', '\\')  # for avoiding "\" escape sequence.
            updated_expression_list.append(updated_item)

        st = '$' + r'\dfrac{' + updated_expression_list[0] + "}" + "{" + updated_expression_list[1] + "}" + x[
                                                                                                            -4:] + '$'  # final expression

    else:
        n = x.index('²')  # locating squaring part
        if x[n + 1] == "(" or x[n + 2] == "+":  # verifying the end of the function
            x = x.replace('²', r'^{2}')  # replacement occurrence

        for key, value in mappings.items():
            x = x.replace(key, value)  # replacement throughtout
        st = "$" + x + "$"  # final expression

    print(st)
    expression = f"{st}"  # final expression stored in string
    return expression  # returning the expression

def display_Latex(expression):  # Function for displaying LaTeX in Matplotlib using only text format.
    plt.text(0.5, 0.5, expression, fontsize=15, ha='center',
             va='center')  # displaying text. ha is horizontal alignment and va is vertical alignment
    plt.axis(
        'off')  # Hide the axis                                       #and they move relative to a specified point or bounding box
    plt.show()

def evaluate_math_expression_to_numpy(x):  # converts to numpy expression for graphing.
    st = x  # made a copy of expression
    mappings = {  # defined the mappings for respective functions
        "[": "np.abs(",  # Absolute Value / Modulus
        "]": ")",
        "√": "np.sqrt",  # Square Root
        "⌊": "np.floor(",  # GIF
        "⌋": ")",
        "⌈": "np.ceil(",  # SIF
        "⌉": ")",
        "sin(": "np.sin(",  # Trigonometric & Inverse Trigonometric
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
        "^": "**",  # Exponential Powers
        "1x": "1 * x",  # Product of constants and variables
        "2x": "2 * x",
        "3x": "3 * x",
        "4x": "4 * x",
        "5x": "5 * x",
        "6x": "6 * x",
        "7x": "7 * x",
        "8x": "8 * x",
        "9x": "9 * x",
        "0x": "0 * x",
        "πx": "np.pi * x",  # Pi with variable
        "ex": "np.e * x",  # Euler's Constant with variable
        "\bπ\b": "np.pi",  # Pi
        "\be\b": "np.e",  # Euler's constant
        "log(": "np.log(",  # Logarithm
    }

    for key, value in mappings.items():  # Doing necessary replacements
        st = st.replace(key, value)
    return st  # Returning the values

def decide_range_of_function(a):  # decides the range to be displayed to make it visually appealing
    # Linspace defines the number of points evenly spaced between a specific x range or interval
    # Arange generates the same thing as Linspace except for that it also generates floating point values along with integers for more precision.

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

    return [m, n]  # returns the values of both in list to be used later

def graph_function_for_universal_functions(I):
    s = evaluate_math_expression_to_numpy(I)  # Calling the functions
    L = decide_range_of_function(I)

    if "[" in I:  # Replacing the modulus function to make it accurately visible as text.
        I = I.replace("[", "|")
    if "]" in I:
        I = I.replace("]", "|")

    print("Displaying Numpy Expression: ")  # Displaying
    print(s)
    x = L[1]  # Adjust the linspace for a better visual representation of the function
    y = eval(s)  # Evaluate function(x) values

    plt.plot(x, y, label=f'{a}')  # Creating the plot
    plt.axhline(0, color='black', linewidth=1.5)  # Horizontal line for x-axis
    plt.axvline(0, color='black', linewidth=1.5)  # Vertical line for y-axis
    plt.xlabel('x')  # Labels
    plt.ylabel(f'{a}')
    plt.title(f'Graph of {a}')
    plt.xticks(L[0])  # Adjust x-axis ticks values. Xtick values basically adjusts the markers or points of numbers or integers on x axis.
    plt.grid()  # Show grids
    plt.legend()  # Show the key
    plt.show()  # Display graph

def graph_function_for_polynomials(coefficients, final_exp):
    roots = np.roots(coefficients)  # Calculate the roots of the polynomial
    min_root = np.min(roots)  # Max root value
    max_root = np.max(roots)  # Min root value

    x = np.linspace(min_root - 1, max_root + 1,
                    1000)  # Generate  1000 x-values' intervals for plotting based on the roots

    y = np.polyval(coefficients, x)  # Calculate corresponding y-values using the polynomial function
    plt.plot(x, y, label=f'f(x) = {final_exp}')  # Plot the polynomial function
    plt.axhline(0, color='black', linewidth=1.5)  # Horizontal line at y = 0 for x-axis
    plt.axvline(0, color='black', linewidth=1.5)  # Vertical line at x = 0 for y-axis

    plt.xlabel('x')  # Labels
    plt.ylabel(f'{final_exp}')
    plt.title(f'Graph of {final_exp}')
    plt.ylim(bottom=min(plt.ylim()[0], -1))  # Add space to the negative y-axis
    plt.grid()  # Show grid
    plt.legend()  # Show key
    plt.show()  # Display the graph

inv = '{}{}'.format(get_sup('-'), get_sup('1'))  # stores ^-1
I = ""  # to store the answer
LHS = ""  # to store left hand side

# MAIN CODE
print("-" * 50)
print("CALCULUS AND FUNCTIONS VIZUALIZATION PYTHON - MYSQL CONNECTIVITY PROJECT")
print("-" * 50)
print("**NOTES TO BE TAKEN BEFORE PROCEEDING**")
print("1. While taking input use () parentheses to seperate the numerator and the denominator and other function types to avoid BODMAS confusion")
print("2. While entering the values ensure that the values fall in their respective domains where they return a definite value.")
print("3. If you want to give a fractional value enter that value in decimals correct upto 3 decimal places.")
print("4. Only general linear and implicit functions are present in this program so as to avoid complications.")
print("5. For entering trignometric functions use 'csc' for cosecant function.")
print("6  For exponentials use ^ sign.")
print("7. Modulus or Absolute Value Functions should be given using [] and not ||.")
print("8. GIF or Floor function should be represented within ⌊ ⌋ and SIF or ceiling function should be represented within ⌈ ⌉")
print("9. Polynomial Functions can be evaluated in both the choices given.")
print("10. The First one provides a better visualization of naïve or simple functions and their roots.")
print("11. If a power's coefficient is missing or not defined then enter 0 while entering the coefficients.")
print("12. The second one provides customization and using other functions implicitly in the polynomial ones.")
print("13. Complex or Special Functions like Lambert W, Riemann Zeta, Gamma functions & Factorial functions are not supported.")
print("14. While defining product between two functions or a constant and a function use * asterisk marks.")
print("15. For Polynomial Functions where the roots of x are complex numbers it's recommended not to use it in the first choice.")

n = input("Make sure you have read the above mentioned rules. Do you want to Proceed? (Y/N): ")  # Input from user

print("Required for Database connection: (You may need to try one more time again if the first time does not works.)")

while n.upper() == "Y":

    host_name = input("Enter host name: ")
    user_name = input("Enter user name: ")
    passwd = input("Enter password: ")

    create_SQL_database(host_name, user_name, passwd)

    while True:  # Running a loop
        print("SELECT OPERATION TYPE")
        print("MAIN MENU:\n1.Differentiation\n2.Indefinite Integration\n3.Definite Integration\n4.Graphs\n5.Exit")  # Main menu for selecting operation type

        try:
            ch1, ch2, ch3 = "-", "-", "-"
            
            ch1 = int(input("Enter choice: "))
            func = ""  # initialiizing variables for storing the type of functions the user is chosing
            func_1 = ""  # in various different choices.
            func_type = ""
            
            # Differentiation
            if ch1 == 1:
                function = ""
                print("SELECT FUNCTION TYPE")
                print(
                    "1. Trigonometric \n2. Inverse Trigonometric \n3. Polyomial \n4. Logarithmic \n5. Exponential")  # Menu for function type

                ch2 = int(input("Enter choice: "))
                a = int(input("Enter value of a: "))
                c = int(input("Enter value of c: "))

                choice_type = ["Trigonometric", "Inverse Trigonometric", "Polyomial", "Logarithmic", "Exponential"]  # Initializing list for tracking choices.

                # Common Differentials of functions are stored here in the variable I.
                # Since complex functions will complicate the code we have selected a
                # general linear implicit expression in all the functions for simplification
                # purposes. The form is (ax + c) linear form where a and c are constants input by the user.

                # Choices.
                if ch2 == 1:  # Trigonometric
                    print("SELECT THE APPROPIATE FUNCTION")
                    print(
                        "MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. csc(ax+c)\n 6. sec(ax+c)")  # Menu for the six trigonometric ratios.
                    ch3 = int(input("Enter choice: "))
                    exp = f"{a}x+{c}"  # expression variable

                    new_expressions_list = []  # Initialized list for appending the modified choices with the user entered expression for LaTeX format.
                    new_expressions_list_2 = []  # Initialized list for appending the modified choices with the user entered expression.
                    expressions_list = [r"\sin{(ax+c)}", r"\cos{(ax+c)}", r"\tan{(ax+c)}", r"\cot{(ax+c)}",
                                        r"\csc{(ax+c)}",
                                        r"\sec{(ax+c)}"]  # Initializing list for tracking choices to display in LaTeX format.
                    expression_list_2 = ["sin(ax+c)", "cos(ax+c)", "tan(ax+c)", "cot(ax+c)", "csc(ax+c)",
                                         "sec(ax+c)"]  # Initializing list for tracking choices.

                    for i in expressions_list:  # Common thing in all cases that the choices are written in a list and whatever
                        i = i.replace("ax+c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed in latex. "ax+c" is
                        new_expressions_list.append(i)  # replaced by the expression input by the user.

                    for i in expression_list_2:  # Common thing in all cases that the choices are written in a list and whatever
                        i = i.replace("ax+c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed. "ax+c" is
                        new_expressions_list_2.append(i)  # replaced by the expression input by the user.

                    # Choices.
                    if ch3 == 1:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"{a}cos({exp})"
                    elif ch3 == 2:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"-{a}sin({exp})"
                    elif ch3 == 3:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"{a}sec²({exp})"
                    elif ch3 == 4:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"-{a}csc²({exp})"
                    elif ch3 == 5:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"-{a}csc({exp})cot({exp})"
                    elif ch3 == 6:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"{a}sec({exp})tan({exp})"

                    function = new_expressions_list[ch3 - 1]  # selecting the LaTeX format of choice.
                    func = new_expressions_list_2[ch3 - 1]  # selecting the choice.

                elif ch2 == 2:  # inverse trigonometric
                    print("SELECT THE APPROPIATE FUNCTION")
                    print(f"MENU:\n 1. sin{inv}(ax+c)\n 2. cos{inv}(ax+c)\n 3. tan{inv}(ax+c)\n"
                        f"4. cot{inv}(ax+c)\n 5. csc{inv}(ax+c)\n 6. sec{inv}(ax+c)")  # Menu for the 6 inverse trigonometric functions.
                    ch3 = int(input("Enter choice: "))
                    exp = f"{a}x+{c}"  # expression variable

                    new_expressions_list = []  # Initialized list for appending the modified choices with the user entered expression for LaTeX format.
                    new_expressions_list_2 = []  # Initialized list for appending the modified choices with the user entered expression.
                    expressions_list = [r"\sin^{-1}{(ax+c)}", r"\cos^{-1}{(ax+c)}", r"\tan^{-1}{(ax+c)}",
                                        r"\cot^{-1}{(ax+c)}", r"\csc^{-1}{(ax+c)}",r"\sec^{-1}{(ax+c)}"]  # Initializing list for tracking choices to display in LaTeX format.
                    expression_list_2 = [f"sin{inv}(ax+c)", f"cos{inv}(ax+c)", f"tan{inv}(ax+c)",
                                         f"cot{inv}(ax+c)",f"csc{inv}(ax+c)",f"sec{inv}(ax+c)"]  # Initializing list for tracking choices.

                    for i in expressions_list:  # Common thing in all cases that the choices are written in a list and whatever
                        i = i.replace("ax+c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed in latex. "ax+c" is
                        new_expressions_list.append(i)  # replaced by the expression input by the user.

                    for i in expression_list_2:  # Common thing in all cases that the choices are written in a list and whatever
                        i = i.replace("ax+c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed. "ax+c" is
                        new_expressions_list_2.append(i)  # replaced by the expression input by the user.

                    # Choices.
                    if ch3 == 1:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"{a}/√(1-({exp})²)"
                    elif ch3 == 2:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"-{a}/√(1-({exp})²)"
                    elif ch3 == 3:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"{a}/(1+({exp})²)"
                    elif ch3 == 4:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"-{a}/(1+({exp})²)"
                    elif ch3 == 5:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"-1/|x|√(({exp})²-1)"
                    elif ch3 == 6:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"1/|x|√(({exp})²-1)"

                    function = new_expressions_list[ch3 - 1]  # selecting the LaTeX format of choice.
                    func = new_expressions_list_2[ch3 - 1]  # selecting the choice.

                elif ch2 == 3:  # polynomial of the form ax+c
                    exp = f"{a}x + {c}"
                    func = exp  # storing the expression.
                    if check_duplicates(function, host_name, user_name, passwd)[0] == 1:
                        I = check_duplicates(function, host_name, user_name, passwd)[1]
                    else:
                        I = str(a)
                    function = exp  # storing the expression to convert to LaTeX.
                    func = exp  # storing the expression.

                elif ch2 == 4:  # logarithmic of the form log(ax+c)
                    exp = f"{a}x + {c}"
                    func = "log(ax+c)".replace("ax+c", exp)  # storing the expression.
                    if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                        I = check_duplicates(func, host_name, user_name, passwd)[1]
                    else:
                        I = f"{a}/{a}x+{c}"
                    function = r"\log" + "{(" + exp + ")}"  # storing the expression to convert to LaTeX.
                    func = "log(ax+c)".replace("ax+c", exp)  # storing the expression.

                elif ch2 == 5:  # exponential of the form e^(ax+c)
                    exp = f"{a}x + {c}"
                    func = "e" + get_sup(exp)  # storing the expression.
                    if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                        I = check_duplicates(func, host_name, user_name, passwd)[1]
                    else:
                        I = f'{a}(e' + '{}{}{}{}{}{}'.format(get_sup('('), get_sup(str(a)), get_sup('x'), get_sup('+'),
                                                         get_sup(str(c)), get_sup(
                            ')')) + ")"  # formatting is done for superscripting the expression.
                    function = r"\mathrm{e}^{" + exp + "}"  # storing the expression to convert to LaTeX.
                    func = "e" + get_sup(exp)  # storing the expression.

                LHS = r"\dfrac{d}{dx} \left(" + " " + function + " " + r"\right) " + " " + "="  # LHS showing d/dx of a function is stored here to show later in Matplotlib
                func_type = choice_type[ch2 - 1]  # storing the function type choice chosen by the user.

            # Indefinite integration
            elif ch1 == 2:
                integrand = ""  # initialiizing variables for storing the type of functions the user is chosing

                print("SELECT FUNCTION TYPE")
                print(
                    "1. Trigonometric \n2. Inverse Trigonometric \n3. Polyomial \n4. Logarithmic \n5. Exponential")  # Menu for function type

                ch2 = int(input("Enter choice: "))
                choice_type = ["Trigonometric", "Inverse Trigonometric", "Polyomial", "Logarithmic",
                               "Exponential"]  # Initializing for tracking user choice.

                # Common Integrals of functions are stored here in the variable I.
                # Since complex functions will complicate the code we have selected a
                # general linear implicit expression in all the functions for simplification
                # purposes. The form is (ax + c) linear form where a and c are constants input by the user.

                # Choices.
                if ch2 == 1:  # trigonometric
                    a = int(input("Enter value of a: "))
                    c = int(input("Enter value of c: "))

                    print("SELECT THE APPROPIATE FUNCTION")
                    print(
                        f"MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. csc(ax+c)\n 6. sec(ax+c)\n 7. sec(ax+c)tan(ax+c)\n 8. csc(ax+c)cot(ax+c)\n 9. csc{get_sup('2')}(ax+c)\n 10. sec{get_sup('2')}(ax+c)")
                    ch3 = int(input("Enter choice: "))

                    exp = f"{a}x+{c}"  # expression variable
                    new_expressions_list = []  # Initialized list for appending the modified choices with the user entered expression for LaTeX format.
                    new_expressions_list_2 = []  # Initialized list for appending the modified choices with the user entered expression.
                    expressions_list = [r"\sin{(ax+c)}", r"\cos{(ax+c)}", r"\tan{(ax+c)}", r"\cot{(ax+c)}",
                                        r"\csc{(ax+c)}", r"\sec{(ax+c)}", r"\sec{(ax+c)}\tan{(ax+c)}",
                                        r"\csc{(ax+c)}\cot{(ax+c)}", r"\csc^{2}{(ax+c)}",
                                        r"\sec^{2}{(ax+c)}"]  # Initializing list for tracking choices to display in LaTeX format.
                    expression_list_2 = ["sin(ax+c)", "cos(ax+c)", "tan(ax+c)", "cot(ax+c)", "csc(ax+c)", "sec(ax+c)",
                                         "sec(ax+c)tan(ax+c)", "csc(ax+c)cot(ax+c)", f"csc{get_sup('2')}(ax+c)",
                                         f"sec{get_sup('2')}(ax+c)"]  ##Initializing list for tracking choices.

                    for i in expressions_list:  # Common thing in all cases that the choices are written in a list and whatever
                        i = i.replace("ax+c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed in latex. "ax+c" is
                        new_expressions_list.append(i)  # replaced by the expression input by the user.

                    for i in expression_list_2:  # Common thing in all cases that the choices are written in a list and whatever
                        i = i.replace("ax+c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed. "ax+c" is
                        new_expressions_list_2.append(i)  # replaced by the expression input by the user.

                    # Choices.
                    if ch3 == 1:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(-cos({exp})/{a}) + C"
                    elif ch3 == 2:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(sin({exp})/{a}) + C"
                    elif ch3 == 3:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(-log(|cos({exp})|)/{a}) + C"  # /u00bx is used for superscripting of x
                    elif ch3 == 4:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(log(|sin({exp})|)/{a}) + C"  # /u00bx is used for superscripting of x
                    elif ch3 == 5:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(-log(|csc({exp}) + cot({exp})|)/{a}) + C"
                    elif ch3 == 6:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(-log(|tan({exp}) + sec({exp})|)/{a}) + C"
                    elif ch3 == 7:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(sec({exp})/{a}) + C"
                    elif ch3 == 8:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(-csc({exp})/{a}) + C"
                    elif ch3 == 9:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(-cot({exp})/{a}) + C"
                    elif ch3 == 10:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(tan({exp})/{a}) + C"

                    integrand = new_expressions_list[ch3 - 1]  # selecting the LaTeX format of choice.
                    func = new_expressions_list_2[ch3 - 1]  # selecting the choice.

                elif ch2 == 2:  # inverse trigonometric

                    print("SELECT THE APPROPIATE FUNCTION")
                    print(
                        f"MENU:\n 1. 1/√(1 - (ax + c){get_sup('2')})\n 2. -1/√(1 - (ax+c){get_sup('2')})\n 3. 1/(b + (ax+c){get_sup('2')})\n 4. -1/(b + (ax+c){get_sup('2')})\n 5. 1/((ax+c)√((ax+c){get_sup('2')} - 1)\n 6. -1/((ax+c)√((ax+c){get_sup('2')}) - 1")

                    a = int(input("Enter value of a: "))
                    c = int(input("Enter value of c: "))
                    b = int(input("Enter value of b (valid only for 3. and 4.):"))  # as other functions dont have "b"
                    ch3 = int(input("Enter choice: "))
                    exp = f"{a}x+{c}"  # expression variable

                    new_expressions_list = []  # initialiizing lists for storing the type of functions the user is chosing.
                    new_expressions_list_2 = []
                    final_expressions_list = []
                    final_expressions_list_2 = []
                    expressions_list = [r"\dfrac{1}{\sqrt{1 - (ax + c)^{2}}}", r"\dfrac{-1}{\sqrt{1 - (ax + c)^{2}}}",
                                        r"\dfrac{1}{b + (ax + c)^{2}}", r"\dfrac{-1}{b + (ax + c)^{2}}",
                                        r"\dfrac{1}{(ax + c)\sqrt{(ax + c)^2 - 1}}",
                                        r"\dfrac{-1}{(ax + c)\sqrt{(ax + c)^2 - 1}}"]  # Initializing list for tracking choices to display in LaTeX format.
                    expression_list_2 = [f"1/√(1 - (ax + c){get_sup('2')})", f"-1/√(1 - (ax + c){get_sup('2')})",
                                         f"1/(b + (ax + c){get_sup('2')})", f"-1/(b + (ax + c){get_sup('2')})",
                                         f"1/((ax + c)√((ax + c){get_sup('2')} - 1)",
                                         f"-1/((ax + c)√((ax + c){get_sup('2')}) - 1"]  # Initializing list for tracking choices to display.

                    for i in expressions_list:  # Common thing in all cases that the choices are written in a list and whatever
                        i = i.replace("ax + c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed in latex. "ax+c" is
                        new_expressions_list.append(i)  # replaced by the expression input by the user.

                    for j in new_expressions_list:  # Common thing in all cases that the choices are written in a list and whatever
                        j = j.replace("b",
                                      f"{b}")  # the user inputs (minus 1) is the choice from list displayed in latex. "b" is
                        final_expressions_list.append(j)  # replaced by the expression input by the user.

                    for k in expression_list_2:  # Common thing in all cases that the choices are written in a list and whatever
                        k = k.replace("ax + c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed. "ax+c" is
                        new_expressions_list_2.append(k)  # replaced by the expression input by the user.

                    for l in new_expressions_list_2:  # Common thing in all cases that the choices are written in a list and whatever
                        l = l.replace("b",
                                      f"{b}")  # the user inputs (minus 1) is the choice from list displayed. "b" is
                        final_expressions_list_2.append(l)  # replaced by the expression input by the user.

                    # Choices.
                    if ch3 == 1:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(sin{inv}({exp})/{a}) + C"
                    elif ch3 == 2:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(cos{inv}({exp})/{a}) + C"
                    elif ch3 == 3:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(tan{inv}(({exp})/√({b}))/({a}√({b}))) + C"
                    elif ch3 == 4:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(cot{inv}(({exp})/√({b}))/({a}√({b}))) + C"
                    elif ch3 == 5:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(sec{inv}({exp})/{a}) + C"
                    elif ch3 == 6:
                        func = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(csc{inv}({exp})/{a}) + C"

                    integrand = final_expressions_list[ch3 - 1]  # selecting the LaTeX format of choice.
                    func = final_expressions_list_2[ch3 - 1]  # selecting the choice.

                elif ch2 == 3:  # polynomial of form (ax+c)
                    a = int(input("Enter value of a: "))
                    c = int(input("Enter value of c: "))
                    integrand = f"{a}x + {c}"  # storing the expression to convert to LaTeX
                    func = integrand  # storing the expression
                    if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                        I = check_duplicates(func, host_name, user_name, passwd)[1]
                    else:
                        I = f"{int(a / 2) if a % 2 == 0 else (a / 2)}x{get_sup(str(2))} + {c}x + C"  #condition for deciding whether it should be a fraction or not.
                    func = integrand  # storing the expression

                elif ch2 == 4:  # logarithmic of form log(ax+c) and expressions of form 1/(ax+b)
                    print("SELECT THE APPROPIATE FUNCTION")
                    print(f"MENU:\n1. log(ax + c) \n2. 1/(ax + c) \n3. a{get_sup('x')}")
                    ch3 = int(input("Enter choice: "))
                    a = int(input("Enter value of a: "))
                    c = int(input("Enter value of c (only for 1. and 2.): "))
                    exp = f"{a}x+{c}"  # expression variable

                    expressions_list = [r"\log{(ax + c)}", r"\dfrac{1}{(ax + c)}",
                                        r"a^{x}"]  # Initializing list for tracking choices in LaTeX format.
                    expression_list_2 = ["log(ax + c)", "1/(ax + c)",
                                         f"a{get_sup('x')}"]  # Initializing list for tracking choices.
                    new_expressions_list = []  # Initialized list for appending the modified choices with the user entered expression for LaTeX format.
                    new_expressions_list_2 = []  # Initialized list for appending the modified choices with the user entered expression.

                    for i in expressions_list:
                        i = i.replace("ax + c", exp)
                        new_expressions_list.append(i)
                    new_expressions_list[2] = new_expressions_list[2].replace("a", f"{a}")

                    for j in expression_list_2:
                        j = j.replace("ax + c", exp)
                        new_expressions_list_2.append(j)
                    new_expressions_list_2[2] = new_expressions_list_2[2].replace("a", f"{a}")

                    # Choices.
                    if ch3 == 1:
                        func = new_expressions_list_2[ch3 - 1]
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"((({exp})(log({exp})-1))/{a}) + C"
                    elif ch3 == 2:
                        func = new_expressions_list_2[ch3 - 1]
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"(log(|({exp})|)/{a}) + C"
                    elif ch3 == 3:
                        func = new_expressions_list_2[ch3 - 1]
                        if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func, host_name, user_name, passwd)[1]
                        else:
                            I = f"({a}{get_sup('x')}/log({a})) + C"

                    integrand = new_expressions_list[ch3 - 1]
                    func = new_expressions_list_2[ch3 - 1]

                elif ch2 == 5:  # exponential of form e^(ax+c)
                    a = int(input("Enter value of a: "))
                    c = int(input("Enter value of c: "))
                    exp = f"{a}x + {c}"
                    func = "e" + get_sup(exp)  # storing expression

                    if check_duplicates(func, host_name, user_name, passwd)[0] == 1:
                        I = check_duplicates(func, host_name, user_name, passwd)[1]
                    else:
                        I = '((e' + f'{get_sup("(")}' + f'{get_sup(exp)}' + f'{get_sup(")")}' + f")/{a}) + C"  # storing expression

                    int_integrand = r"\mathrm{e}^{ax + c}"  # storing expression in form of LaTeX.
                    integrand = int_integrand.replace("ax + c",
                                                      exp)  # performing replacements for the expression entered by user.
                    func = "e" + get_sup(exp)  # storing expression

                LHS = r"\int \left(" + " " + integrand + " " + r"\right) \, dx" + " " + "="  # integrand is the function to be integrated and is on LHS with dx being the variable
                # with respect to with the function should be integrated. For e.g.: ∫f(x)dx is the
                # general form where f(x) is chosen by the user.
                func_type = choice_type[ch2 - 1]  # Appending the choice.

            # Definite integration
            elif ch1 == 3:
                integrand = ""
                print("SELECT FUNCTION TYPE")
                print("1.Trigonometric\n2.Inverse Trigonometric\n3.Polyomial\n4.Logarithmic\n5.Exponential")

                ch2 = int(input("Enter choice: "))
                a = int(input("Enter value of a: "))
                c = int(input("Enter value of c: "))

                lwr_bound = int(input("Enter lower bound: "))  # lower limit
                upr_bound = int(input("Enter upper bound: "))  # upper limit

                choice_type = ["Trigonometric", "Inverse Trigonometric", "Polyomial", "Logarithmic", "Exponential"]

                # Common Integrals of functions calculated from upper bound or upper limit
                # to lower bound or lower limit are stored here in the variable I.
                # The general formula or the fundamental theory of Calculus states that
                # If integral of any function f(x) is given from a(lower limit) to b(upper limit)
                # and F(x) is the integral or anti-derivative of the function then the
                # evaluated expression will be F(b) - F(a)
                # Since complex functions will complicate the code we have selected a
                # general linear implicit expression in all the functions for simplification
                # purposes. The form is (ax + c) linear form where a and c are constants input by the user.
                # The formula are put here in directly using the math module.

                # Choices.
                if ch2 == 1:  # trigonometric
                    print("SELECT APPROPIATE FUNCTION")
                    print(
                        "MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. csc(ax+c)\n 6. sec(ax+c)\n 7. sec(ax+c)tan(ax+c)\n 8. csc(ax+c)cot(ax+c)\n 9. csc\u00b2(ax+c)\n 10. sec\u00b2(ax+c)")
                    ch3 = int(input("Enter choice: "))
                    exp = f"{a}x + {c}"
                    exp_lwr = (a * lwr_bound) + c  # calculating exp in terms of lower limit of x
                    exp_upr = (a * upr_bound) + c  # calculating exp in terms of upper limit of x

                    new_expressions_list = []  # Initialized list for appending the modified choices with the user entered expression for LaTeX format.
                    new_expressions_list_2 = []  # Initialized list for appending the modified choices with the user entered expression.
                    expressions_list = [r"\sin{(ax+c)}", r"\cos{(ax+c)}", r"\tan{(ax+c)}", r"\cot{(ax+c)}",
                                        r"\csc{(ax+c)}", r"\sec{(ax+c)}", r"\sec{(ax+c)}\tan{(ax+c)}",
                                        r"\csc{(ax+c)}\cot{(ax+c)}", r"\csc^{2}{(ax+c)}",
                                        r"\sec^{2}{(ax+c)}"]  # initializing list for tracking the LaTeX format of choice.
                    expression_list_2 = ["sin(ax+c)", "cos(ax+c)", "tan(ax+c)", "cot(ax+c)", "csc(ax+c)", "sec(ax+c)",
                                         "sec(ax+c)tan(ax+c)", "csc(ax+c)cot(ax+c)",
                                         "csc\u00b2(ax+c)\n 10. sec\u00b2(ax+c)"]  # initializing list for tracking the choice.

                    for i in expressions_list:  # Common thing in all cases that the choices are written in a list and whatever
                        i = i.replace("ax+c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed in latex. "ax+c" is
                        new_expressions_list.append(i)  # replaced by the expression input by the user.

                    for i in expression_list_2:  # Common thing in all cases that the choices are written in a list and whatever
                        i = i.replace("ax+c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed. "ax+c" is
                        new_expressions_list_2.append(i)  # replaced by the expression input by the user.

                    # Choices
                    if ch3 == 1:  # Calculations.
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (-math.cos(exp_upr) / a) - (-math.cos(exp_lwr) / a)
                    elif ch3 == 2:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (math.sin(exp_upr) / a) - (math.sin(exp_lwr) / a)
                    elif ch3 == 3:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (-math.log(abs(math.cos(exp_upr))) / a) - (-math.log(abs(math.cos(exp_lwr))) / a)
                    elif ch3 == 4:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (math.log(abs(math.sin(exp_upr))) / a) - (math.log(abs(math.sin(exp_lwr))) / a)
                    elif ch3 == 5:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (-math.log(abs(1 / math.sin(exp_upr) + 1 / math.tan(exp_upr))) / a) - (
                                    -math.log(abs(1 / math.sin(exp_lwr) + 1 / math.tan(exp_lwr))) / a)
                    elif ch3 == 6:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (-math.log(abs((math.tan(exp_upr) + 1 / math.cos(exp_upr)))) / a) - (
                                    -math.log(abs((math.tan(exp_lwr) + 1 / math.cos(exp_lwr)))) / a)
                    elif ch3 == 7:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (1 / math.cos(exp_upr) / a) - (1 / math.cos(exp_lwr) / a)
                    elif ch3 == 8:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (-1 / math.sin(exp_upr) / a) - (-1 / math.sin(exp_lwr) / a)
                    elif ch3 == 9:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (-1 / math.tan(exp_upr) / a) - (-1 / math.tan(exp_lwr) / a)
                    elif ch3 == 10:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (math.tan(exp_upr) / a) - (math.tan(exp_lwr) / a)

                    integrand = new_expressions_list[ch3 - 1]  # selecting the LaTeX format of choice.
                    func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.

                elif ch2 == 2:  # inverse trigonometric
                    print("SELECT APPROPIATE FUNCTION")
                    print(
                        "MENU:\n 1. 1/√(1 - (ax + c)\u00b2)\n 2. -1/√(1 - (ax + c)\u00b2)\n 3. 1/(b + (ax + c)\u00b2)\n 4. -1/(b + (ax + c)\u00b2)\n 5. 1/((ax + c)√((ax + c)\u00b2 - 1)\n 6. -1/((ax + c)√((ax + c)\u00b2) - 1")
                    b = int(input("Enter value of b (valid only for 3. and 4.):"))
                    ch3 = int(input("Enter choice: "))
                    exp_lwr = (a * lwr_bound) + c  # calculating exp in terms of lower limit of x
                    exp_upr = (a * upr_bound) + c  # calculating exp in terms of upper limit of x
                    exp = f"{a}x + {c}"  # expression variable

                    new_expressions_list = []  # Initialized list for appending the modified choices with the user entered expression for LaTeX format as well as others.
                    new_expressions_list_2 = []
                    final_expressions_list = []
                    final_expressions_list_2 = []
                    expressions_list = [r"\dfrac{1}{\sqrt{1 - (ax + c)^{2}}}", r"\dfrac{-1}{\sqrt{1 - (ax + c)^{2}}}",
                                        r"\dfrac{1}{b + (ax + c)^{2}}", r"\dfrac{-1}{b + (ax + c)^{2}}",
                                        r"\dfrac{1}{(ax + c)\sqrt{(ax + c)^2 - 1}}",
                                        r"\dfrac{-1}{(ax + c)\sqrt{(ax + c)^2 - 1}}"]  # initialiizing lists for storing the type of functions the user is chosing in LaTeX format.
                    expression_list_2 = ["1/√(1 - (ax + c)\u00b2)", "-1/√(1 - (ax + c)\u00b2)",
                                         "1/(b + (ax + c)\u00b2)", "-1/(b + (ax + c)\u00b2)",
                                         "1/((ax + c)√((ax + c)\u00b2 - 1)",
                                         "-1/((ax + c)√((ax + c)\u00b2) - 1"]  # initialiizing lists for storing the type of functions the user is chosing.

                    for i in expressions_list:  # Common thing in all cases that the choices are written in a list and whatever
                        i = i.replace("ax + c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed in latex. "ax+c" is
                        new_expressions_list.append(i)  # replaced by the expression input by the user.

                    for j in new_expressions_list:  # Common thing in all cases that the choices are written in a list and whatever
                        j = j.replace("b",
                                      f"{b}")  # the user inputs (minus 1) is the choice from list displayed in latex. "b" is
                        final_expressions_list.append(j)  # replaced by the expression input by the user.

                    for k in expression_list_2:  # Common thing in all cases that the choices are written in a list and whatever
                        k = k.replace("ax + c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed. "ax+c" is
                        new_expressions_list_2.append(k)  # replaced by the expression input by the user.

                    for l in new_expressions_list_2:  # Common thing in all cases that the choices are written in a list and whatever
                        l = l.replace("b",
                                      f"{b}")  # the user inputs (minus 1) is the choice from list displayed. "b" is
                        final_expressions_list_2.append(l)  # replaced by the expression input by the user.

                    # Choices.
                    if ch3 == 1:  # Calculations
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (math.asin(exp_upr) / a) - (math.asin(exp_lwr) / a)
                    elif ch3 == 2:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = -(math.acos(exp_upr) / a) - -(math.acos(exp_lwr) / a)
                    elif ch3 == 3:
                        I = (math.atan((exp_upr) / math.sqrt(b)) / (a * math.sqrt(b))) - (
                                    math.atan((exp_lwr) / math.sqrt(b)) / (a * math.sqrt(b)))
                    elif ch3 == 4:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (math.atan(math.sqrt(b) / (exp_upr)) / (a * math.sqrt(b))) - (
                                    math.atan(math.sqrt(b) / (exp_lwr)) / (
                                        a * math.sqrt(b)))  # arccot(x) = arctan(1 / x)
                    elif ch3 == 5:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (math.acos(1 / exp_upr) / a) - (math.acos(1 / exp_lwr) / a)  # arcsec(x) = arccos(1 / x)
                    elif ch3 == 6:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (math.asin(1 / exp_upr) / a) - (math.asin(1 / exp_lwr) / a)  # arccosec(x) = arcsin(1 / x)

                    integrand = final_expressions_list[ch3 - 1]  # selecting the LaTeX format of choice.
                    func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.

                elif ch2 == 3:  # polynomial of form (ax+c)
                    integrand = f"{a}x + {c}"  # storing the expression for latex format.
                    func_1 = integrand  # storing the expression.
                    if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                        I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                    else:
                        I = ((a / 2) * ((upr_bound ** 2) - (lwr_bound ** 2))) + c * (upr_bound - lwr_bound)

                elif ch2 == 4:  # logarithmic of form log(ax+c) and expressions of form 1/(ax+b)
                    print("SELECT APPROPIATE FUNCTION")
                    print(f"MENU:\n1. log(ax + c) \n2. 1/(ax + c) \n3. a{get_sup('x')}")
                    ch3 = int(input("Enter choice: "))

                    exp = f"{a}x + {c}"
                    exp_lwr = (a * lwr_bound) + c  # calculating exp in terms of lower limit of x
                    exp_upr = (a * upr_bound) + c  # calculating exp in terms of upper limit of x

                    expressions_list = [r"\log{(ax + c)}", r"\dfrac{1}{(ax + c)}",
                                        r"a^{x}"]  # initialiizing lists for storing the type of functions the user is chosing in LaTeX.
                    expression_list_2 = ["log(ax + c)", "1/(ax + c)",
                                         f"a{get_sup('x')}"]  # initialiizing lists for storing the type of functions the user is chosing.
                    new_expressions_list = []  # Initialized list for appending the modified choices with the user entered expression for LaTeX format.
                    new_expressions_list_2 = []  # Initialized list for appending the modified choices with the user entered expression.

                    for i in expressions_list:  # Common thing in all cases that the choices are written in a list and whatever
                        i = i.replace("ax + c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed in latex. "ax+c" is
                        new_expressions_list.append(i)  # replaced by the expression input by the user.
                    new_expressions_list[2] = new_expressions_list[2].replace("a", f"{a}")  # Final Replacement

                    for j in expression_list_2:  # Common thing in all cases that the choices are written in a list and whatever
                        j = j.replace("ax + c",
                                      exp)  # the user inputs (minus 1) is the choice from list displayed in latex. "ax+c" is
                        new_expressions_list_2.append(j)  # replaced by the expression input by the user.
                    new_expressions_list_2[2] = new_expressions_list_2[2].replace("a", f"{a}")  # Final Replacement.

                    # Choices.
                    if ch3 == 1:  # Calculations.
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (((exp_upr) * (math.log(exp_upr) - 1)) / a) - (((exp_lwr) * (math.log(exp_lwr) - 1)) / a)
                    elif ch3 == 2:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (math.log(abs(exp_upr)) / a) - (math.log(abs(exp_lwr)) / a)
                    elif ch3 == 3:
                        func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.
                        if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                            I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                        else:
                            I = (math.pow(a, upr_bound) / math.log(a)) - (math.pow(a, lwr_bound) / math.log(a))

                    integrand = new_expressions_list[ch3 - 1]  # selecting the LaTeX format of choice.
                    func_1 = new_expressions_list_2[ch3 - 1]  # selecting the choice.

                elif ch2 == 5:  # exponential of form e^(ax+c)
                    exp = f"{a}x + {c}"
                    exp_lwr = (a * lwr_bound) + c  # calculating exp in terms of lower limit of x
                    exp_upr = (a * upr_bound) + c  # calculating exp in terms of upper limit of x
                    func_1 = "e" + get_sup(exp)  # Storing the expression.
                    if check_duplicates(func_1, host_name, user_name, passwd)[0] == 1:
                        I = check_duplicates(func_1, host_name, user_name, passwd)[1]
                    else:
                        I = ((math.pow((math.e), exp_upr)) / (a)) - ((math.pow((math.e), exp_lwr)) / (a))

                    int_integrand = r"\mathrm{e}^{ax + c}"  # Storing the expression for LaTeX format
                    integrand = int_integrand.replace("ax + c",
                                                      exp)  # Replacing the expression with the user-entered one.

                LHS_int = r"\int_{lwr_bound}^{upr_bound} \left(" + " " + integrand + " " + r"\right) \, dx" + " " + "= $"  # In latex a definite integral from a to b where
                LHS_mod = LHS_int.replace("lwr_bound",
                                          f"{lwr_bound}")  # a is the lower bound and b is the upper bound is represented
                LHS = LHS_mod.replace("upr_bound",
                                      f"{upr_bound}")  # as \int{a}^{b}. Here replacements have been done to replace the
                func = func_1 + f" from {lwr_bound} to {upr_bound}"  # bounds.
                func_type = choice_type[ch2 - 1]  # Storing the function type choice entered by the user.

            # Graphs
            elif ch1 == 4:
                print("MENU")  # Menu and choices
                print("1. Polynomial Function (recommended for better visualization of Polynomial Functions)")
                print("2. Other Functions (Trigonometric, Inverse, Exponential, etc.)")

                ch2 = int(input("Enter choice: "))
                choice_type = ["Polynomial Function", "Basic Mathematical Function"]

                if ch2 == 1:  # Accepts general form of polynomial only
                    deg = int(input(
                        "Enter degree (highest power of polynomial): "))  # Degree of polynomial is accepted which is the highest power present in expression
                    coefficients = []  # Initializing both coefficient values and empty string expression.
                    st = ""

                    for i in range(deg, 0, -1):  # Loop runs until all the coefficients are accepted
                        coeff = int(input(f"Enter the coefficient of x^{i} : "))  # Accepting coefficients
                        st += str(
                            coeff) + f"x^{i} + "  # Forming the string of the expression being entered on basis of coefficients.
                        coefficients.append(coeff)  # Appending to the list

                    const = int(input("Enter constant (last number) of polynomial: "))  # Accepting constant
                    coefficients.append(const)  # Appending

                    I = st + str(const)  # Forming the string format of the polynomial to be displayed.

                    graph_function_for_polynomials(coefficients, I)

                elif ch2 == 2:  # Accepts elementary mathematical functions
                    I = input("Enter the function: ")  # User Input
                    graph_function_for_universal_functions(I)  # Function Calling

                else:
                    print("Invalid Choice.")  # Error Message

                func_type = choice_type[ch2 - 1]  # storing the function type choice chosen by the user.
            
            # Code Termination
            elif ch1 == 5:  
                print("Exiting ...")
                sys.exit()

            else:
                print("Invalid Choice. Please try again.")

            # Executes after the menu completion
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
                        L = ["Graph", func_type, ch1,  I, ch2 , "-", "-"]
                        insert_into_SQL_database(host_name, user_name, passwd, L)

                else:
                    print("Displaying latest mathematical notation evaluated ...")
                    print(
                        "No Mathematical Expression has been evaluated since user has not entered any expression.")  # Since I is getting displayed therefore this msg is displayed

                if ch1 == 1:  # For Differentiation
                    print("Displaying Latex Notation ... ")

                    RHS = convert_to_Latex_for_differentials(I)[
                          1:]  # Same concept as used in Integral's one for $ notation.
                    final_exp = "$" + LHS + " " + RHS  # Final Expression

                    display_Latex(final_exp)  # Function call

                elif ch1 == 2 or ch1 == 3:  # For both types of integration
                    print("Displaying LaTeX Notation ...")

                    if type(I) == int or type(
                            I) == float:  # Checking whether I is integer or float as in case of Indefinite
                        RHS = str(I)  # Integration it is not.

                    else:
                        RHS = convert_to_Latex_for_integrals(I)[1:]  # Displaying except the $ at the beginning as there
                        # shouldn't be $ in between the equation.

                    final_exp = "$" + LHS + " " + RHS  # Concatenating both LHS and RHS of the equation
                    # with $ added at beginning since there is already one at the end
                    display_Latex(final_exp)  # function call

        except (ValueError, KeyboardInterrupt):  # Exceptions
            print("Invaild Input. Please try again")  # Error message

else:
    print("Code Exited due to non - agreement of user.")  # Error message