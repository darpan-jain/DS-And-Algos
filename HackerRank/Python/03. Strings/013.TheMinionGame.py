def minion_game(string):
    p1,p2=0,0
    n=len(string)
    for i in range(n):
        if string[i] in "AEIOU":
            p1+=n-i
        else:
            p2+=n-i
    if p1>p2:
        print("Kevin",p1)
    elif p2>p1:
        print("Stuart",p2)
    else:
        print("Draw")
             
