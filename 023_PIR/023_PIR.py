import math
def areaTetrahedron(a, b, c, d, e, f):
    """
    a, b, c, d, e, f: int or float
    refer to http://www.had2know.com/academics/tetrahedron-volume-6-edges.html for the formula to calculate area of tetrahedron
    """
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    # Creates four lists (representing coordinates) containing 3 lists (representing x, y, z of coordinates) initialized to 0
    coordinates = [[0 for i in range(3)] for j in range(4)] 
    # first coordinate is (0, 0, 0)
    coordinates[0][0] = 0
    coordinates[0][1] = 0
    coordinates[0][2] = 0
    # second coordinate
    coordinates[1][0] = 0
    coordinates[1][1] = c
    coordinates[1][2] = 0
    # third coordinate
    y = (a**2 + c**2 - b**2) / (2 * c)
    coordinates[2][1] = y
    x = math.sqrt(a**2 - y**2)
    coordinates[2][0] = x
    coordinates[2][2] = 0
    # fourth coordinate
    q = (c**2 + e**2 - d**2) / (2 * c)
    coordinates[3][1] = q
    p = (a**2 + e**2 - f**2 - 2 * coordinates[3][1] * y) / (2 * x)
    coordinates[3][0] = p
    r = math.sqrt(e**2 - q**2 - p**2)
    coordinates[3][2] = r
    # after getting 4 coordinates, use matrix formula ( one sixth of the determinant of a simplified 3 x 3 matrix) to find area of tetrahedron
    determinant = determinantThreeTimesThreeMatrix((coordinates[0][0] - coordinates[3][0]), (coordinates[1][0] - coordinates[3][0]), (coordinates[2][0] - coordinates[3][0]), (coordinates[0][1] - coordinates[3][1]), (coordinates[1][1] - coordinates[3][1]), (coordinates[2][1] - coordinates[3][1]), (coordinates[0][2] - coordinates[3][2]), (coordinates[1][2] - coordinates[3][2]), (coordinates[2][2] - coordinates[3][2]))
    return (1 / 6.0) * determinant
    
def determinantThreeTimesThreeMatrix(a, b, c, d, e, f, g, h, i):
    """
    a, b, c, d, e, f, g, h, i: float
    Return the determinant of a 3 x 3 matrix
    """
    return (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)
    
# get number of tests
t = int(raw_input())

# initialize matrix of 1000 cases
s = ["a" for x in range(1000)]

# get t numbers of cases, each case has a string of 6 values corresponding to sides of tetrahedron
for i in range(t):
    s[i] = raw_input()
    
# initialize matrix of 1000 cases, each case has 6 values
z = [["" for x in range(6)] for y in range(1000)]

# put each of the six values of each cases into respective matrix
for i in range(t):
    l = 0
    z[i][l] = "" 
    for j in s[i]:
        if j == " ":
            l += 1
        else:
            z[i][l] += j
# prints area of tetrahedron of each cases up to 4 decimal points
for i in range(t):
    print "%.4f" % (areaTetrahedron(z[i][0], z[i][3], z[i][1], z[i][5], z[i][2], z[i][4],))