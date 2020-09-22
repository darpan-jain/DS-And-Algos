'''
Question : Initialize your list and read in the value of n followed by n lines of commands where each command 
           will be of the 7 types listed above i.e insert, print, remove, append, sort, pop, remove. 
           Iterate through each command in order and perform the corresponding operation on your list.
 
Link : https://www.hackerrank.com/challenges/python-lists/problem
'''

if __name__=='__main__':
    def commdr(lst, instruct): 
        if instruct[0] == 'insert':
            lst.insert(int(instruct[1]), int(instruct[2]))
        elif instruct[0] == 'print':
            print(lst)
        elif instruct[0] == 'remove':
            lst.remove(int(instruct[1]))
        elif instruct[0] == 'append':
            lst.append(int(instruct[1]))
        elif instruct[0] == 'sort':
            lst.sort()
        elif instruct[0] == 'reverse':
            lst.reverse()
        elif instruct[0] == 'pop':
            lst.pop()
        else: 
            print("Command not recognized!")

n = int(input()) 
lst = []
for command in range(0,n):
    temp = [str(i) for i in input().strip().split()]
    commdr(lst, temp)
