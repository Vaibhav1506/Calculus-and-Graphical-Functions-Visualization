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
        print("MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. cosec(ax+c)\n 6. sec(ax+c)")
        ch3 = int(input("Enter choice: "))
        exp = f"{a}x+{c}"  # expression variable
        if ch3 == 1:
            I = f"{a}cos({exp})"
        elif ch3 == 2:
            I = f"-{a}sin({exp})"
        elif ch3 == 3:
            I = f"{a}sec\u00b2({exp})"      # /u00bx is used for superscripting of x
        elif ch3 == 4:
            I = f"-{a}cosec\u00b2({exp})"   # /u00bx is used for superscripting of x
        elif ch3 == 5:
            I = f"-cosec({exp})cot({exp})"
        elif ch3 == 6:
            I = f"sec({exp})tan({exp})"

    elif ch2 == 2:  # inverse trigonometric
        print(f"MENU:\n 1. sin{inv}(ax+c)\n 2. cos{inv}(ax+c)\n 3. tan{inv}(ax+c)\n 4. cot{inv}(ax+c)\n 5. cosec{inv}(ax+c)\n 6. sec{inv}(ax+c)")
        ch3 = int(input("Enter choice: "))
        exp = f"{a}x+{c}"  # expression variable
        if ch3 == 1:
            I = f"{a}/√(1-({exp})\u00b2)"
        elif ch3 == 2:
            I = f"-{a}/√(1-({exp})\u00b2)"
        elif ch3 == 3:
            I = f"{a}/(1+({exp})\u00b2))"
        elif ch3 == 4:
            I = f"-{a}/(1+({exp})\u00b2))"
        elif ch3 == 5:
            I = f"-1/(|x|√(({exp})\u00b2-1)"
        elif ch3 == 6:
            I = f"1/(|x|√(({exp})\u00b2-1)"

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
        print("MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. cosec(ax+c)\n 6. sec(ax+c)\n\
              7. sec(ax+c)tan(ax+c)\n 8. cosec(ax+c)cot(ax+c)\n 9. cosec\u00b2(ax+c)\n 10. sec\u00b2(ax+c)")
        ch3 = int(input("Enter choice: "))
        exp = f"{a}x+{c}"  # expression variable
        if ch3 == 1:
            I = f"-cos({exp})/({a}) + k"
        elif ch3 == 2:
            I = f"-sin({exp}/({a})) + k"
        elif ch3 == 3:
            I = f"(log|sec({exp})|)/({a}) + k"  # /u00bx is used for superscripting of x
        elif ch3 == 4:
            I = f"(log|sin({exp})|)/({a}) + k"  # /u00bx is used for superscripting of x
        elif ch3 == 5:
            I = f"(-log|cosec({exp}) + cot({exp}|)/({a}) + k"
        elif ch3 == 6:
            I = f"(-log|tan({exp}) + sec({exp})|)/({a}) + k"
        elif ch3 == 7:
            I = f"(sec({exp}))/({a}) + k"
        elif ch3 == 8:
            I = f"(-cosec({exp})|)/({a}) + k"
        elif ch3 == 9:
            I = f"(-cot({exp}))/({a}) + k"
        elif ch3 == 10:
            I = f"(tan({exp}))/({a}) + k"

    elif ch2 == 2:  # inverse trigonometric
        inv = '{}{}'.format(get_sup('-'), get_sup('1'))  # stores ^-1
        print("MENU:\n\
            1. 1/√(b\u00b2-(ax + c)\u00b2)\n\
            2. -1/√(b\u00b2-(ax+c)\u00b2)\n\
            3. 1/(b\u00b2+(ax+c)\u00b2)\n\
            4. -1/(b\u00b2+(ax+c)\u00b2)\n\
            5. 1/(x√(b\u00b2+(ax+c)\u00b2)\n\
            6. -1/(x√(b\u00b2+(ax+c)\u00b2)")
        a = int(input("Enter value of a: "))
        c = int(input("Enter value of c: "))
        b = int(input("Enter value of b:"))
        ch3 = int(input("Enter choice: "))
        exp = f"{a}x+{c}"  # expression variable
        if ch3 == 1:
            I = f"sin{inv}({exp}/{b}) + k"
        elif ch3 == 2:
            I = f"cos{inv}({exp}/{b}) + k"
        elif ch3 == 3:
            I = f"(1/{b})tan{inv}({exp}/{b}) + k"
        elif ch3 == 4:
            I = f"(1/{b})cot{inv}({exp}/{b}) + k"
        elif ch3 == 5:
            I = f"(1/{b})sec{inv}({exp}/{b}) + k"
        elif ch3 == 6:
            I = f"(1/{b})cosec{inv}({exp}/{b}) + k"

    elif ch2 == 3:  # polynomial of form (ax+c)
        a = int(input("Enter value of a: "))
        c = int(input("Enter value of c: "))
        I = f"{a/2}x{get_sup('2')} + {c}x + k"

    elif ch2 == 4:  # logarithmic of form log(ax+c) and expressions of form 1/(ax+b)
        print("MENU:\n 1. log(ax + c) \n2. 1/(ax + c)")
        ch3 = int(input("Enter choice: "))
        a = int(input("Enter value of a: "))
        c = int(input("Enter value of c: "))
        exp = f"{a}x+{c}"  # expression variable
        if ch3 == 1:
            I = f"(({exp}(log{exp} - 1))/{a}) + k"
        elif ch3 == 2:
            I = f"log(|{exp}|)/({a}) + k"

    elif ch2 == 5:  # exponential of form e^(ax+c)
        a = int(input("Enter value of a: "))
        c = int(input("Enter value of c: "))
        I = '((e{}{}{}{}'.format(get_sup(str(a)), get_sup('x'), get_sup('+'), get_sup(str(c))) + f')/{a}) + k'

# Definite integration
elif ch1 == 3:
    print("MENU for Definite Integration:")
    print("1.Trigonometric\n2.Inverse Trigonometric\n3.Polyomial\n4.Logarithmic\n5.Exponential")

    ch2 = int(input("Enter choice: "))
    a = int(input("Enter value of a: "))
    c = int(input("Enter value of c: "))

    if ch2 == 1:  # trigonometric
        print("MENU:\n 1. sin(ax+c)\n 2. cos(ax+c)\n 3. tan(ax+c)\n 4. cot(ax+c)\n 5. cosec(ax+c)\n 6. sec(ax+c)\n\
                  7. sec(ax+c)tan(ax+c)\n 8. cosec(ax+c)cot(ax+c)\n 9. cosec\u00b2(ax+c)\n 10. sec\u00b2(ax+c)")
        ch3 = int(input("Enter choice: "))
        exp = f"{a}x+{c}"  # expression variable
        if ch3 == 1:
            I = f"-cos({exp})/({a}) + C"
        elif ch3 == 2:
            I = f"-sin({exp}/({a})) + C"
        elif ch3 == 3:
            I = f"(log|sec({exp})|)/({a}) + C"  # /u00bx is used for superscripting of x
        elif ch3 == 4:
            I = f"(log|sin({exp})|)/({a}) + C"  # /u00bx is used for superscripting of x
        elif ch3 == 5:
            I = f"(-log|cosec({exp}) + cot({exp}|)/({a}) + C"
        elif ch3 == 6:
            I = f"(-log|tan({exp}) + sec({exp})|)/({a}) + C"
        elif ch3 == 7:
            I = f"(sec({exp}))/({a}) + C"
        elif ch3 == 8:
            I = f"(-cosec({exp})|)/({a}) + C"
        elif ch3 == 9:
            I = f"(-cot({exp}))/({a}) + C"
        elif ch3 == 10:
            I = f"(tan({exp}))/({a}) + C"

    elif ch2 == 2:  # inverse trigonometric
        inv = '{}{}'.format(get_sup('-'), get_sup('1'))  # stores ^-1
        print("MENU:\n 1. 1/√(b^2-(ax + c)^2)\n 2. -1/√(b^2-(ax+c)^2)\n 3. 1/(b^2+(ax+c)^2)\n\
                  4. -1/(b^2+(ax+c)^2)\n 5. 1/(x√(b^2+(ax+c)^2)\n 6. -1/(x√(b^2+(ax+c)^2)\n ")
        b = int(input("Enter value of b:"))
        ch3 = int(input("Enter choice: "))
        exp = f"{a}x+{c}"  # expression variable
        if ch3 == 1:
            I = f"sin{inv}({exp}/{b}) + C"
        elif ch3 == 2:
            I = f"cos{inv}({exp}/{b}) + C"
        elif ch3 == 3:
            I = f"(1/{b})tan{inv}({exp}/{b}) + C"
        elif ch3 == 4:
            I = f"(1/{b})cot{inv}({exp}/{b}) + C"
        elif ch3 == 5:
            I = f"(1/{b})sec{inv}({exp}/{b}) + C"
        elif ch3 == 6:
            I = f"(1/{b})cosec{inv}({exp}/{b}) + C"

    elif ch2 == 3:  # polynomial of form (ax+c)
        I = f"({a}x" + get_sup('2') + f")/(2) + {c}x + C"

    elif ch2 == 4:  # logarithmic of form log(ax+c) and expressions of form 1/(ax+b)
        print("MENU:\n 1. log(ax + c) \n2. 1/(ax + c)")
        ch3 = int(input("Enter choice: "))
        exp = f"{a}x+{c}"  # expression variable
        if ch3 == 1:
            I = f"(({exp}(log{exp} - 1))/{a}) + C"
        elif ch3 == 2:
            I = f"log(|{exp}|)/({a}) + C"

    elif ch2 == 5:  # exponential of form e^(ax+c)
        I = '((e' + '{}{}{}{}'.format(get_sup(str(a)), get_sup('x'), get_sup('+'), get_sup(str(c))) + ')/(a)) + C'

# Graphs
elif ch1 == 4:
    print("MENU:\n1. sin(x)\n2. cos(x)\n3. tan(x)\n4. cot(x)\n5. cosec(x)\n6. sec(x)\n"+
          f"7. sin{inv}(x)\n8. cos{inv}(x)\n9. tan{inv}(x)\n10. cot{inv}(x)\n11. cosec{inv}(x)\n12. sec{inv}(x)")
    ch2 = int(input("Enter choice: "))
    if ch2 in range(1,13):
        Graph(ch2)
    else:
        sys.exit()

else:
    sys.exit(0)

print(I)