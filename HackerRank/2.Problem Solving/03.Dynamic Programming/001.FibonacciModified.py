'''
Question : Given three integers, t1, t2, and n, compute and print the nth term of a modified Fibonacci sequence.

Link : https://www.hackerrank.com/challenges/fibonacci-modified/problem
'''

def fibonacciModified(t1, t2, n , memo):
    if n<=2:
        return memo[n-1]

    else:
        for i in range(n-2):
            memo.append(memo[-2] + memo[-1]**2)

    return memo[-1]

if __name__ == '__main__':

    t1T2n = input().split()
    t1 = int(t1T2n[0])
    t2 = int(t1T2n[1])
    n = int(t1T2n[2])

    memo = [t1,t2]

    result = fibonacciModified(t1, t2, n, memo)
    
    print(result)
