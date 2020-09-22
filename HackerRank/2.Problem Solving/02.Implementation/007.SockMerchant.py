'''
Question : John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
           Given an array of integers representing the color of each sock, determine how many pairs of socks 
           with matching colors there are.

Link : https://www.hackerrank.com/challenges/sock-merchant/problem
'''

def sockMerchant(n, ar):   
    pair , i = 0,0
    ar.sort()
    
    while i<(n-1):
        if ar[i] == ar[i+1]:
            pair = pair+1
            i=i+2
        else:
            i=i+1
            
    return pair

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
