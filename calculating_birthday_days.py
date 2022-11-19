from datetime import date
import time

today = date.today()
user_name = input("Enter your name: ")
year_of_birth= int(input('Enter year of birth:'))
month_of_birth= int(input('Enter month of birth:'))
day_of_birth= int(input('Enter day of birth:'))

date_of_birth = date(year_of_birth, month_of_birth, day_of_birth)
my_birthday= date(today.year, month_of_birth, day_of_birth)
if date_of_birth < today:
    days_to_birthday = ((today-my_birthday).days)


else:
    days_to_birthday = ((my_birthday-today).days)


# if my_birthday < today:
    # my_birthday = my_birthday.replace(today.year+1, 11, 20)
    # print(my_birthday)


# print(days_to_birthday)
print(f" Hello {user_name} you were born {date_of_birth} you have {days_to_birthday} to your birthday")