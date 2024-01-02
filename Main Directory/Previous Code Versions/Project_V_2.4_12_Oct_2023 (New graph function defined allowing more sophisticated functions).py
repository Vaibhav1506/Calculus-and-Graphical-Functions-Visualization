import numpy as np
import matplotlib.pyplot as plt

def evaluate_math_expression(x):
    st = x        
    mappings = {
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



a = input("Enter expression: ")
s = evaluate_math_expression(a)
print("Displaying Numpy Expression: ")
print(s)

if "⌊" in a or "⌋" in a or "⌈" in a or "⌉" in a:
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


# Adjust the linspace for a better visual representation of the square function
x = n # 100 points from -3 to 3

# Compute function(x) values
y = eval(s)

# Create the plot
plt.plot(x, y, label=f'{a}')

#Axes
plt.axhline(0, color='black', linewidth = 1.5)  # Horizontal line for x-axis
plt.axvline(0, color='black', linewidth = 1.5)  # Vertical line for y-axis

# Add labels and title
plt.xlabel('x')
plt.ylabel(f'{a}')
plt.title(f'Graph of {a}')
plt.xticks(m)  # Adjust x-axis ticks

plt.grid()  # to show grids
plt.legend()  # Show the legend
plt.show()  # to show the plot
