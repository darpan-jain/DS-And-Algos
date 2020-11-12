'''
Question : You are given a string S.
           Your task is to find out whether S is a valid regex or not.

Link : https://www.hackerrank.com/challenges/incorrect-regex/problem
'''

import re

t = int(input())

for i in range(t):
    s = input()
    try:
        re.compile(s)
        is_valid = True
        
    except re.error:
        is_valid = False
    
    print(is_valid)
