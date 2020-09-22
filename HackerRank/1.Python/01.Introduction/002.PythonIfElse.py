'''
Question : Given an integer, n, perform the following conditional actions:
           1.If  is odd, print Weird
           2.If  is even and in the inclusive range of  to 2,5 print Not Weird
           3.If  is even and in the inclusive range of  to 6,20 print Weird
           4.If  is even and greater than 20, print Not Weird

Link : https://www.hackerrank.com/challenges/py-if-else/problem
'''

n = int(input())

if n%2!=0 : 
    print("Weird")
    
elif n%2==0 and n>=2  and n<=5 :
    print("Not Weird") 
    
elif n%2==0 and n>=6 and n<=20 :
    print("Weird")
    
elif n%2==0 and n>20 :
    print("Not Weird")
