height = int(input("Please enter the height:"))
aux = 1
cont = 1
is_first_time = True
while aux <= height:
    if is_first_time:
        print(cont)
        is_first_time = False
    else:
        print(cont, end = " ")
        aux2 = cont - 2
        while aux2 >= 1:
            if aux2 == 1:
                print(aux2)
            else:
                print(aux2, end = " ")
            aux2 -= 2   
    aux += 1
    cont += 2