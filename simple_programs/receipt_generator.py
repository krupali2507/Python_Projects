#Simple receipt_generator for general store.
# print quantity wise total and Final total in receipt.

item_list = []
sum = 0

def add_item_to_bill():
    item = input("Enter Item: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter Quantity: "))
    total_item_price = price * quantity
    item_list.append((item,price,quantity,total_item_price))
    
    

def print_bill():
    print("Item  |Price|Quantity|Total_item_price")
    sum = 0
    for item in item_list:
        name,price,quantity,total_item_price = item
        print(f"{name}   |{price}   |{quantity}      |{total_item_price}")
        sum += total_item_price
    return sum

while True:
    userinput = input("Would you like to generate bill(y/n): ").lower()
    if userinput == 'y':
        add_item_to_bill()
        while True:
            anotherinput = input("want to add another item?(y/n): ").lower()
            if anotherinput == 'y':
                add_item_to_bill()
            else:
                sum = print_bill()
                print("--------------------------------------------------------------")
                print(f"Your Total bill is {sum}. Thank you for visiting Shree Ram General store.")
                break
    else:
        print("Thank you for visiting Shree Ram General store.")
        break