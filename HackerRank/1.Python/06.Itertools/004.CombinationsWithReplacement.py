'''
Question : You are given a string S. Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

Link : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
'''

from itertools import combinations_with_replacement

s,k = input().split()
print(*["".join(i) for i in combinations_with_replacement(sorted(s) , int(k))], sep="\n")
