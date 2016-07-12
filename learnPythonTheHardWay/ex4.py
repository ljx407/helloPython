# there are 100 cars
cars = 100
# there ara 4 space in each car
space_in_a_car = 4.0
# there ara 30 drivers
drivers = 30
# there are 90 passeages
passengers = 90
# there are only 30 drivers but have 90 cars so 60 cars will stop
cars_not_driven = cars - drivers
# there are 30 drives ,each driver drive a car
cars_driven = drivers
# 30 drives car transport 120 passages
carpoll_capacity = cars_driven * space_in_a_car
# there are 90 passages and 30 cars ,so each car must at least drive 3 passages
average_passengers_per_car = passengers / cars_driven

print "There are", cars ,"cars available."
print "There are only",drivers ,"drivers available."
print "There will be",cars_not_driven,"empth cars today."
print "We car transport",carpoll_capacity,"peaple today."
print "We have",passengers,"to carpoll today."
print "We need to put about",average_passengers_per_car,"in each car."

#study drills
#you use a variable named "car_poll_capacity" in lne 8 , but it cannot define in the context.
