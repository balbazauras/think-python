#exercise 2
MILES_IN_KILOMETER = 1.61
minutes=42
seconds=42
#convert kilometers to miles
miles=10/MILES_IN_KILOMETER
#convert time given in minutes to seconds
time=minutes*60+seconds
#calculate the running pace in time per mile
pace=time/miles/60
#average speed in miles per hour
avg_speed=60/pace
print("Average pace in minutes:"+str(pace))
print ("Average speed in miles per hour:"+str(avg_speed)) 

