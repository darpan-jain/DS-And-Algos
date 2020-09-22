'''
Question : Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
           Print the decimal value of each fraction on a new line with 6 places after the decimal.

Link : https://www.hackerrank.com/challenges/plus-minus/problem
'''

def plusMinus(arr):
    pos , neg , zero =0 , 0 , 0
    for i in arr:
        if i>0:
            pos = pos + 1
        elif i<0:
            neg = neg + 1
        else:
            zero+=1

    print('%.6f'%(pos/len(arr)))
    print('%.6f'%(neg/len(arr)))
    print('%.6f'%(zero/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
