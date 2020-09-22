'''
Question : You are choreographing a circus show with various animals. 
           For one act, you are given two kangaroos on a number line ready to jump in the positive direction.
           1.The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
           2.The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
           You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. 
           If it is possible, return YES, otherwise return NO.

Link : https://www.hackerrank.com/challenges/kangaroo/problem
'''

def kangaroo(x1, v1, x2, v2):
    return 'YES' if (v1 > v2) and (x1 - x2) % (v2 - v1) == 0 else 'NO'

if __name__ == '__main__':

    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    
    print(result)
