def exponential(base, exp):
    if exp <= 1:
        return base
    return base * exponential(base, exp - 1)
#base * exp(2)
#base * exp(1)


def main():
    base = int(input("Please enter the base:"))
    exp = int(input("Please enter the exp:"))
    result = exponential(base,exp)
    print(result)

    
main()