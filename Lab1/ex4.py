# Amount of cars.
cars = 100
# Amount of free seats in a car.
space_in_a_car = 4.0
# Amount of drivers.
drivers = 30
# Amount of passengers.
passengers = 90
# Cars not driven is amount of cars - drivers.
cars_not_driven = cars - drivers
#Cars driven is the amount of drivers.
cars_driven = drivers
# The amount of how many passengers there is room for.
carpool_capacity = cars_driven * space_in_a_car
# The average number of people in each car.
average_passengers_per_car = passengers / cars_driven

# The printout.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
