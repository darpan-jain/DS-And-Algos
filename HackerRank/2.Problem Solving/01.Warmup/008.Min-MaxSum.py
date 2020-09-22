'''
Question : Given five positive integers, find the minimum and maximum values that can be calculated by summing 
           exactly four of the five integers. 
           Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Link : https://www.hackerrank.com/challenges/mini-max-sum/problem
'''

def miniMaxSum(arr):
    s = sum(arr)
    print(s-max(arr) , s-min(arr))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
