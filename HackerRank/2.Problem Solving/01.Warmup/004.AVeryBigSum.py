'''
Question : In this challenge, you are required to calculate and print the sum of the elements in an array,
           keeping in mind that some of those integers may be quite large.

Link : https://www.hackerrank.com/challenges/a-very-big-sum/problem
'''

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)
