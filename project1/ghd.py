Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy

def check_pathagorean(a, b, c):
    return a**2 + b**2 == c**2

for a in range(1, 332):
    for b in range(a+1, int(numpy.ceil((1000-a)/2.-1))):
        c = 1000 - a - b
        if (check_pathagorean(a, b, c)):
            print( a, b, c, a**2, b**2, c**2)
            break