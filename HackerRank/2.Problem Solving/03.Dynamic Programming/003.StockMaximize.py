'''
Question : Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. 
           (WOT) will be for the next number of days. Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own,
           or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?

Link : https://www.hackerrank.com/challenges/stockmax/problem
'''

def stockmax(prices):
    profit , maximum  = 0 , prices[-1]
    
    for i in range(len(prices)-2 , -1 , -1):
        if prices[i] > maximum:
            maximum = prices[i]
        profit += maximum - prices[i]
    return profit

if __name__ == '__main__':
    t = int(input().strip())
    
    for t_itr in range(t):
        n = int(input().strip())
        prices = list(map(int, input().rstrip().split()))
        result = stockmax(prices)
        print(result)
