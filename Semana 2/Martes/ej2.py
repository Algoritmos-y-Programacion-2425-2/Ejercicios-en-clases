hours_str = input("Please enter how many hours you worked:")
hours = float(hours_str)
price = float(input("Please enter how much costs your hour (USD):"))
total = hours * price
print(f"Your total income is: ${total}")