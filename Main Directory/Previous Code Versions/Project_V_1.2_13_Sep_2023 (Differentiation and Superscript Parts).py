import math
import sys

# function to convert to superscript
def get_sup(x):
    normal = "abcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

I = ""  # to store the answer
print("MENU:\n1.Differentiation\n2.Indefinite Integration\n3.Definite Integration")
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
            I = f"{a}cos({exp})"
        elif ch3 == 3:
            I = f"{a}sec\u00b2({exp})"      # /u00bx is used for superscripting of x
        elif ch3 == 4:
            I = f"-{a}cosec\u00b2({exp})"   # /u00bx is used for superscripting of x
        elif ch3 == 5:
            I = f"-cosec({exp})cot({exp})"
        elif ch3 == 6:
            I = f"sec({exp})tan({exp})"

    elif ch2 == 2:  # inverse trigonometric
        inv = '{}{}'.format(get_sup('-'),get_sup('1'))  # stores ^-1
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


# Definite integration
elif ch1 == 3:
    print("MENU for Definite Integration:")
    print("1.Trigonometric\n2.Inverse Trigonometric\n3.Polyomial\n4.Logarithmic\n5.Exponential")

else:
    sys.exit(0)

print(I)