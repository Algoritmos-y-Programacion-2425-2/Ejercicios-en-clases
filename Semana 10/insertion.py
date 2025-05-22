def main():
    while True:
        lista = [6,5,4,1,3,9,8,2]
        insertion(lista)
        print(lista)

def insertion(lista):
    for i, number in enumerate(lista): #n
        j = i - 1 #n
        while j >=0 and number < lista[j]: #n2
            lista[i] = lista[j] #n2
            lista[j] = number #n2
            i -= 1 #n2
            j -=1 #n2
            #5n2 + 2n = O(n2)
            

main()