cars = 100 # amount of the car
space_in_a_car = 4 # amount of the seats in a car
drivers = 30 # amount of the drivers
passengers = 90 # amount of the passengers
cars_not_driven = cars - drivers # amount of the car without drivers
cars_driven = drivers # amount of the car with drivers
carpool_capacity = cars_driven * space_in_a_car # total seats with drivers
average_passengers_per_car = passengers / cars_driven # passengers for each car with driver


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Just try %s more," % "then you can find a way."
print "Hey %s there." % "you"