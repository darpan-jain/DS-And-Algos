'''
Question : Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
           She tabulates the number of times she breaks her season record for most points and least points in a game. 
           Points scored in the first game establish her record for the season, and she begins counting from there.
           Given Maria's scores for a season, find and print the number of times she breaks her records for most and 
           least points scored during the season.
           
Link : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
'''

def breakingRecords(scores):
    highest  , lowest = 0 , 0
    high , low = scores[0] , scores[0]
    for i in scores[1:]:
        if i>high:
            high = i
            highest+=1

        if i<low:
            low = i
            lowest+=1

    return [highest ,lowest]

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
