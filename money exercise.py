#Ferhat Yeter
#18-09-14
#Money exercise

money = int(input("Please input amount of money: "))

#20
money_20 = money // 20
remainder_20 = money % 20

#10
money_10 = remainder_20 // 10
remainder_10 = remainder_20 % 10

#5
money_5 = remainder_10 // 5
remainder_5 = remainder_10 % 5

#2
money_2 = remainder_5 // 2
remainder_2 = remainder_5 % 2

#1
money_1 = remainder_2 // 1
remainder_1 = remainder_2 % 1



print("You have {0} £20, {1} £10, {2} £5,{3} £2, and {4} £1.".format(money_20,money_10,money_5,money_2,money_1))
