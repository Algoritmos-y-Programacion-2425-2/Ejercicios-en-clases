money = float(input("Please enter how much money do you want to save:"))
money_year_1 = money * 1.04
money_year_2 = money_year_1 * 1.04
money_year_3 = money_year_2 * 1.04

print("The money after year 1 is: {}".format(round(money_year_1, 2)))
print(f"The money after year 2 is: {round(money_year_2, 2)}")
print(f"The money after year 3 is: {round(money_year_3, 2)}")