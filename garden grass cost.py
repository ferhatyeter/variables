#Ferhat Yeter
#16-09-14
#Exercise garden grass cost

garden_length = float(input("Please enter the length of your garden in meters: "))
garden_width = float(input("Please enter the width of your garden in meters: "))
border = float(input("Please enter the border aroud the lawn you dont want to turf: "))

new_garden_length = garden_length - border
new_garden_width = garden_width - border

area = new_garden_length * new_garden_width

cost = area * 10

print("the cost of new turf is: £{0:.0f}.".format(cost))
