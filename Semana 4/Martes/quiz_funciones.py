def get_menu_options():
    print("Welcome to UNIMET Store")
    return input("Please enter a option: \n1- See inventory\n2- Purchse\n3- Exit\n->")

def see_inventory(products):
    product_option = input("Please enter a product option to see: \n1- Mobiles\n2- laptops\n3- Back\n->")
    brands = None
    if product_option == "1":
        brands = products.get("mobiles")
    elif product_option == "2":
        brands = products.get("laptops")
    else:
        pass
    if brands != None:
        for brand_name, product_list in brands.items():
            print(brand_name)
            for product in product_list:
                print(f"id:{product.get("id")} - {product.get("name")}: ${product.get("price")} ")
    else:
        pass

def search_product(products, id_product):
    product_option = input("Please enter a product option to purchase: \n1- Mobiles\n2- laptops\n3- Back\n->")
    brands = None
    if product_option == "1":
        brands = products.get("mobiles")
    elif product_option == "2":
        brands = products.get("laptops")
    else:
        pass
    if brands != None:
        for brand_name, product_list in brands.items():
            for product in product_list:
                if product.get("id") == id_product:
                    return product
    else:
        pass

def purchase(products, customers):
    option = input("Do you want to see the inventory first: \n1-Yes\n2-No\n->")
    if option == "1":
        see_inventory(products)
    id_product = int(input("Please enter an id for the product that you want:"))
    product = None
    while product == None:
        product = search_product(products, id_product)
    name= input("Please enter your name:")
    customers.append(
        {
            "name": name,
            "product": product
        }
    )

def main():
    products = {
        "mobiles": {
            "Apple": [
                {
                    "id": 1,
                    "name": "iPhone 7",
                    "price": 300
                },
                {
                    "id": 2,
                    "name": "iPhone 8",
                    "price": 350
                },
                {
                    "id": 3,
                    "name": "iPhone Xr",
                    "price": 450
                },
                {
                    "id": 4,
                    "name": "iPhone Xs",
                    "price": 460
                },
                {
                    "id": 5,
                    "name": "iPhone 11",
                    "price": 900
                },
                {
                    "id": 6,
                    "name": "iPhone 12",
                    "price": 1100
                },
                {
                    "id": 7,
                    "name": "iPhone 13",
                    "price": 1300
                },
            ],
            "Samsung": [
                {
                    "id": 8,
                    "name": "Samsung Galaxy Beam",
                    "price": 150
                },
                {
                    "id": 9,
                    "name": "Samsung Galaxy S6",
                    "price": 200
                },
                {
                    "id": 10,
                    "name": "Samsung Galaxy S7",
                    "price": 300
                },
            ],
            "Xiaomi": [
                {
                    "id": 11,
                    "name": "Xiaomi Redmi Note 8",
                    "price": 250
                },
                {
                    "id": 12,
                    "name": "Xiaomi Redmi Note 8 Pro",
                    "price": 300
                },
            ]
        },
        "laptops": {
            "DELL": [
                {
                    "id": 13,
                    "name": "Dell Inspiron 15",
                    "price": 600
                },
                {
                    "id": 14,
                    "name": "Dell Latitude 14",
                    "price": 650
                },
            ],
            "MAC": [
                {
                    "id": 15,
                    "name": "MacBook Pro 13",
                    "price": 900
                },
                {
                    "id": 16,
                    "name": "MacBook M1",
                    "price": 1500
                },
            ]
        },
    }
    customers = []
    while True:
        option = get_menu_options()
        if option == "1":
            see_inventory(products)
        elif option == "2":
            purchase(products, customers)
            print(customers)
        elif option == "3":
            break
        else:
            print("Invalid option")

main()
            