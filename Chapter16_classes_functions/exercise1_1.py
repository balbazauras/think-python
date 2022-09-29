class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second

    def print_time(self):
        time_string = "Hours:{:2d}minutes: {} seconds: {}".format(self.hour,self.minute,self.second)
      


def is_after(time1,time2):
    return(time1.hour,time1.minute,time1.second) > (time2.hour,time2.minute,time2.second)

def main():
    time1=Time(12,30,60)
    time2=Time(14,30,60)
    print(is_after(time1,time2))
    
if __name__ == '__main__':
    main()

def increment(time, seconds):
    time.second += seconds
    
    if time.second >= 60:
        time.second = time.second%60
        time.minute +=time.second//60

    if time.minute >= 60:
        time.minute = time.minute%60
        time.hour += time.minute//60
    return time

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time(0,0,0)
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def increment(time, seconds):
    
    return int_to_time(seconds+time_to_int(time))