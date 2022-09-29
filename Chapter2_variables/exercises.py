from cmath import pi
#Calculates volume of a sphere
radius=5
volume=4/3*pi*radius**3
print("Volume of sphere with radius of 5: "+str(volume))

#calculate shipping cost
number_of_copies=60
book_cover_price=24.95
book_store_discout=0.4


shipping_cost=3+0.75*59
book_price=book_cover_price*(1-book_store_discout)*number_of_copies
wholesale_cost=shipping_cost+book_price
print ("Total wholesale cost of 60 books: "+str(wholesale_cost))

# initial startig time in seconds

starting_time=(6*60+52)*60
running_time=(8*60+15)*2+(7*60+12)*3
arrival_time=(starting_time+running_time)/3600
print(starting_time)
print(running_time)
print("Arrivalt time: "+str(arrival_time))