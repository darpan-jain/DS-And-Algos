'''
Question : You are given a string S. 
Suppose a character 'c' occurs consecutively times X in the string. 
Replace these consecutive occurrences of the character 'c' with (X , c) in the string. 

Link : https://www.hackerrank.com/challenges/compress-the-string/problem
'''

from itertools import groupby

print(*[(len(list(s)) , int(k)) for k , s in groupby(input())])
