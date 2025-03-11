def search_in_list(lista, index, number):
    if index == len(lista) - 1:
        if lista[index] == number:
            return number
        else:
            return None
    if lista[index] == number:
        return number
    return search_in_list(lista, index + 1, number) 

def main():
    lista = [1,2,3,4,5,6,7,8,9]
    number_to_find = int(input("Please enter the number:"))
    result = search_in_list(lista, 0, number_to_find)

    if result:
        print(f"The number: {number_to_find} was found")
    else:
        print(f"The number: {number_to_find} was not found")
    
main()