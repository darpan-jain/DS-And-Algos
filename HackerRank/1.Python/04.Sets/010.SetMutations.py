'''
Question : You are given a set A and N number of other sets. 
           These N number of sets have to perform some specific mutation operations on set A.
           Your task is to execute those operations and print the sum of elements from set A.

Link : https://www.hackerrank.com/challenges/py-set-mutations/problem
'''

(_ , base_set) = (int(input()) , set(map(int, input().split())))
n = int(input())

for _ in range(n):
    (command , up_set) = (input().split()[0] , set(map(int, input().split())))
    getattr(base_set , command)(up_set)

print (sum(base_set))
