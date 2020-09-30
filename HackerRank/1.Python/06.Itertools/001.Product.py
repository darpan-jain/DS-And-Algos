'''
Question : You are given a two lists A and B. Your task is to compute their cartesian product A X B.

Link : https://www.hackerrank.com/challenges/itertools-product/problem
'''

from itertools import product

a = map(int , input().split())
b = map(int , input().split())
print(*product(a , b))
