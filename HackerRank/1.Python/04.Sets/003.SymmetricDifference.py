'''
Question : Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
           The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Link : https://www.hackerrank.com/challenges/symmetric-difference/problem
'''

n = int(input())
N = list(map(int , input().split()))
m = int(input())
M = list(map(int , input().split()))

x = set(N).difference(set(M)) 
y = set(M).difference(set(N)) 
z = sorted(list(x.union(y)))

for i in z:
    print(i)
