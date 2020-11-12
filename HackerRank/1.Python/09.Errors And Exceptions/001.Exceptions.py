'''
Question : You are given two values a and b. Perform integer division and print a/b. 
           You havr to take care of various exceptions as well.

Link : https://www.hackerrank.com/challenges/exceptions/problem
'''

t = int(input())

for i in range(t):
    a , b = input().split()
    try:
        print(int(a)//int(b))
    
    except BaseException as e:
        print("Error Code:" , e)
