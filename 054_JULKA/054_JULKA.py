# number of test cases is T
T = 10

# initialize list x to store number of apples both girls have together for each test cases
x = [0 for i in range(T)]
# initialize list y to store number of apples Klaudia has more for each test cases
y = [0 for i in range(T)]

# get x and y for each test cases
for i in range(T):
    x[i] = int(input())
    y[i] = int(input())

# initialize list k to store number of apples Klaudia has for each test cases
k = [0 for i in range(T)]

# initialize list n to store number of apples Natalia has for each test cases
n = [0 for i in range(T)]

# calculate n and k for each cases, and print k and n for each cases
for i in range(T):
    n[i] = (x[i] - y[i]) / 2
    k[i] = x[i] - n[i]
    print(k[i])
    print(n[i])