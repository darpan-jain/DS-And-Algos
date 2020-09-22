'''
Question : The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
           Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Link : https://www.hackerrank.com/challenges/finding-the-percentage/problem
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
   
l = list(student_marks[query_name])
no = len(l)
s = sum(l)
ss = s/no
print("{0:.2f}".format(ss))
