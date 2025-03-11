def main():
    lista = [6,5,4,1,3,9,8,2]
    selection(lista)
    print(lista)

def selection(lista):
    for i in range(len(lista)):
        minor_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minor_index]:
                minor_index = j
        temp = lista[i]
        lista[i] = lista[minor_index]
        lista[minor_index] = temp

main()