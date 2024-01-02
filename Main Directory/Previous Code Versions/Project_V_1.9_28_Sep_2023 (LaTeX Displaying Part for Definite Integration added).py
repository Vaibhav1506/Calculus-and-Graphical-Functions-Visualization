import matplotlib.pyplot as plt
import numpy as np
import math
import sys

def Graph(n):
    if n == 1:      # sine
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
    elif n == 2:    # cosine
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
    elif n == 3:    # tangent
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
    elif n == 4:    # cotangent
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
    elif n == 5:    # cosecant
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
    elif n == 6:    # secant
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
    elif n == 7:    # sine inv
        x = np.linspace(-6.283, 6.283, 1000)  # 1000 points from -2pi to 2pi

        y = np.arcsin(x)  # Compute sin^-1(x) values
        y = plt.plot(x, y, label='sin^-1(x)')  # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('sin^-1(x)')
        plt.title('Sin Inverse Function')

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    elif n == 8:    # cosine inv
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
    elif n == 9:    # tangent inv
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
    elif n == 10:    # cotangent inv
        x = np.linspace(-100, 100, 1000)  # 1000 points from -10 to 10
        y = np.linspace(0, 100, 1000)  # 1000 points from -10 to 10

        y = np.arctan(1 / x)  # Compute tan^-1(x) values
        y = plt.plot(x, y, label='cot^-1(x)')  # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('cot^-1(x)')
        plt.title('Cot Inverse Function')

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    elif n == 11:    # cosecant inv
        x = np.linspace(-3, 3, 1000)  # 1000 points from -3 to 3
        y = np.arcsin(1 / x)  # Compute csc^-1(x) values
        y = plt.plot(x, y, label='csc^-1(x)')  # Create the plot

        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('csc^-1(x)')
        plt.title('Cosec Inverse Function')

        # making markings on the axes
        plt.xticks(list(range(-3, 4, 1)))

        plt.grid()  # to show grids
        plt.show()  # to show the plot
    elif n == 12:    # secant inv
        x = np.linspace(-100, 100, 1000)  # 1000 points from -100 to 100
        y = np.linspace(0, 3.1416, 1000)  # 1000 points from 0 to pi
        y = np.arccos(1 / x)  # Compute sec^-1(x) values
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

I = ""  # to store the answer

def convert_to_Latex(x):
    mappings = {                             #mappings corresponding to the LATEX notation for diff. mathematical notations.
            "cos": r"\cos",                  #Converts a mathematical expression to LaTeX format.
            "sin": r"\sin",
            "tan": r"\tan",
            "csc": r"\csc",
            "sec": r"\sec",
            "cot": r"\cot",
            "(": r"{(",
            ")": r")}",
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
            "(e" : r"(\mathrm{e}",
    }
    
    if "√" in x and "¹" in x:
        expression_list = x[1:-5].split("/")  # Split the expression correctly
        func_end_idx = (expression_list[0].index("¹"))
        a = expression_list[0][func_end_idx+1:]
        updated_expression_list = [a[1:] , expression_list[1][:-1]]

        for i in range(len(updated_expression_list)):
            updated_item = updated_expression_list[i]
            for key, value in mappings.items():
                updated_item = updated_item.replace(key, value)
            updated_expression_list[i] = updated_item

        st = "\dfrac" + updated_expression_list[0] + "{" + updated_expression_list[1] + "}"
        func = expression_list[0][:func_end_idx + 1]
        for key, value in mappings.items():
            func = func.replace(key, value)
            func = func.replace('\\\\', '\\')
        num_r = func + "{(" + st + ")}"

        den_r = expression_list[2]
        for key, value in mappings.items():
            den_r = den_r.replace(key, value)   
        final_exp =  "\dfrac" + "{" + num_r + "}" + den_r
        
        st = '$' + final_exp + x[-4:] + '$'
    
    elif "/" in x:
        expression_list = x[1:-5].split("/")  # Split the expression correctly
        updated_expression_list = []

        for item in expression_list:
            updated_item = item
            for key, value in mappings.items():
                updated_item = updated_item.replace(key, value)

            # Replace double backslashes with a single backslash
            updated_item = updated_item.replace('\\\\', '\\')
            updated_expression_list.append(updated_item)

        st = '$' + '\dfrac{' + updated_expression_list[0] + "}" + "{" + updated_expression_list[1] + "}" + x[-4:] + '$'
    
    else: 
        n = x.index('²')
        if x[n + 1] == "(":
            x = x.replace('²', r'^{2}')

        for key, value in mappings.items():
            x = x.replace(key, value) 
        st = "$" + x + "$"
    expression = f"{st}"
    return expression

def display_Latex(expression):
    plt.text(0.5, 0.5, expression, fontsize=15, ha='center', va='center')
    plt.axis('off')  # Hide the axis
    plt.show()

print("MENU:\n1.Differentiation\n2.Indefinite Integration\n3.Definite Integration\n4.Graphs")
ch1 = int(input("Enter choice: "))

# Differentiation
if ch1 == 1:
    print("MENU for Differentiation:")
    print("1. Trigonometric (f(ax+c))\n2. Inverse Trigonometric (f(ax+c))\n3. Polyomial (ax+c)\n4. Logarithmic (log(ax+c))\n5. Exponential (e^(ax+c))")
    ch2 = int(input("Enter choice: "))
    a = int(input("Enter value of a: "))
    c = int(input("Enter value of c: "))

    if ch2 == 1:  # trigonometric
        print("MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. csc(ax+c)\n 6. sec(ax+c)")
        ch3 = int(input("Enter choice: "))
        exp = f"{a}x+{c}"  # expression variable
        if ch3 == 1:
            I = f"{a}cos({exp})"
        elif ch3 == 2:
            I = f"-{a}sin({exp})"
        elif ch3 == 3:
            I = f"{a}sec²({exp})"      # /u00bx is used for superscripting of x
        elif ch3 == 4:
            I = f"-{a}csc²({exp})"   # /u00bx is used for superscripting of x
        elif ch3 == 5:
            I = f"-csc({exp})cot({exp})"
        elif ch3 == 6:
            I = f"sec({exp})tan({exp})"

    elif ch2 == 2:  # inverse trigonometric
        print(f"MENU:\n 1. sin{inv}(ax+c)\n 2. cos{inv}(ax+c)\n 3. tan{inv}(ax+c)\n 4. cot{inv}(ax+c)\n 5. csc{inv}(ax+c)\n 6. sec{inv}(ax+c)")
        ch3 = int(input("Enter choice: "))
        exp = f"{a}x+{c}"  # expression variable
        if ch3 == 1:
            I = f"{a}/√(1-({exp})²)"
        elif ch3 == 2:
            I = f"-{a}/√(1-({exp})²)"
        elif ch3 == 3:
            I = f"{a}/(1+({exp})²))"
        elif ch3 == 4:
            I = f"-{a}/(1+({exp})²))"
        elif ch3 == 5:
            I = f"-1/(|x|√(({exp})²-1)"
        elif ch3 == 6:
            I = f"1/(|x|√(({exp})²-1)"

    elif ch2 == 3:  # polynomial of the form ax+c
        I = a

    elif ch2 == 4:  # logarithmic of the form log(ax+c)
        I = f"{a}/{a}x+{c}"

    elif ch2 == 5:  # exponential of the form e^(ax+c)
        I = f'{a}e'+'{}{}{}{}'.format(get_sup(str(a)),get_sup('x'),get_sup('+'),get_sup(str(c)))

    else:
        sys.exit(0)

# Indefinite integration
elif ch1 == 2:
    print("MENU for Indefinite Integration:")
    print("1.Trigonometric\n2.Inverse Trigonometric\n3.Polyomial\n4.Logarithmic\n5.Exponential")

    ch2 = int(input("Enter choice: "))

    if ch2 == 1:  # trigonometric
        a = int(input("Enter value of a: "))
        c = int(input("Enter value of c: "))
        
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
        print(f"MENU:\n 1. 1/√(1 - (ax + c){get_sup('2')})\n 2. -1/√(1 - (ax+c){get_sup('2')})\n 3. 1/(b + (ax+c){get_sup('2')})\n 4. -1/(b + (ax+c){get_sup('2')})\n 5. 1/((ax+c)√((ax+c){get_sup('2')} - 1)\n 6. -1/((ax+c)√((ax+c){get_sup('2')}) - 1")
        
        a = int(input("Enter value of a: "))
        c = int(input("Enter value of c: "))
        b = int(input("Enter value of b (valid only for 3. and 4.):"))
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
        I = '((e' + f'{get_sup(exp)}' + f")/{a}) + C"
        
        int_integrand = r"\mathrm{e}^{ax + c}"
        integrand = int_integrand.replace("ax + c", exp)
    
    LHS = r"\int \left(" + " " + integrand + " " + r"\right) \, dx" + " " + "="

# Definite integration
elif ch1 == 3:
    print("MENU for Definite Integration:")
    print("1.Trigonometric\n2.Inverse Trigonometric\n3.Polyomial\n4.Logarithmic\n5.Exponential")

    ch2 = int(input("Enter choice: "))
    a = int(input("Enter value of a: "))
    c = int(input("Enter value of c: "))

    lwr_bound = int(input("Enter lower bound: "))           #lower limit
    upr_bound = int(input("Enter upper bound: "))           #upper limit
    
    if ch2 == 1:  # trigonometric
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
            I = (((exp_upr)(math.log(exp_upr)-1))/a) - (((exp_lwr)(math.log(exp_lwr)-1))/a)
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
    
    LHS_int = r"\int_{lwr_bound}^{upr_bound} \left(" + " " + integrand + " " + r"\right) \, dx" + " " + "= $"
    LHS_mod = LHS_int.replace("lwr_bound", f"{lwr_bound}")
    LHS = LHS_mod.replace("upr_bound", f"{upr_bound}")
    
# Graphs
elif ch1 == 4:
    print("MENU:\n1. sin(x)\n2. cos(x)\n3. tan(x)\n4. cot(x)\n5. csc(x)\n6. sec(x)\n"+
          f"7. sin{inv}(x)\n8. cos{inv}(x)\n9. tan{inv}(x)\n10. cot{inv}(x)\n11. csc{inv}(x)\n12. sec{inv}(x)")
    ch2 = int(input("Enter choice: "))
    if ch2 in range(1,13):
        Graph(ch2)
    else:
        print("Code Exited.")

else:
    print("Code Exited.")


print("Displaying Mathematical Notation ...")
print("Answer:" , I)

if ch1 == 2 or ch1 == 3:
    print("Displaying LaTeX Notation ...")

    if type(I) == int or type(I) == float:
        RHS = str(I)
    else:
        RHS = convert_to_Latex(I)[1:]

    final_exp = "$" + LHS + " " + RHS

    display_Latex(final_exp)