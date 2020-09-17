'''
Question : In this challenge, the user enters a string and a substring. 
           You have to print the number of times that the substring occurs in the given string. 
           String traversal will take place from left to right, not from right to left.
           NOTE: String letters are case-sensitive.

Link : https://www.hackerrank.com/challenges/find-a-string/problem
'''

def count_substring(string, sub_string):
    n = 0
    for i in range(0 , len(string)):
        if string[i : len(sub_string) + i] == sub_string:
            n += 1          
    return n
