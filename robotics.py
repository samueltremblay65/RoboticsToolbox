from math import sin, asin
from math import cos, acos
from math import pi

def radToDegree(theta):
    return theta / pi * 180

def degreeToRad(theta):
    return theta / 180 * pi

def q2d(x_t, y_t, theta):
    theta = degreeToRad(theta)
    a = [[cos(theta), sin(theta), x_t], [sin(theta), cos(theta), y_t], [0, 0, 1]]
    return a

def inv_q2d(a):
    x = a[0][2]
    y = a[1][2]

    theta = asin(a[0][1])
    
    # Determine the quadrant of the angle
    if(a[0][1] > 0 and a[0][0] > 0):
        # nothing, original quadrant
        print("Quadrant 1")
    
    if(a[0][1] < 0 and a[0][0] > 0):
        # nothing, already correct
        print("Quadrant 2")

    if(a[0][1] > 0 and a[0][0] < 0):
        theta =  pi - theta

    if(a[0][1] < 0 and a[0][0] < 0):
        theta = theta + pi
    
    return {"x": x, "y": y, "theta": radToDegree(theta)}

def q3d():
    print("Not implemented")


def matrix_multiply(a, b):    
    # Check if matrix multiplication is valid
    # If not, print an error message

    a_rows = len(a)
    a_columns = len(a[0])

    b_rows = len(b)
    b_columns = len(b[0])

    if(a_columns != b_rows):
        print("Provided arrays are not compatible for matrix multiplication")

    # If valid, then proceed with multiplication
    c = []

    # Create empty matrix c with correct dimensions
    for i in range(a_rows):
        tmp_list = []
        for j in range(b_columns):
            tmp_list.append(0)
        c.append(tmp_list)

    for i in range(a_rows):
        for j in range(b_columns):
            index = 0
            sum = 0

            for k in range(a_columns):
                sum += a[i][k] * b[k][j]

            c[i][j] = sum
    
    return c


def transform_multiply3d(a,b):
    print("Not implemented")


def inv2d(a):
    print("Not implemented")