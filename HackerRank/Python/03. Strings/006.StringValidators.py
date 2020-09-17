'''
Question : You are given a string S. Your task is to find out if the string S contains: 
           alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Link : https://www.hackerrank.com/challenges/string-validators/problem
'''

if __name__ == '__main__':
    str = input()
    for i in ('isalnum' , 'isalpha' , 'isdigit','islower', 'isupper'):
        print(any(eval("a." + i + "()") for a in str))
