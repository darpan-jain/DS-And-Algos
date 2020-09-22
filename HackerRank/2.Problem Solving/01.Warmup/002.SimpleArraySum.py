'''
Question : Given an array of integers, find the sum of its elements.

Link : https://www.hackerrank.com/challenges/simple-array-sum/problem
'''

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)