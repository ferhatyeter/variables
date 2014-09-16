#Ferhat Yeter
#16-09-14
#Exercise height and weight conversion


height_inches = float(input("Please enter the height in inches you would like converted into cm: "))
weight_stones = float(input("Please enter the weight in stones you would like converted into kg: "))

height_cm = height_inches * 2.4
weight_kg = weight_stones * 6.364

print("Your height in cm is {0:.2f}.".format(height_cm))
print("Your weight in kg is {0:.2f}.".format(weight_kg))
