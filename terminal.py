from funkcijas import (
    add_client,
    add_order,
    add_product,
    get_clients,
    get_orders,
    get_products,
)

while True:
    print ("\nMAXIMA")
    print("1 - Pievienot klientu")
    print("2 - Pievienot preci")
    print("3 - Pievienot pasūtījumu")
    print("4 - Parādīt pasūtījumu")

    choise = input("Izvele:")

    if choise == "1":
        name = input("Klienta vārds: ")
        surname = input("Klienta uzvārds: ")
        client_id = add_client(name, surname)
        print("Klients pievienot. ID:", client_id)

    elif choise == "2":
        name = input("Preces nosaukums: ")
        price = input("Preces cena: ")
        product_id = add_product(name, price)
        print("Prece pievienota. ID:", product_id)

    elif choise == "3":
        print("\nĶlientu saraksts:")
        for client in get_clients():
            print(client)

        print("\nPreču saraksts:")
        for product in get_products():
            print(product)

        name = input("Klienta ID: ")
        price = input("Preces ID: ")
        order_id = add_order(name, price)
        print("Pasūtījums pievienots. ID:", order_id)

    elif choise == "4":
        print("\nPasūtījumu saraksts:")
        for order in get_orders():
            print(order)

    if choise == "0":
        break
