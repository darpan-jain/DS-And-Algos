'''
Question : You are given a date. Your task is to find what the day is on that date.

Link : https://www.hackerrank.com/challenges/calendar-module/problem
'''

import calendar
from datetime import date
import datetime

month , day , year = (int(i) for i in input().split(' '))
s = datetime.date(year, month, day) 
print(s.strftime("%A").upper())
