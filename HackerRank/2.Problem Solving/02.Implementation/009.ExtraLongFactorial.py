'''
Question : Calculate and print the factorial of a given integer n.

Link : https://www.hackerrank.com/challenges/extra-long-factorials/problem
'''

def extraLongFactorials(n , memo):
    if n==1 or n==0:
        return 1

    if memo[n]!=0:
        return memo[n]

    fact = n * extraLongFactorials(n-1 , memo)
    memo[n] = fact

    return fact

if __name__ == '__main__':
    n = int(input())

    memo = [0 for _ in range(n+1)]

    s = extraLongFactorials(n , memo)
    
    print(s)
