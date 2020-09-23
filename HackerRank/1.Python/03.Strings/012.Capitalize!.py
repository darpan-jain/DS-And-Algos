'''
Question : You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
           For example, alison heck should be capitalised correctly as Alison Heck.

Link : https://www.hackerrank.com/challenges/capitalize/problem
'''

def solve(s):
    for x in s[:].split(" "): 
        s = s.replace(x , x.capitalize()) 
        s= "".join(s) 
        
    return s
    
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
