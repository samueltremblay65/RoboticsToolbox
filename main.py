from robotics import *

a = [[1, 2, 3]]
b = [[1], [2], [3]]

print("Matrix a: ")
print(a)
print()
print("Matrix b: ")
print(b)
print()

c = matrix_multiply(b,a)

print("Resulting frame: ")
print(c)
