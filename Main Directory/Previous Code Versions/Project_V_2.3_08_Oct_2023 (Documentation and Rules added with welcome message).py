import matplotlib.pyplot as plt          #importing libraries for necessary functions as
import numpy as np                       #numpy is automatically needed in graphs in matplotlib.
import math                              #math is used for handling the calculations in definite integrals. 
import sys                               #Used here for exiting the program with a success code.

#LaTeX is a typesetting system commonly used for academic and professional documents. 
#It offers powerful features for creating structured documents, mathematical equations, 
#figures, tables, bibliographies, and more. LaTeX source code is written in plain text 
#and is processed to produce beautifully formatted documents.It is helpful in writing math 
#equations like fractions, square root , integrals , differentials and so on. 
#Some basics about the LaTeX :- (the prefix is always a "/" so these are stored in raw string to override Python Escape Sequence System)
#For fraction of form numerator by denominator it can be represented as \dfrac{num_r}{den_r}
#For integrals of form ∫f(x) dx it can be represented as \int f(x) \, dx 
#Definite Integrals can be represented as \int{lower_limit}^{upper_limit}
#Square root like √(x) can be represented as \sqrt{x}
#All Trigonometric Ratios (Inverse ones as well) can be represented by putting a "\" before them
#For powers or superscripts we can use ^{x}
#Logarithm (natural base e) can be represented as \log
#Mathematical constants like e (Euler's number = 2.71... ) can be represented as \mathrm{e}
#General form for values inside functions is that those should be enclosed within curly braces {}
#While writing expressions the whole expression should be enclosed with $$ (both at start and end).

#FUNCTIONS

def Graph(n1):
    if n1 == 1:      # sine
        x = np.linspace(-6.283, 6.283, 100)  # 100 points from -2pi to 2pi
        y = np.sin(x)  # Compute sin(x) values
        y = plt.plot(x, y, label='sin(x)')
        # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('sin(x)')
        plt.title('Sin Function')
        plt.xticks(list(range(-7, 8, 1)))

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    
    elif n1 == 2:    # cosine
        x = np.linspace(-6.283, 6.283, 100)  # 100 points from -2pi to 2pi
        y = np.cos(x)  # Compute cos(x) values
        y = plt.plot(x, y, label='cos(x)')
        # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('cos(x)')
        plt.title('Cos Function')
        plt.xticks(list(range(-7, 7, 1)))

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    
    elif n1 == 3:    # tangent
        x = np.linspace(-6.283, 6.283, 100)  # 100 points from -2pi to 2pi
        y = np.tan(x)  # Compute tan(x) values
        y = plt.plot(x, y, label='tan(x)')
        # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('tan(x)')
        plt.title('Tan Function')
        plt.xticks(list(range(-7, 7, 1)))

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    
    elif n1 == 4:    # cotangent
        x = np.linspace(-6.283, 6.283, 10000)  # 100 points from -2pi to 2pi
        y = 1 / np.tan(x)  # Compute cot(x) values
        y = plt.plot(x, y, label='tan(x)')
        # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('cot(x)')
        plt.title('Cot Function')
        plt.xticks(list(range(-10, 11, 1)))

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    
    elif n1 == 5:    # cosecant
        x = np.linspace(-6.283, 6.283, 1000)  # 1000 points from -2pi to 2pi
        y = 1 / np.sin(x)  # Compute cosec(x) values
        y = plt.plot(x, y, label='csc(x)')
        # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('csc(x)')
        plt.title('Cosec Function')

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    
    elif n1 == 6:    # secant
        x = np.linspace(-6.283, 6.283, 1000)  # 100 points from -2pi to 2pi
        y = 1 / np.cos(x)  # Compute sec(x) values
        y = plt.plot(x, y, label='sec(x)')
        # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('sec(x)')
        plt.title('Sec Function')
        plt.xticks(list(range(-7, 7, 1)))

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    
    elif n1 == 7:    # sine inverse
        x = np.linspace(-6.283, 6.283, 1000)  # 1000 points from -2pi to 2pi

        y = np.arcsin(x)  # Compute sin^-1(x) values
        y = plt.plot(x, y, label='sin^-1(x)')  # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('sin^-1(x)')
        plt.title('Sin Inverse Function')

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    
    elif n1 == 8:    # cosine inverse
        x = np.linspace(-2, 2, 100)  # 100 points from -2 to 2
        y = np.linspace(-6.283, 6.283, 100)  # 100 points from -2pi to 2pi

        y = np.arccos(x)  # Compute cos^-1(x) values
        y = plt.plot(x, y, label='cos^-1(x)')  # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('cos^-1(x)')
        plt.title('Cos Inverse Function')

        # making markings on the axes
        plt.yticks(list(range(-1, 5, 1)))
        plt.xticks(list(range(-2, 3, 1)))

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    
    elif n1 == 9:    # tangent inverse
        x = np.linspace(-10, 10, 1000)  # 1000 points from -10 to 10
        y = np.linspace(-3.14, 3.14, 1000)  # 1000 points from -pi to pi

        y = np.arctan(x)  # Compute tan^-1(x) values
        y = plt.plot(x, y, label='tan^-1(x)')  # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('tan^-1(x)')
        plt.title('Tan Inverse Function')

        # making markings on the axes
        plt.xticks(list(range(-10, 11, 1)))
        plt.yticks(list(range(-2, 3, 1)))

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    
    elif n1 == 10:    # cotangent inverse
        x = np.linspace(-100, 100, 1000)  # 1000 points from -10 to 10
        y = np.linspace(0, 100, 1000)  # 1000 points from -10 to 10

        y = np.arctan(1 / x)  # Compute cot^-1(x) values as cot^-1(x) = tan^-1(1 / x)
        y = plt.plot(x, y, label='cot^-1(x)')  # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('cot^-1(x)')
        plt.title('Cot Inverse Function')

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    
    elif n1 == 11:    # cosecant inverse
        x = np.linspace(-3, 3, 1000)  # 1000 points from -3 to 3
        y = np.arcsin(1 / x)  # Compute csc^-1(x) values as csc^-1(x) = sin^-1(1 / x)
        y = plt.plot(x, y, label='csc^-1(x)')  # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('csc^-1(x)')
        plt.title('Cosec Inverse Function')

        # making markings on the axes
        plt.xticks(list(range(-3, 4, 1)))

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    
    elif n1 == 12:    # secant inverse
        x = np.linspace(-100, 100, 1000)  # 1000 points from -100 to 100
        y = np.linspace(0, 3.1416, 1000)  # 1000 points from 0 to pi
        y = np.arccos(1 / x)  # Compute sec^-1(x) values as sec^-1(x) = cos^-1(1 / x)
        y = plt.plot(x, y, label='sec^-1(x)')
        # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('sec^-1(x)')
        plt.title('Sec Inverse Function')
        plt.xticks(list(range(-100, 100, 10)))

        plt.grid()  # to show grids
        plt.show()  # to show the plot
# function to display graphs

def get_sup(x):
    normal = "abcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)
# function to convert to superscript

inv = '{}{}'.format(get_sup('-'),get_sup('1'))  # stores ^-1
I = ""                                          # to store the answer

def convert_to_Latex_for_differentials(x):   #Function for differentials conversion to LaTeX.
    mappings = {                             #Mappings corresponding to the LATEX notation for diff. mathematical notations.
            "cos": r"\cos",                  #Converts a mathematical expression to LaTeX format. The mappings here correspondingly
            "sin": r"\sin",                  #point to their values as represented in LaTeX format. For e.g: sin(x) is written as 
            "tan": r"\tan",                  #$\sin{(x)}$. 
            "csc": r"\csc",
            "sec": r"\sec",
            "cot": r"\cot",
            "log": r"\log",
            "sin⁻¹" : r"\sin^{-1}",
            "cos⁻¹" : r"\cos^{-1}",
            "tan⁻¹" : r"\tan^{-1}",
            "cot⁻¹" : r"\cot^{-1}",
            "sec⁻¹" : r"\sec^{-1}",
            "csc⁻¹" : r"\csc^{-1}",
            "√" : r"\sqrt",
            "⁰" : "0",
            "¹" : "1",
            "²" : "2",
            "³" : "3",
            "⁴" : "4",
            "⁵" : "5",
            "⁶" : "6",
            "⁷" : "7",
            "⁸" : "8",
            "⁹" : "9",
            "ˣ" : "x",  
            "⁺" : "+",
            "⁻" : "-",
            "⁼" : "=",
            "⁽" : "(",
            "⁾" : ")",
            "(": r"{(",
            ")": r")}",
            "(e" : r"(\mathrm{e}^",
    }
    
    if "√" in x and "/" in x:                          #Checks if there is square root and fractions in the expression.
        n = x.index('²')                               #Finds the index of any squared expression or value in the expression. Comes handy in converting the inverse trigonometric expressions' differentials.
        if x[n + 1] == ")" or x[n + 1] == "-":         #Checks if there is any parentheses or minus sign after the squaring so as to not count other instances.
            x = x.replace('²', r'^{2}')                #Replaces with the LaTeX format of the square , i.e. , a^{2}.
        expression_list = x.split("/")                 #Splits the expression on basis of the fraction to seperate numerator and denominator into list elements.
        updated_expression_list = []

        for item in expression_list:                   #Iterating in the list splitted earlier.
            updated_item = item                        #Assigning a variable for each iterated item.
            for key, value in mappings.items():        #Iterating through the mappings simultaneously.
                updated_item = updated_item.replace(key, value) #Replacing the values.
            updated_expression_list.append(updated_item)  # Append the updated item to the new list

        st = "$\dfrac{" + updated_expression_list[0] + "}{" + updated_expression_list[1] + "}$"  #final expression

    elif "/" in x:
        expression_list = x.split("/")  # Split the expression correctly into numerator and denominator in list.
        st = "$" + '\dfrac{' + expression_list[0] + "}{" + expression_list[1] + "}" + "$"  #Final expression in form of $\dfrac{num_r}{den_r} 
    else:                                                                                  #where num_r is the expression_list[0] and den_r is the expression_list[1]
        if "²" in x:                    #Checking the squaring index in the string.
            n = x.index('²')            #Finding the index
            if x[n + 1] == ")":         #Condition if there is parentheses after this
                x = x.replace('²', r'^{2}')   #Replacement as earlier
        for key, value in mappings.items():
            x = x.replace(key, value)   #Same replacement as earlier
        st = "$" + x + "$"              #final expression
    
    print(st)                           #printing
    expression = f"{st}"                
    return expression                   #storing and returning the expression in another variable and taking it in f string format

def convert_to_Latex_for_integrals(x):       #Function for differentials conversion to LaTeX.
    mappings = {                             #Mappings corresponding to the LATEX notation for diff. mathematical notations.
            "cos": r"\cos",                  #Converts a mathematical expression to LaTeX format. The mappings here correspondingly
            "sin": r"\sin",                  #point to their values as represented in LaTeX format. For e.g: sin(x) is written as 
            "tan": r"\tan",                  #$\sin{(x)}$. 
            "csc": r"\csc",
            "sec": r"\sec",
            "cot": r"\cot",
            "log": r"\log",
            "sin⁻¹" : r"\sin^{-1}",
            "cos⁻¹" : r"\cos^{-1}",
            "tan⁻¹" : r"\tan^{-1}",
            "cot⁻¹" : r"\cot^{-1}",
            "sec⁻¹" : r"\sec^{-1}",
            "csc⁻¹" : r"\csc^{-1}",
            "√" : r"\sqrt",
            "⁰" : "0",
            "¹" : "1",
            "²" : "2",
            "³" : "3",
            "⁴" : "4",
            "⁵" : "5",
            "⁶" : "6",
            "⁷" : "7",
            "⁸" : "8",
            "⁹" : "9",
            "ˣ" : "x",  
            "⁺" : "+",
            "⁻" : "-",
            "⁼" : "=",
            "⁽" : "(",
            "⁾" : ")",
            "(": r"{(",
            ")": r")}",
            "(e" : r"(\mathrm{e}^",
    }
    
    if "√" in x and "¹" in x:
        expression_list = x[1:-5].split("/")                    #Split the expression correctly into numerator and denominator. 
                                                                #The slicing is for omitting the + C which is the constant of the integration.
        
        
        func_end_idx = (expression_list[0].index("¹"))                  #Finding the "1" superscript for the inverse tangent functions so as to locate their terminating point.
        a = expression_list[0][func_end_idx + 1:]                       #Taking the remaining part of the function after the tangent part enclosed in parentheses. 
                                                                        #Typically if tan^-1(x) is the expression then x is being taken in this variable along with ).
        updated_expression_list = [a[1:] , expression_list[1][:-1]]     #Created new list using a such that it omits ) in both cases.

        for i in range(len(updated_expression_list)):                               
            updated_item = updated_expression_list[i]
            for key, value in mappings.items():
                updated_item = updated_item.replace(key, value)                     #Usual replacement
            updated_expression_list[i] = updated_item

        st = "\dfrac" + updated_expression_list[0] + "{" + updated_expression_list[1] + "}"  #final strin in form of the fraction part as told earlier.
        func = expression_list[0][:func_end_idx + 1]                                         #taking function part
        for key, value in mappings.items():                                                  #replacement occuring
            func = func.replace(key, value)                                                  #omitting the "\" escape sequence 
            func = func.replace('\\\\', '\\')
        num_r = func + "{(" + st + ")}"                                                      #final expression for numerator

        den_r = expression_list[2]                                                           #final expression for denominator 
        for key, value in mappings.items():                                                  #performing replacement in denominator
            den_r = den_r.replace(key, value)   
        final_exp =  "\dfrac" + "{" + num_r + "}" + den_r                                    #final expression
        
        st = '$' + final_exp + x[-4:] + '$'                                                  #final latex expression
    
    elif "/" in x:
        expression_list = x[1:-5].split("/")                            #Split the expression correctly in same way to emit + C
        updated_expression_list = []    

        for item in expression_list:
            updated_item = item
            for key, value in mappings.items():                         #Performing replacements.
                updated_item = updated_item.replace(key, value)

                                                                        #Replace double backslashes with a single backslash
            updated_item = updated_item.replace('\\\\', '\\')           #for avoiding "\" escape sequence.
            updated_expression_list.append(updated_item)

        st = '$' + '\dfrac{' + updated_expression_list[0] + "}" + "{" + updated_expression_list[1] + "}" + x[-4:] + '$'     #final expression
    
    else: 
        n = x.index('²')                           #locating squaring part
        if x[n + 1] == "(":                        #verifying the end of the function
            x = x.replace('²', r'^{2}')            #replacement occurrence

        for key, value in mappings.items():
            x = x.replace(key, value)               #replacement throughtout
        st = "$" + x + "$"                          #final expression
    
    print(st)                                       #final expression stored in string
    expression = f"{st}"
    return expression                               #returning the expression

def display_Latex(expression):               #Function for displaying LaTeX in Matplotlib using only text format.
    plt.text(0.5, 0.5, expression, fontsize=15, ha='center', va='center')  #displaying text. ha is horizontal alignment and va is vertical alignment 
    plt.axis('off')  # Hide the axis                                       #and they move relative to a specified point or bounding box
    plt.show()

print("-" * (len("WELCOME TO THE <insert_a_cool_name_here>. We hope you will enjoy your time here. Please read on the rules") + 20))
print("WELCOME TO THE <insert_a_cool_name_here>. We hope you will like it. Please read on the rules.")
print("-" * (len("WELCOME TO THE <insert_a_cool_name_here>. We hope you will enjoy your time here. Please read on the rules") + 20))

print("RULES")         #Made it user friendly and rules to avoid errors.
print("1. Please read each and every prompt or text message carefully so as to avoid an error.")
print("2. While taking input please use () parentheses to seperate the numerator and the denominator and other function types to avoid BODMAS/PEMDAS confusion. Use it as much as possible.")
print("3. While entering the values especially in the inverse trigonometric functions ensure that the values fall in their respective domains where they return a definite value and not an undefined one.")
print("4. If you want to give a fractional value please enter that value in decimals correct upto 3 decimal places.")
print("5. Complex functions like sin(e^(x)) or sin(x)cos(x) or e^(x)log(x) are not supported as of now in Graphs.")
print("6. If there is a message being displayed 'Code Terminated' then it either means that an invalid choice has been entered or the code was exited due to the choice of user.")
print("7. For entering trignometric functions with common prefixes / suffixes please use 'csc' for cosecant function to avoid confusion with secant.")
print("8  For exponentials use ^ sign.")

n = input("Make sure you have read the above mentioned rules. Do you want to Proceed? (Y/N): ")

while n == 'Y' or n == "y":

    print("SELECT OPERATION TYPE")
    print("MAIN MENU:\n1.Differentiation\n2.Indefinite Integration\n3.Definite Integration\n4.Graphs\n5.Exit")  #Main menu for selecting operation type
    ch1 = int(input("Enter choice: "))

    # Differentiation
    if ch1 == 1:
        print("SELECT FUNCTION TYPE")
        print("1. Trigonometric \n2. Inverse Trigonometric \n3. Polyomial (ax+c)\n4. Logarithmic (log(ax+c))\n5. Exponential (e^(ax+c))")  #Menu for function type

        ch2 = int(input("Enter choice: "))
        a = int(input("Enter value of a: "))
        c = int(input("Enter value of c: "))

        #Common Differentials of functions are stored here in the variable I.
        #Since complex functions will complicate the code we have selected a 
        #general linear implicit expression in all the functions for simplification 
        #purposes. The form is (ax + c) linear form where a and c are constants input by the user.

        if ch2 == 1:  # Trigonometric
            print("SELECT THE APPROPIATE FUNCTION")
            print("MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. csc(ax+c)\n 6. sec(ax+c)")  #Menu for the six trigonometric ratios.
            ch3 = int(input("Enter choice: "))
            exp = f"{a}x+{c}"  # expression variable

            new_expressions_list = []
            expressions_list = [r"\sin{(ax+c)}", r"\cos{(ax+c)}", r"\tan{(ax+c)}", r"\cot{(ax+c)}", r"\csc{(ax+c)}", r"\sec{(ax+c)}"]
            for i in expressions_list:                                  #Common thing in all cases that the choices are written in a list and whatever 
                i = i.replace("ax+c", exp)                              #the user inputs (minus 1) is the choice from list displayed in latex. "ax+c" is
                new_expressions_list.append(i)                          #replaced by the expression input by the user.

            if ch3 == 1:
                I = f"{a}cos({exp})"
            elif ch3 == 2:
                I = f"-{a}sin({exp})"
            elif ch3 == 3:
                I = f"{a}sec²({exp})"      # /u00bx is used for superscripting of x
            elif ch3 == 4:
                I = f"-{a}csc²({exp})"   # /u00bx is used for superscripting of x
            elif ch3 == 5:
                I = f"-{a}csc({exp})cot({exp})"
            elif ch3 == 6:
                I = f"{a}sec({exp})tan({exp})"

            function = new_expressions_list[ch3 - 1]

        elif ch2 == 2:  # inverse trigonometric
            print("SELECT THE APPROPIATE FUNCTION")
            print(f"MENU:\n 1. sin{inv}(ax+c)\n 2. cos{inv}(ax+c)\n 3. tan{inv}(ax+c)\n 4. cot{inv}(ax+c)\n 5. csc{inv}(ax+c)\n 6. sec{inv}(ax+c)") #Menu for the 6 inverse trigonometric functions.
            ch3 = int(input("Enter choice: "))
            exp = f"{a}x+{c}"  # expression variable

            new_expressions_list = []
            expressions_list = [r"\sin^{-1}{(ax+c)}", r"\cos^{-1}{(ax+c)}", r"\tan^{-1}{(ax+c)}", r"\cot^{-1}{(ax+c)}", r"\csc^{-1}{(ax+c)}", r"\sec^{-1}{(ax+c)}"]
            for i in expressions_list:
                i = i.replace("ax+c", exp)
                new_expressions_list.append(i)

            if ch3 == 1:
                I = f"{a}/√(1-({exp})²)"
            elif ch3 == 2:
                I = f"-{a}/√(1-({exp})²)"
            elif ch3 == 3:
                I = f"{a}/(1+({exp})²)"
            elif ch3 == 4:
                I = f"-{a}/(1+({exp})²)"
            elif ch3 == 5:
                I = f"-1/|x|√(({exp})²-1)"
            elif ch3 == 6:
                I = f"1/|x|√(({exp})²-1)"

            function = new_expressions_list[ch3 - 1]

        elif ch2 == 3:  # polynomial of the form ax+c
            exp = f"{a}x + {c}"
            I = str(a)
            function = exp

        elif ch2 == 4:  # logarithmic of the form log(ax+c)
            exp = f"{a}x + {c}"
            I = f"{a}/{a}x+{c}"
            function = r"\log" + "{(" + exp + ")}"
            
        elif ch2 == 5:  # exponential of the form e^(ax+c)
            exp = f"{a}x + {c}"
            I = f'{a}(e'+'{}{}{}{}{}{}'.format(get_sup('('),get_sup(str(a)),get_sup('x'),get_sup('+'),get_sup(str(c)), get_sup(')')) + ")"    #formatting is done for superscripting the expression.
            function = r"\mathrm{e}^{" + exp +"}"
        
        else:
            sys.exit(0)

        LHS = r"\dfrac{d}{dx} \left(" + " " + function + " " + r"\right) " + " " + "=" #LHS showing d/dx of a function is stored here to show later in Matplotlib

    # Indefinite integration
    elif ch1 == 2:
        print("SELECT FUNCTION TYPE")
        print("1. Trigonometric \n2. Inverse Trigonometric \n3. Polyomial (ax+c) \n4. Logarithmic \n5. Exponential")  #Menu for function type

        ch2 = int(input("Enter choice: "))
        
        #Common Integrals of functions are stored here in the variable I.
        #Since complex functions will complicate the code we have selected a 
        #general linear implicit expression in all the functions for simplification 
        #purposes. The form is (ax + c) linear form where a and c are constants input by the user.

        if ch2 == 1:  # trigonometric
            a = int(input("Enter value of a: "))
            c = int(input("Enter value of c: "))
            
            print("SELECT THE APPROPIATE FUNCTION")
            print(f"MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. csc(ax+c)\n 6. sec(ax+c)\n 7. sec(ax+c)tan(ax+c)\n 8. csc(ax+c)cot(ax+c)\n 9. csc{get_sup('2')}(ax+c)\n 10. sec{get_sup('2')}(ax+c)")
            ch3 = int(input("Enter choice: "))
            
            exp = f"{a}x+{c}"  # expression variable
            new_expressions_list = []
            expressions_list = [r"\sin{(ax+c)}", r"\cos{(ax+c)}", r"\tan{(ax+c)}", r"\cot{(ax+c)}", r"\csc{(ax+c)}", r"\sec{(ax+c)}", r"\sec{(ax+c)}\tan{(ax+c)}", r"\csc{(ax+c)}\cot{(ax+c)}", r"\csc^{2}{(ax+c)}", r"\sec^{2}{(ax+c)}"]
            for i in expressions_list:
                i = i.replace("ax+c", exp)
                new_expressions_list.append(i)

            if ch3 == 1:
                I = f"(-cos({exp})/{a}) + C"
            elif ch3 == 2:
                I = f"(sin({exp})/{a}) + C"
            elif ch3 == 3:
                I = f"(-log(|cos({exp})|)/{a}) + C"  # /u00bx is used for superscripting of x
            elif ch3 == 4:
                I = f"(log(|sin({exp})|)/{a}) + C"  # /u00bx is used for superscripting of x
            elif ch3 == 5:
                I = f"(-log(|csc({exp}) + cot({exp})|)/{a}) + C"
            elif ch3 == 6:
                I = f"(-log(|tan({exp}) + sec({exp})|)/{a}) + C"
            elif ch3 == 7:
                I = f"(sec({exp})/{a}) + C"
            elif ch3 == 8:
                I = f"(-csc({exp})/{a}) + C"
            elif ch3 == 9:
                I = f"(-cot({exp})/{a}) + C"
            elif ch3 == 10:
                I = f"(tan({exp})/{a}) + C"

            integrand = new_expressions_list[ch3 - 1]

        elif ch2 == 2:  # inverse trigonometric
            print("SELECT THE APPROPIATE FUNCTION")
            print(f"MENU:\n 1. 1/√(1 - (ax + c){get_sup('2')})\n 2. -1/√(1 - (ax+c){get_sup('2')})\n 3. 1/(b + (ax+c){get_sup('2')})\n 4. -1/(b + (ax+c){get_sup('2')})\n 5. 1/((ax+c)√((ax+c){get_sup('2')} - 1)\n 6. -1/((ax+c)√((ax+c){get_sup('2')}) - 1")
            
            a = int(input("Enter value of a: "))
            c = int(input("Enter value of c: "))
            b = int(input("Enter value of b (valid only for 3. and 4.):"))  #as other functions dont have "b"
            ch3 = int(input("Enter choice: "))
            exp = f"{a}x+{c}"  # expression variable
            
            new_expressions_list = []
            final_expressions_list = []
            expressions_list = [r"\dfrac{1}{\sqrt{1 - (ax + c)^{2}}}", r"\dfrac{-1}{\sqrt{1 - (ax + c)^{2}}}", r"\dfrac{1}{b + (ax + c)^{2}}", r"\dfrac{-1}{b + (ax + c)^{2}}", r"\dfrac{1}{(ax + c)\sqrt{(ax + c)^2 - 1}}", r"\dfrac{-1}{(ax + c)\sqrt{(ax + c)^2 - 1}}"]

            for i in expressions_list:
                i = i.replace("ax + c", exp)
                new_expressions_list.append(i)

            for j in new_expressions_list:
                j = j.replace("b", f"{b}")
                final_expressions_list.append(j)

            if ch3 == 1:
                I = f"(sin{inv}({exp})/{a}) + C"
            elif ch3 == 2:
                I = f"(cos{inv}({exp})/{a}) + C"
            elif ch3 == 3:
                I = f"(tan{inv}(({exp})/√({b}))/({a}√({b}))) + C" 
            elif ch3 == 4:
                I = f"(cot{inv}(({exp})/√({b}))/({a}√({b}))) + C"
            elif ch3 == 5:
                I = f"(sec{inv}({exp})/{a}) + C"
            elif ch3 == 6:
                I = f"(csc{inv}({exp})/{a}) + C"

            integrand = final_expressions_list[ch3 - 1]
            
        elif ch2 == 3:  # polynomial of form (ax+c)
            a = int(input("Enter value of a: "))
            c = int(input("Enter value of c: "))
            
            I = f"{int(a/2) if a % 2 == 0 else (a/2)}x{get_sup('2')} + {c}x + C"
            integrand = f"{a}x + {c}"

        elif ch2 == 4:  # logarithmic of form log(ax+c) and expressions of form 1/(ax+b)
            print("SELECT THE APPROPIATE FUNCTION")
            print(f"MENU:\n1. log(ax + c) \n2. 1/(ax + c) \n3. a{get_sup('x')}")
            ch3 = int(input("Enter choice: "))
            a = int(input("Enter value of a: "))
            c = int(input("Enter value of c (only for 1. and 2.): "))
            exp = f"{a}x+{c}"  # expression variable
            
            expressions_list = [r"\log{(ax + c)}", r"\dfrac{1}{(ax + c)}", r"a^{x}"]
            new_expressions_list = []

            for i in expressions_list:
                i = i.replace("ax + c", exp)
                new_expressions_list.append(i)
            new_expressions_list[2] = new_expressions_list[2].replace("a", f"{a}")
            if ch3 == 1:
                I = f"((({exp})(log({exp})-1))/{a}) + C"
            elif ch3 == 2:
                I = f"(log(|({exp})|)/{a}) + C"
            elif ch3 == 3:
                I = f"({a}{get_sup('x')}/log({a})) + C"

            integrand = new_expressions_list[ch3 - 1]

        elif ch2 == 5:  # exponential of form e^(ax+c)
            a = int(input("Enter value of a: "))
            c = int(input("Enter value of c: "))
            exp = f"{a}x + {c}" 
            I = '((e' + f'{get_sup("(")}' + f'{get_sup(exp)}'+ f'{get_sup(")")}' + f")/{a}) + C"
            
            int_integrand = r"\mathrm{e}^{ax + c}"
            integrand = int_integrand.replace("ax + c", exp)
        
        LHS = r"\int \left(" + " " + integrand + " " + r"\right) \, dx" + " " + "="  #integrand is the function to be integrated and is on LHS with dx being the variable
                                                                                    #with respect to with the function should be integrated. For e.g.: ∫f(x)dx is the 
                                                                                    #general form where f(x) is chosen by the user.

    #Definite integration
    elif ch1 == 3:
        print("SELECT FUNCTION TYPE")
        print("1.Trigonometric\n2.Inverse Trigonometric\n3.Polyomial\n4.Logarithmic\n5.Exponential")

        ch2 = int(input("Enter choice: "))
        a = int(input("Enter value of a: "))
        c = int(input("Enter value of c: "))

        lwr_bound = int(input("Enter lower bound: "))           #lower limit
        upr_bound = int(input("Enter upper bound: "))           #upper limit

        #Common Integrals of functions calculated from upper bound or upper limit
        #to lower bound or lower limit are stored here in the variable I.
        #The general formula or the fundamental theory of Calculus states that
        #If integral of any function f(x) is given from a(lower limit) to b(upper limit)
        #and F(x) is the integral or anti-derivative of the function then the
        # evaluated expression will be F(b) - F(a)
        #Since complex functions will complicate the code we have selected a 
        #general linear implicit expression in all the functions for simplification 
        #purposes. The form is (ax + c) linear form where a and c are constants input by the user.
        #The formula are put here in directly using the math module.

        if ch2 == 1:  # trigonometric
            print("SELECT APPROPIATE FUNCTION")
            print("MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. csc(ax+c)\n 6. sec(ax+c)\n 7. sec(ax+c)tan(ax+c)\n 8. csc(ax+c)cot(ax+c)\n 9. csc\u00b2(ax+c)\n 10. sec\u00b2(ax+c)")
            ch3 = int(input("Enter choice: "))
            exp = f"{a}x + {c}"
            exp_lwr = (a * lwr_bound) + c                           #calculating exp in terms of lower limit of x
            exp_upr = (a * upr_bound) + c                           #calculating exp in terms of upper limit of x
            
            new_expressions_list = []
            expressions_list = [r"\sin{(ax+c)}", r"\cos{(ax+c)}", r"\tan{(ax+c)}", r"\cot{(ax+c)}", r"\csc{(ax+c)}", r"\sec{(ax+c)}", r"\sec{(ax+c)}\tan{(ax+c)}", r"\csc{(ax+c)}\cot{(ax+c)}", r"\csc^{2}{(ax+c)}", r"\sec^{2}{(ax+c)}"]
            for i in expressions_list:
                i = i.replace("ax+c", exp)
                new_expressions_list.append(i)
            
            if ch3 == 1:
                I = (-math.cos(exp_upr)/a) - (-math.cos(exp_lwr)/a)
            elif ch3 == 2:
                I = (math.sin(exp_upr)/a) - (math.sin(exp_lwr)/a)
            elif ch3 == 3:
                I = (-math.log(abs(math.cos(exp_upr)))/a) - (-math.log(abs(math.cos(exp_lwr)))/a)  
            elif ch3 == 4:
                I = (math.log(abs(math.sin(exp_upr)))/a) - (math.log(abs(math.sin(exp_lwr)))/a)   
            elif ch3 == 5:
                I = (-math.log(abs(1 / math.sin(exp_upr) + 1 / math.tan(exp_upr)))/a) - (-math.log(abs(1 / math.sin(exp_lwr) + 1 / math.tan(exp_lwr)))/a)
            elif ch3 == 6:
                I = (-math.log(abs((math.tan(exp_upr) + 1 / math.cos(exp_upr))))/a) - (-math.log(abs((math.tan(exp_lwr) + 1 / math.cos(exp_lwr))))/a)
            elif ch3 == 7:
                I = (1 / math.cos(exp_upr)/a) - (1 / math.cos(exp_lwr)/a)
            elif ch3 == 8:
                I = (-1 / math.sin(exp_upr)/a) - (-1 / math.sin(exp_lwr)/a)
            elif ch3 == 9:
                I = (-1 / math.tan(exp_upr)/a) - (-1/ math.tan(exp_lwr)/a)
            elif ch3 == 10:
                I = (math.tan(exp_upr)/a) - (math.tan(exp_lwr)/a)
            
            integrand = new_expressions_list[ch3 - 1]

        elif ch2 == 2:  # inverse trigonometric
            print("SELECT APPROPIATE FUNCTION")
            print("MENU:\n 1. 1/√(1 - (ax + c)\u00b2)\n 2. -1/√(1 - (ax+c)\u00b2)\n 3. 1/(b + (ax+c)\u00b2)\n 4. -1/(b + (ax+c)\u00b2)\n 5. 1/((ax+c)√((ax+c)\u00b2 - 1)\n 6. -1/((ax+c)√((ax+c)\u00b2) - 1")
            b = int(input("Enter value of b (valid only for 3. and 4.):"))
            ch3 = int(input("Enter choice: "))
            exp_lwr = (a * lwr_bound) + c                           #calculating exp in terms of lower limit of x
            exp_upr = (a * upr_bound) + c                           #calculating exp in terms of upper limit of x
            exp = f"{a}x + {c}"

            new_expressions_list = []
            final_expressions_list = []
            expressions_list = [r"\dfrac{1}{\sqrt{1 - (ax + c)^{2}}}", r"\dfrac{-1}{\sqrt{1 - (ax + c)^{2}}}", r"\dfrac{1}{b + (ax + c)^{2}}", r"\dfrac{-1}{b + (ax + c)^{2}}", r"\dfrac{1}{(ax + c)\sqrt{(ax + c)^2 - 1}}", r"\dfrac{-1}{(ax + c)\sqrt{(ax + c)^2 - 1}}"]

            for i in expressions_list:
                i = i.replace("ax + c", exp)
                new_expressions_list.append(i)

            for j in new_expressions_list:
                j = j.replace("b", f"{b}")
                final_expressions_list.append(j)

            if ch3 == 1:
                I = (math.asin(exp_upr)/a) - (math.asin(exp_lwr)/a)
            elif ch3 == 2:
                I = -(math.acos(exp_upr)/a) - -(math.acos(exp_lwr)/a)
            elif ch3 == 3:
                I = (math.atan((exp_upr)/math.sqrt(b))/(a * math.sqrt(b))) - (math.atan((exp_lwr)/math.sqrt(b))/(a * math.sqrt(b)))
            elif ch3 == 4:
                I = (math.atan(math.sqrt(b)/(exp_upr))/(a * math.sqrt(b))) - (math.atan(math.sqrt(b)/(exp_lwr))/(a * math.sqrt(b)))   #arccot(x) = arctan(1 / x)
            elif ch3 == 5:
                I = (math.acos(1 / exp_upr)/a) - (math.acos(1 / exp_lwr)/a)                                                           #arcsec(x) = arccos(1 / x)
            elif ch3 == 6:
                I = (math.asin(1 / exp_upr)/a) - (math.asin(1 / exp_lwr)/a)                                                           #arccosec(x) = arcsin(1 / x)
        
            integrand = final_expressions_list[ch3 - 1]

        elif ch2 == 3:  # polynomial of form (ax+c)

            I = ((a / 2) * ((upr_bound ** 2) - (lwr_bound ** 2))) + c * (upr_bound - lwr_bound)
            integrand = f"{a}x + {c}"

        elif ch2 == 4:  # logarithmic of form log(ax+c) and expressions of form 1/(ax+b)
            print("SELECT APPROPIATE FUNCTION")
            print(f"MENU:\n 1. log(ax + c) \n2. 1/(ax + c) \n3. a{get_sup('x')}")
            ch3 = int(input("Enter choice: "))
            
            exp = f"{a}x + {c}"
            exp_lwr = (a * lwr_bound) + c                           #calculating exp in terms of lower limit of x
            exp_upr = (a * upr_bound) + c                           #calculating exp in terms of upper limit of x
            
            expressions_list = [r"\log{(ax + c)}", r"\dfrac{1}{(ax + c)}", r"a^{x}"]
            new_expressions_list = []

            for i in expressions_list:
                i = i.replace("ax + c", exp)
                new_expressions_list.append(i)
            new_expressions_list[2] = new_expressions_list[2].replace("a", f"{a}")
            
            if ch3 == 1:
                I = (((exp_upr) * (math.log(exp_upr)-1))/a) - (((exp_lwr) * (math.log(exp_lwr)-1))/a)
            elif ch3 == 2:
                I = (math.log(abs(exp_upr))/a) - (math.log(abs(exp_lwr))/a)
            elif ch3 == 3:
                I = (math.pow(a, upr_bound) / math.log(a)) - (math.pow(a, lwr_bound) / math.log(a))

            integrand = new_expressions_list[ch3 - 1]

        elif ch2 == 5:  # exponential of form e^(ax+c)
            exp = f"{a}x + {c}" 
            exp_lwr = (a * lwr_bound) + c                           #calculating exp in terms of lower limit of x
            exp_upr = (a * upr_bound) + c                           #calculating exp in terms of upper limit of x
            I = ((math.pow((math.e), exp_upr)) / (a)) - ((math.pow((math.e), exp_lwr)) / (a))
            int_integrand = r"\mathrm{e}^{ax + c}"
            integrand = int_integrand.replace("ax + c", exp)
        
        LHS_int = r"\int_{lwr_bound}^{upr_bound} \left(" + " " + integrand + " " + r"\right) \, dx" + " " + "= $" #In latex a definite integral from a to b where 
        LHS_mod = LHS_int.replace("lwr_bound", f"{lwr_bound}")                                                    #a is the lower bound and b is the upper bound is represented 
        LHS = LHS_mod.replace("upr_bound", f"{upr_bound}")                                                        #as \int{a}^{b}. Here replacements have been done to replace the 
                                                                                                                #bounds. 
        
    # Graphs
    elif ch1 == 4:
        print("MENU:\n1. sin(x)\n2. cos(x)\n3. tan(x)\n4. cot(x)\n5. csc(x)\n6. sec(x)\n" + f"7. sin{inv}(x)\n8. cos{inv}(x)\n9. tan{inv}(x)\n10. cot{inv}(x)\n11. csc{inv}(x)\n12. sec{inv}(x)")
        ch2 = int(input("Enter choice: "))
        if ch2 in range(1,13):
            Graph(ch2)
        else:
            print("Code Exited.")

    #The below two else statements terminates the code
    elif ch1 == 5:       
        n = "N"                                    #Sets to N so as to terminate the while loop
        print("Code Terminated.")
        if I == "":
            print("No Mathematical Expression has been evaluated since user has not entered any expression.") #Since I is getting displayed therefore this msg is displayed.
        else:
            print("Displaying latest mathematical notation evaluated ...")

    else:
        n = "N"
        print("Code Terminated.")
        if I == "":
            print("No Mathematical Expression has been evaluated since user has not entered any expression.") #Since I is getting displayed therefore this msg is displayed
        else:
            print("Displaying latest mathematical notation evaluated ...")

    if I != "":
        print("Displaying Mathematical Notation ...")
        print("Answer:" , I)

    else:
        print("Displaying latest mathematical notation evaluated ...")
        print("No Mathematical Expression has been evaluated since user has not entered any expression.")   #Since I is getting displayed therefore this msg is displayed

    if ch1 == 2 or ch1 == 3:                        #For both types of integration
        print("Displaying LaTeX Notation ...")

        if type(I) == int or type(I) == float:      #Checking whether I is integer or float as in case of Indefinite 
            RHS = str(I)                            #Integration it is not.
        else:
            RHS = convert_to_Latex_for_integrals(I)[1:]     #Displaying except the $ at the beginning as there
                                                            #shouldn't be $ in between the equation.
        final_exp = "$" + LHS + " " + RHS                   #Concatenating both LHS and RHS of the equation
                                                            #with $ added at beginning since there is already one at the end
        
        display_Latex(final_exp)                            #function call

    elif ch1 == 1:                                  #For Differentiation
        print("Displaying Latex Notation ... ")

        RHS = convert_to_Latex_for_differentials(I)[1:]     #Same concept as used in Integral's one for $ notation.
        final_exp = "$" + LHS + " " + RHS                   #Final Expression

        display_Latex(final_exp)                            #Function call
