def factorial(x):
    """
    x: int, x >= 0
    return the factorial of a number, x
    """
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

# user input number of test cases
t = int(raw_input())

# initialize a list that can accomodate t cases
n = [0 for x in range(t)]

# user input number of each test cases
for i in range(t):
    n[i] = int(raw_input())

# calculate factorial of number of each test cases
for i in range(t):
    print(factorial(n[i]))