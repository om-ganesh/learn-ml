# variable assignment and data types
x = 2.5
print(type(x))

# method indentation
if ( x > 0):
    print("x is positive")

# operator knows the operands to decide operator
y = x * 2
z = "hello" * 2
print("int v/s string multiply:", y, z)

# builtin math functions
y = min(-5,8)
y = abs(y)
print("y after min and absolute:", y)

# Python tuples
a = [2,3,4]
b = [5,6,7]
a,b = b,a
print("swap array", a)


# reading python help about in-build functions
help(abs)

# defining help for your own methods
def my_average(a,b,c):
    """Return average of 3 given integers
    """
    return (a+b+c)/3

help(my_average)

# print number and array with separator
print(3,4,sep='>')
x = [5,6,7]
print('|'.join(map(str,x)))


# number can be rounder by positive or negative
print(round(1234.5678,2))
print(round(1251.5678,-2))
print(round(1237.5678,-1))