def reverseNum(x):
    """
    x: int
    Reverse the number x, if the reverse of x has leading zeros, the leading zeros are omitted
    """
    # remove any trailing zeros
    while x % 10 == 0:
        x /= 10
    reverse = ""
    while x != 0:
        reverse += str(x % 10)
        x /= 10
    return int(reverse)

# input number of test cases, N
N = int(raw_input())

# initialize list with N number of items
data = ["" for x in range(N)]

# input each test cases into list, data
for i in range(N):
    data[i] = raw_input()

# initialize array with N number of lists, each with 2 items
array = [["" for y in range(2)] for z in range(N)]

# input each number of each test cases into array
for i in range(N):
    index = 0
    for j in data[i]:
        if j == " ":
            index += 1
        else:
            array[i][index] += j
# print the reverse of sum of reverse of the numbers of each case
for i in range(N):
    print(reverseNum(reverseNum(int(array[i][0])) + reverseNum(int(array[i][1]))))