<<<<<<< HEAD
num1 = input("Please enter first number:")
num2 = input("Please enter second number:")
if num1.isnumeric() and num2.isnumeric():
    num1 = float(num1)
    num2 = float(num2)
    if num2 == 0.0:
        print("Error")
    else:
        result = num1 / num2
        print("The result is:", result)
else:
=======
num1 = input("Please enter first number:")
num2 = input("Please enter second number:")
if num1.isnumeric() and num2.isnumeric():
    num1 = float(num1)
    num2 = float(num2)
    if num2 == 0.0:
        print("Error")
    else:
        result = num1 / num2
        print("The result is:", result)
else:
>>>>>>> e340c6d12d116be7b453234c2d68e3ce8eddd4d1
    print("Invalid inputs")