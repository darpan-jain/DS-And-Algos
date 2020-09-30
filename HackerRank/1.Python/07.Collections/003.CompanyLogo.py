'''
Question : A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. 
          They are now trying out various combinations of company names and logos based on this condition. Given a string,
          which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
          1.Print the three most common characters along with their occurrence count.
          2.Sort in descending order of occurrence count.
          3.If the occurrence count is the same, sort the characters in alphabetical order.


Link : https://www.hackerrank.com/challenges/most-commons/problem
'''

from collections import Counter

if __name__ == '__main__':
    s = input()
    k = Counter(sorted(s))
    high = k.most_common(3)
    for i in high:
        print(i[0] , i[1])
