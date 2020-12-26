#exploring datetime
import datetime
t = datetime.time(22,24,5)
print(f'User entered time is: {t}')

print(f'\nMinimun time is: {datetime.time.min}')

print(f'\nMaximum time is: {datetime.time.max}')

print(f'\nResolution is: {datetime.time.resolution}')

print(f'\nDate of today is: {datetime.date.today()}')

#changing some aspects of the date variable
d1 = datetime.date(2020,12,26)
print(d1)
d2 = d1.replace(year = 2021)
d3 = d2.replace(month = 8)
d4 = d3.replace(day = 22)
print(d2,d3,d4,sep='\n')

#difference
print(f'Difference between dates {d4} and {d1} is {d4-d1}')