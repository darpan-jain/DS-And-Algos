'''
Question : Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
           The red region denotes his house, where s is the start point, and t is the endpoint. 
           The apple tree is to the left of his house, and the orange tree is to its right. 
           You can assume the trees are located on a single point, where the apple tree is at point a, 
           and the orange tree is at point b.
           When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. 
           A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means 
           it falls d units to the tree's right. Given the value of d for m apples and n oranges, 
           determine how many apples and oranges will fall on Sam's house (i.e. in the inclusive range [s,t])?

Link : https://www.hackerrank.com/challenges/apple-and-orange/problem
'''

def countApplesAndOranges(s, t, a, b, apples, oranges):
    num_a , num_o = 0 , 0
    for i in apples:
        i = i+a
        if i>=s and i <=t:
            num_a = num_a+1 

    for i in oranges:
        i = i+b
        if i>=s and i <=t:
            num_o = num_o+1 

    print(num_a , num_o , sep='\n')

if __name__ == '__main__':
    
    st = input().split()
    s = int(st[0])
    t = int(st[1])

    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
