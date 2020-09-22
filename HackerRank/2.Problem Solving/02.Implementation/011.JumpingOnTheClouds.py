'''
Question : Emma is playing a new mobile game that starts with consecutively numbered clouds. 
           Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud 
           having a number that is equal to the number of the current cloud plus 1 or 2. She must avoid the thunderheads. 
           Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. 
           It is always possible to win the game.
           For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

Link : https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
'''

def jumpingOnClouds(c):
    length = len(c)
    steps , i = 0 , 0
    
    while i<length-1:
        if i < length-2 and c[i+2] == 0: 
            steps = steps + 1
            i = i + 2
        else:
            steps = steps + 1
            i=i+1 

    return steps

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    
    print(result)
