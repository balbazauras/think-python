
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date




def birthday_calculator(birthday):
    delta=datetime.today()-birthday
    
    return delta

def main():

    #exercise 1
    current_date=datetime.today()
    print("ex1: ")
    print (current_date.weekday())

    #exercise 2
    print("ex2:")
    today = date.today()
    birthdate=date(1999,11,29)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    next_bday = birthdate.replace(year=today.year)
    if next_bday < today:
        next_bday = next_bday.replace(year=today.year+1)
    print(next_bday)
    print("You are {} years old and you next birthday will be in {}".format(age, next_bday - today))
    
    #exercise 3
    print("ex3")
    bday1=date(1989,3,12)
    bday2=date(2007,8,30)
    delta1 = min(bday1, bday2)
    delta2 = max(bday1, bday2)
    double_day =   delta2+(delta2 - delta1)
    print (double_day)
if __name__ == '__main__':
    main()

