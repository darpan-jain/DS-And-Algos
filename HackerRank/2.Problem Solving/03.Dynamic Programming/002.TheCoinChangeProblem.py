'''
Question : You are working at the cash counter at a fun-fair, and you have different types of coins available to you in infinite quantities. 
           The value of each coin is already given. Can you determine the number of ways of making change for a particular number of units 
           using the given types of coins? 

Link : https://www.hackerrank.com/challenges/coin-change/problem
'''

def getWays(n, c, m, memo):
    for i in range(m):
        for j in range(c[i] , len(memo)):
            memo[j] += memo[j - c[i]]
    
    return memo[-1]

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().rstrip().split()))
    memo = [0 for _ in range(n+1)]
    memo[0] = 1
    ways = getWays(n , c , m, memo)  
    print(ways)
