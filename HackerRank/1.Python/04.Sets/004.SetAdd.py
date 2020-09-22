'''
Question : Rupal has a huge collection of country stamps. 
           She decided to count the total number of distinct country stamps in her collection. 
           She asked for your help. You pick the stamps one by one from a stack of N country stamps.
           Find the total number of distinct country stamps.

Link : https://www.hackerrank.com/challenges/py-set-add/problem
'''

stamps = set()
for _ in range(int(input())):
    n = input()
    stamps.add(n)
print(len(stamps))
