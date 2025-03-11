def main():
    lista = [6,5,4,1,3,9,8,2]
    lista = quicksort(lista)
    print(lista)

def quicksort(lista):
    if len(lista) < 2:
        return lista
    minor, pivot, greater = partition(lista)
    return quicksort(minor) + [pivot] + quicksort(greater)
    

def partition(lista):
    minor = []
    greater = []
    pivot = lista[0]
    for i in range(len(lista)):
        if lista[i] < pivot:
            minor.append(lista[i])
        elif lista[i] > pivot:
            greater.append(lista[i])

    return minor, pivot, greater

main()