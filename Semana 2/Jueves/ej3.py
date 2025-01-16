option = input("Ingresa que tipo de pizza quieres:\n1-Vegetariana\n2-No Vegetariana\n->")
adicional = ""
if option == "1":
    adicional = input("Ingresa que ingrediente adicional desea agregar a la pizza:\n1-Pimiento\n2-Tofu\n->")
    if adicional == "1":
        adicional = "Pimiento"
    else:
        adicional = "Tofu"
    print(f"La pizza es Vegetariana y tiene los ingredientes: Tomate, Mozzarela y {adicional}")
elif option == "2":
    adicional = input("Ingresa que ingrediente adicional desea agregar a la pizza:\n1-Peperoni\n2-Jamon\n3-Salmon\n->")
    if adicional == "1":
        adicional = "Peperoni"
    elif adicional == "2":
        adicional = "Jamon"
    else:
        adicional = "Salmon"
    print(f"La pizza es no Vegetariana y tiene los ingredientes: Tomate, Mozzarela y {adicional}")
else: 
    print("Invalid option")