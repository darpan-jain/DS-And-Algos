'''
Question : You are given a string S. Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Link : https://www.hackerrank.com/challenges/itertools-combinations/problem
'''

from itertools import combinations

s,k = input().split()
for i in range(1 , int(k) + 1):
    for j in combinations(sorted(s) , i):
        print("".join(j))
