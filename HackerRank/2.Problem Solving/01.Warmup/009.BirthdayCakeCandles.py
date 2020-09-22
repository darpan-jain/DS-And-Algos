'''
Question : You are in charge of the cake for a child's birthday. 
           You have decided the cake will have one candle for each year of their total age. 
           They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Link : https://www.hackerrank.com/challenges/birthday-cake-candles/problem
'''

def birthdayCakeCandles(ar):
    return ar.count(max(ar))

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
           
    print(result)
