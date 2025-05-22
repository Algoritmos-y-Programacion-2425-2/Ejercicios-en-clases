def main():
    lista = [6,5,4,1,3,9,8,2]
    selection(lista)
    print(lista)

def selection(lista):
    for i in range(len(lista)): #n
        minor_index = i #n
        for j in range(i+1, len(lista)): #n2
            if lista[j] < lista[minor_index]: #n2
                minor_index = j #n2
        temp = lista[i] #n
        lista[i] = lista[minor_index] #n
        lista[minor_index] = temp #n
        #3n2 + 5n
main()