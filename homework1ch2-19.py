# Pranav Tetali
#ID#1541822


# Coding Problem 1
from datetime import date
def calculateAge(currentDate,birthDate):
    today=currentDate
    age=today.year-birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    return age
original_year=1981
original_month=9
original_day=21
print("Birthday Calculator")
print("Current Day")
month=int(input("Month:"))
day=int(input("Day:"))
year=int(input("Year:"))
print("Birthday")
birthday_month=int(input("Month:"))
birthday_day=int(input("Day:"))
birthday_year=int(input("Year:"))
print("You are", calculateAge(date(year,month,day),date(birthday_year,birthday_month,birthday_day)), "years old.")
if day==birthday_day:
    print("Happy Birthday!")