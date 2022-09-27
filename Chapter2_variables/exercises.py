from cmath import pi
#Calculates volume of a sphere
volume=4/3*pi*5**3
print("Volume of sphere with radius of 5: "+str(volume))

#calculate shipping cost
shipping_cost=3+0.75*59
book_price=24.95*0.6*60
wholesale_cost=shipping_cost+book_price
print ("Total wholesale cost of 60 books: "+str(wholesale_cost))

# initial startig time in seconds
starting_time=(6*60+52)*60
running_time=(8*60+15)*2+(7*60+12)*3
arrival_time=(starting_time+running_time)/3600
print(starting_time)
print(running_time)
print("Arrivalt time: "+str(arrival_time))