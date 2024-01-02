import numpy as np
import matplotlib.pyplot as plt

def evaluate_math_expression_to_numpy(x):
    st = x        
    mappings = {
        "[" : "np.abs(",
        "]" : ")",
        "√" : "np.sqrt",
        "⌊" : "np.floor(",  #GIF
        "⌋" : ")",
        "⌈" : "np.ceil(",   #SIF
        "⌉" : ")",
        "sin(": "np.sin(",
        "cos(": "np.cos(",
        "tan(": "np.tan(",
        "cot(": "1 / np.tan(",
        "csc(": "1 / np.sin(",
        "sec(": "1 / np.cos(",
        "sin^-1(" : "np.arcsin(",
        "cos^-1(" : "np.arccos(",
        "tan^-1(" : "np.arctan(",
        "cot^-1(" : "np.arctan(1 / ",
        "sec^-1(" : "np.arccos(1 / ",
        "csc^-1(" : "np.arcsin(1 / ",
        "^" : "**",
        "1x" : "1 * x",
        "2x" : "2 * x",
        "3x" : "3 * x",
        "4x" : "4 * x",
        "5x" : "5 * x",
        "6x" : "6 * x",
        "7x" : "7 * x",
        "8x" : "8 * x",
        "9x" : "9 * x",
        "0x" : "0 * x",
        "πx" : "np.pi * x",
        "ex" : "np.e * x",
        "\bπ\b" : "np.pi",
        "\be\b" : "np.e",
        "log(": "np.log(",
    }
    
    for key, value in mappings.items():
        st = st.replace(key, value)

    return st

def decide_range_of_function(a):
    if "⌊" in a or "⌋" in a or "⌈" in a or "⌉" in a or "[" in a or "]" in a:
        n = np.linspace(-6, 6, 1000)
        m = np.arange(-6, 6, 0.5)
    elif "sin^-1" in a or "cos^-1" in a:
        n = np.linspace(-1, 1, 500)
        m = np.arange(-1, 1, 0.1)
    elif "tan^-1" in a:
        n = np.linspace(-np.pi/2, np.pi/2, 500)
        m = np.arange(-np.pi/2, np.pi/2, 0.1)
    elif "cot^-1" in a:
        n = np.linspace(-np.pi, np.pi, 500)
        m = np.arange(-np.pi, np.pi, 0.1)
    elif "csc^-1" in a:
        n = np.linspace(-np.pi/2, np.pi/2, 500)
        m = np.arange(-np.pi/2, np.pi/2, 0.1)
    elif "sec^-1" in a:
        n = np.linspace(-np.pi/2, np.pi/2, 500)
        m = np.arange(-np.pi/2, np.pi/2, 0.1)
    elif "sin" in a or "cos" in a or "tan" in a or "cot" in a or "sec" in a or "csc" in a:
        n = np.linspace(-10, 10, 100)
        m = np.arange(-10, 10, 1)
    else:
        n = np.linspace(-100, 100, 1000)
        m = np.arange(-1000, 1000, 50)
    return [m,n]

print("Graphing Calculator Gen 2 Prototype for Main Calculus Project")
print("NOTES:")
print("1. Modulus Function should be given using [] and not ||")
print("2. Polynomial Functions can be evaluated in both the choices given.")
print("3. The First one provides a better visualization of naive or simple functions and their roots.")
print("4. If a power's coefficient is missing or not defined then enter 0 while entering the coefficients. For example :- 5x^2 + 0x + 4")
print("5. But the second one provides customization and using other functions implicitly in the polynomial ones.")


print("MENU")
print("1. Polynomial Function (recommended for better visualization Polynomial Functions)")
print("2. Other Functions (Trigonometric, Inverse, Exponential, etc.)")
ch = int(input("Enter choice: "))

if ch == 1:
    deg = int(input("Enter degree (highest power of polynomial): "))
    coefficients = []
    st = ""

    for i in range(deg, 0, -1):
        coeff = int(input(f"Enter the coefficient of x^{i} : "))
        st += str(coeff) + f"x^{i} + "
        coefficients.append(coeff)

    const = int(input("Enter constant (last number) of polynomial: "))
    coefficients.append(const)
    
    final_exp = st + str(const)

    # Calculate the roots of the polynomial
    roots = np.roots(coefficients)
    min_root = np.min(roots)
    max_root = np.max(roots)

    # Generate x-values for plotting based on the roots
    x = np.linspace(min_root - 1, max_root + 1, 1000)

    # Calculate corresponding y-values using the polynomial
    y = np.polyval(coefficients, x)

    # Plot the polynomial function
    plt.plot(x, y, label = f'f(x) = {final_exp}')

    plt.axhline(0, color = 'black', linewidth = 1.5)  # Horizontal line at y = 0 for x-axis
    plt.axvline(0, color = 'black', linewidth = 1.5)  # Vertical line at x = 0 for y-axis

    # Customize the plot
    plt.xlabel('x')
    plt.ylabel(f'{final_exp}')
    plt.title(f'Graph of {final_exp}')

    # Add space to the negative y-axis
    plt.ylim(bottom=min(plt.ylim()[0], -1))

    plt.grid()
    plt.legend()
    plt.show()

elif ch == 2:
    a = input("Enter expression: ")

    s = evaluate_math_expression_to_numpy(a)
    L = decide_range_of_function(a)

    print("Displaying Numpy Expression: ")
    print(s)

    # Adjust the linspace for a better visual representation of the square function
    x = L[1] # 100 points from -3 to 3

    # Compute function(x) values
    y = eval(s)

    # Create the plot
    plt.plot(x, y, label = f'{a}')

    #Axes
    plt.axhline(0, color='black', linewidth = 1.5)  # Horizontal line for x-axis
    plt.axvline(0, color='black', linewidth = 1.5)  # Vertical line for y-axis

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel(f'{a}')
    plt.title(f'Graph of {a}')
    plt.xticks(L[0])  # Adjust x-axis ticks

    plt.grid()  # to show grids
    plt.legend()  # Show the legend
    plt.show()  # to show the plot

else:
    print("Invalid Choice.")