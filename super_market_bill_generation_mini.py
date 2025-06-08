from datetime import *

name = input("Enter customer  Name: ")


# List of items
lists = '''
Rice       Rs 10/kg
Sugar      Rs 8/kg
Oil        Rs 30/liter
Salt       Rs 25/kg
Paneer     Rs 40/kg
Maggie     Rs 12/pack
Boost      Rs 200/bottle
'''

# Item rates dictionary
items = {
    'rice': 10,
    'sugar': 8,
    'oil': 30,
    'salt': 25,
    'paneer': 40,
    'maggie': 12,
    'boost': 200
}

# Declaration of variables
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []   # items list
qlist = []   # quantity list
plist = []   # item total price list

while True:
    option = input("\nPress 1 for list or 2 to exit: ")
    if option == '2':
        print("\nThank you for shopping")
        break

    elif option == '1':
        print("\n", lists)

        while True:
            inp1 = input("To buy press 1 or press 2 to exit: ")
            if inp1 == '2':
                print("\nThank you for shopping")
                break

            elif inp1 == '1':
                item = input("Choose your item: ").lower()
                if item in items:
                    while True:
                        quantity_input = input("Enter quantity: ")
                        if quantity_input.isdigit():
                            quantity = int(quantity_input)
                            break
                        else:
                            print("Please enter a valid quantity.")

                    price = quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available. Sorry for the inconvenience.")
            else:
                print("enter a valid number either 1 or 2")
                
        if totalprice > 0:
            tax = (totalprice * 12) / 100
            Finalprice = totalprice + tax

            print("\n" + "=" * 25, "Pythonlife Supermarket", "=" * 25)
            print(" " * 28 + "Hyderabad")
            print(f"date and time is {datetime.now()} ")
            print("Name:", name)
            print("-" * 75)
            print("S.No", " " * 10, "Items", " " * 8, "Quantity", " " * 8, "Price")
            for i in range(len(pricelist)):
                print(i + 1, " " * 13, ilist[i], " " * (12 - len(ilist[i])), qlist[i], " " * 12, plist[i])
            print("-" * 75)
            print(" " * 50, "Total amount: Rs", totalprice)
            print("Tax amount", " " * 50, "Rs", round(tax, 2))
            print("-" * 75)
            print(" " * 50, "Final amount: Rs", round(Finalprice, 2))
            print("-" * 75)
            print(" " * 20, "Thank you & Visit again")
            print("-" * 75)
            break

    else:
        print("Invalid input. Please enter 1 or 2.")
