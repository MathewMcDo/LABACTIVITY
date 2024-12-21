def show_menu():
    print("Welcome to the Food Ordering System!")
    print("Here are the available items:")
    print("1. Burger - $5.50")
    print("2. Pizza - $7.25")
    print("3. Pasta - $6.00")
    print("4. Salad - $4.75")
    print("5. Soda - $1.50")

def get_choice():
    while True:
        choice = input("Enter the number of the item you want to order: ")
        if choice in ['1', '2', '3', '4', '5']:
            return int(choice)
        else:
            print("Invalid choice, please try again.")

def process_payment(total):
    while True:
        payment = float(input(f"The total is ${total}. Please enter your payment: $"))
        if payment >= total:
            return payment
        else:
            print(f"That's not enough money. You need ${total - payment} more.")

def main():
    show_menu()
    
    choice = get_choice()

    if choice == 1:
        item = "Burger"
        price = 5.50
    elif choice == 2:
        item = "Pizza"
        price = 7.25
    elif choice == 3:
        item = "Pasta"
        price = 6.00
    elif choice == 4:
        item = "Salad"
        price = 4.75
    else:
        item = "Soda"
        price = 1.50

    print(f"\nYou ordered a {item}. The total is ${price}.")

    payment = process_payment(price)
    change = payment - price

    if change > 0:
        print(f"Thank you for your payment! Your change is ${change:.2f}.")
    else:
        print("Thank you for your payment!")

    print(f"Enjoy your {item}!")

if __name__ == "__main__":
    main()
