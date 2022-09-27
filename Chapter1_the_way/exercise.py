#convert kilometers to miles
miles=10/1.61
#convert time given in minutes to seconds
time=42*60+42
#calculate the running pace in time per mile
pace=time/miles/60
#average speed in miles per hour
avg_speed=60/pace
print("Average pace in minutes:"+str(pace))
print ("Average speed in miles per hour:"+str(avg_speed)) 

