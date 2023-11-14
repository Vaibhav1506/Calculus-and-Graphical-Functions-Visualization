# importing the required module
import matplotlib.pyplot as plt
import numpy as np

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
plt.show()  # to show the plot