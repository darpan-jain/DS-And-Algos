'''
Question : Lily has a chocolate bar that she wants to share it with Ron for his birthday. 
           Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that 
           the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. 
           You must determine how many ways she can divide the chocolate.

Link : https://www.hackerrank.com/challenges/the-birthday-bar/problem
'''

def birthday(s, d, m):
    tp = (len(s)-m) + 1 
    return len([1 for i in range(tp) if sum(s[i:i+m])==d])


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])

    result = birthday(s, d, m)
    
    print(result)
