# Mariam Vaid
# 1477614

from datetime import date


def calculate(current, birthdate):
    today = current
    age = today.year - birthdate.year - ((today.Month, today.Day) > (birthdate.month, birthdate.day))
    return age


a = 1981
b = 9
c = 21
print("Birthday Calculator")
print('Current Day')
m = int(input('Month: '))
d = int(input('Day: '))
y = int(input('Year: '))
print('Birthday')
tm = int(input('Month: '))
td = int(input('Day: '))
ty = int(input('Year: '))
print("You are", calculate(date(y, m, a), date(ty, tm, td)), "years old")
if (d == td) and (m == tm):
    print("Happy Birthday!!")
