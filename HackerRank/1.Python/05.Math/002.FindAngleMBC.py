'''
Question : You are given the lengths AB and BC.
Your task is to find angle MBC (angle theta, as shown in the figure) in degrees.

Link : https://www.hackerrank.com/challenges/find-angle/problem
'''

import math
a = int(input())
b = int(input())

print(round(math.degrees(math.atan(a/b))), u'\N{DEGREE SIGN}' , sep='')
