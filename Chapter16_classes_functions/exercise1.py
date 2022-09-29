from exercise1_1 import Time, time_to_int,int_to_time

#exercise 1 atros dalies nespratau uzduoties
def mul_time(time,number):
    new_time=int_to_time(time_to_int(time)*number)
    print(new_time)
    return new_time

def main():
    start_time=Time(10,20,30)
    time_ans=mul_time(start_time,3)

    print("Hours: {} Minutes: {} Seconds {}".format(time_ans.hour,time_ans.minute,time_ans.second))
if __name__ == '__main__':
    main()

