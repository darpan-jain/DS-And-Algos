'''
Question : You are given a string S. Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Link : https://www.hackerrank.com/challenges/itertools-permutations/problem
'''

from itertools import permutations

s,k = input().split()
print(*["".join(i) for i in permutations(sorted(s) , int(k))] , sep="\n")
