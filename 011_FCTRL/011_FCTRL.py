def trailingZeroFac(x):
    """
    x: int, x >= 0
    Return the number of trailing zeroes of factorial x
    """
    zeroes = 0
    # refer explanation at http://www.purplemath.com/modules/factzero.htm
    while x >= 1:
        zeroes += x / 5
        x /= 5
    return zeroes
    
# get number of test cases
T = int(raw_input())

# initialize list to store N
number = []
# get positive integer number, N of each test cases
for i in range(T):
    number.append(int(raw_input()))

# loop over each test cases, print the number of trailing zeroes of factorial N
for j in range(T):
    print(trailingZeroFac(number[j]))
