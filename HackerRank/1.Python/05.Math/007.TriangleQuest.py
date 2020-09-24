'''
Question : You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:
           1
           22
           333
           4444
           55555
           ......

Link : https://www.hackerrank.com/challenges/python-quest-1/problem
'''

for i in range(1,int(input())): 
    print(((10**i)//9)*i)
