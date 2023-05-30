
import datetime

inputDate = input("Введите дату в формате 'dd-mm-yy' : ")

day, month, year = inputDate.split('-')

isValidDate = True
try:
    datetime.datetime(int(year), int(month), int(day))
except ValueError:
    isValidDate = False

if(isValidDate):
    print(inputDate)
else:
    print("Input date is not valid..")