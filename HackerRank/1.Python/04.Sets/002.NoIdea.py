'''
Question : There is an array of n integers. There are also  disjoint sets, A and ,B each containing m integers. 
           You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
           For each i integer in the array, if i belongs to A, you add 1 to your happiness. If i belongs to B, you 
           add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Link : https://www.hackerrank.com/challenges/no-idea/problem
'''

z = input()
array = input().split()
like = set(input().split())
dislike = set(input().split())

print(sum((i in like) - (i in dislike) for i in array))
