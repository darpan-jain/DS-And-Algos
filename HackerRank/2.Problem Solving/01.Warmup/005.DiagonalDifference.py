'''
Question : Given a square matrix, calculate the absolute difference between the sums of its diagonals.

Link : https://www.hackerrank.com/challenges/diagonal-difference/problem
'''

def diagonalDifference(arr,n):
    d1 , d2 = 0 , 0
    for i in range(0 , n):
        for j in range (0 , n):
            if i==j:
                d1 = d1 + arr[i][j]
            if i == n-j-1:
                d2 = d2 + arr[i][j]
                   
    return abs(d1-d2)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    print(result)