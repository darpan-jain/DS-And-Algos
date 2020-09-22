'''
Question : Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. 
           During his last hike he took exactly n steps. For every step he took, he noted if it was an uphill, U, or a downhill, 
           D step. Gary's hikes start and end at sea level and each step up or down represents a 1 unit change in altitude. 
           We define the following terms:
           1. A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and 
              ending with a step down to sea level.
           2. A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and 
              ending with a step up to sea level.
           Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

Link : https://www.hackerrank.com/challenges/counting-valleys/problem
'''

def countingValleys(n, s):
    val , sea = 0 , 0
    for i in s:
        if i == 'U':
            sea = sea + 1
        else:
            sea = sea - 1
        
        if sea == 0 and i == 'U':
            val = val + 1
            
    return val

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    
    print(result)
