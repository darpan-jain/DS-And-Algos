'''
Question : You have a non-empty set s, and you have to execute N commands given in N lines.
	   The commands will be pop, remove and discard.

Link : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
'''

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    command = input().split()

    if command[0] == 'pop':
        s.pop()

    elif command[0] == 'remove':
        s.remove(int(command[1]))

    else:
        s.discard(int(command[1]))

print(sum(s))
