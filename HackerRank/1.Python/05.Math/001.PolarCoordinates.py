'''
Question : You are given a complex z. Your task is to convert it to polar coordinates.

Link : https://www.hackerrank.com/challenges/polar-coordinates/problem
'''

import cmath

z = complex(input())
print(abs(z))
print(cmath.phase(z))
