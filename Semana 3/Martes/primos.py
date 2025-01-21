number = int(input("Please enter a number:"))
aux = 2
is_prime = True
if number < 2:
    is_prime = False
else:
    while aux < number:
        if number % aux == 0:
            is_prime = False
            break
        aux += 1
if is_prime:
    print(f"The number {number} is prime")
else:
    print(f"The number {number} is not prime")

