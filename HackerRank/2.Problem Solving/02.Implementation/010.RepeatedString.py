'''
Question : Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
           Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.

Link : https://www.hackerrank.com/challenges/repeated-string/problem
'''

def repeatedString(s, n):
    return s.count('a') * (n // len(s)) + s[ : n % len(s)].count('a')
    
if __name__ == '__main__':
    
    s = input()
    n = int(input())

    result = repeatedString(s, n)
    
    print(result)
