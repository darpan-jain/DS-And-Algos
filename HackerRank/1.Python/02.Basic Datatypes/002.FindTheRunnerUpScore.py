'''
Question : Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
           You are given n scores. Store them in a list and find the score of the runner-up.

Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    z=max(arr)
    for i in range(n):
        if z==max(arr):
            arr.remove(max(arr))
    print(max(arr))
   
