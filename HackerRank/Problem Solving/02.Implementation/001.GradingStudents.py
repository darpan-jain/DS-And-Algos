'''
Question : Sam is a professor at the HackerLand University and likes to round each student's grade according to these rules:
           1.If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
           2.If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

Link : https://www.hackerrank.com/challenges/grading/problem
'''

def gradingStudents(grades):
    for i in grades:
        if i%5 > 2 and i>=38:
            print(i-i%5+5)
        else:
            print(i)  

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    gradingStudents(grades)
