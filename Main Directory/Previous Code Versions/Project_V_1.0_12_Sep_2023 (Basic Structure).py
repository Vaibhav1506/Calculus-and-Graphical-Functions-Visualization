# shows use of eval

def function():
    # expression to be evaluated
    expr = input("Enter the function(in terms of x):")

    # variable used in expression
    x = int(input("Enter the value of x:"))

    # evaluating and printing expression
    print("y = ",eval(expr))

function()