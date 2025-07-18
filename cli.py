import requests

BASE = "http://127.0.0.1:5000"

def menu():
    while True:
        print("\n1. View All\n2. View One\n3. Add\n4. Update\n5. Delete\n6. Fetch from API\n0. Exit")
        choice = input("Choice: ")

        if choice == '1':
            print(requests.get(f"{BASE}/inventory").json())
        elif choice == '2':
            id = input("Enter ID: ")
            print(requests.get(f"{BASE}/inventory/{id}").json())
        elif choice == '3':
            name = input("Name: ")
            brand = input("Brand: ")
            barcode = input("Barcode: ")
            stock = int(input("Stock: "))
            price = float(input("Price: "))
            data = {"name": name, "brand": brand, "barcode": barcode, "stock": stock, "price": price}
            print(requests.post(f"{BASE}/inventory", json=data).json())
        elif choice == '4':
            id = input("ID: ")
            field = input("Field to update: ")
            value = input("New value: ")
            value = int(value) if field == 'stock' else float(value) if field == 'price' else value
            print(requests.patch(f"{BASE}/inventory/{id}", json={field: value}).json())
        elif choice == '5':
            id = input("ID: ")
            print(requests.delete(f"{BASE}/inventory/{id}").json())
        elif choice == '6':
            query = input("Enter barcode or product name: ")
            print(requests.get(f"{BASE}/fetch/{query}").json())
        elif choice == '0':
            break

if __name__ == '__main__':
    menu()
