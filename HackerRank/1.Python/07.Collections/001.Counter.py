'''
Question :  Raghu is a shoe shop owner. His shop has X number of shoes. He has a list containing the size of each shoe he has in his shop.
            There are number N of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.
            Your task is to compute how much money Raghu earned.

Link : https://www.hackerrank.com/challenges/collections-counter/problem
'''

from collections import Counter

x = int(input())                              #Number of Shoes
size = Counter(map(int , input().split()))    #Shoe Sizes
n = int(input())                              #Number of customers
income = 0

for i in range(n):
    s , price = map(int , input().split())    
    if size[s]:
        income = income + price
        size[s] = size[s] - 1
 
print(income)
