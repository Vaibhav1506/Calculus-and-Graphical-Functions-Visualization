import math
import sys

print("MENU:\n1.Indefinite Integration\n2.Definite Integration")
ch1 = int(input("Enter choice: "))

# Indefinite
if ch1 == 1:
    print("MENU:\n1.Trigonometric Function\n2.Polyomial Function")
    ch2 = int(input("Enter choice: "))
    if ch2 == 1:    # trigonometric
        pass
    elif ch2 == 2:  # polynomial
        pass
    else:
        print("Program Terminated")

# Definite
elif ch1 == 2:
    pass

else:
    print("Program Terminated")