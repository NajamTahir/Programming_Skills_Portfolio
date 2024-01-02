# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 03:06:06 2024

@author: lenovo
"""

def calculate_total_price(product_price, quantity):
    return product_price * quantity

def create_billing(product_code, product_price, quantity, payment_method, credit_card_number=None):
    total_price = calculate_total_price(product_price, quantity)

    print("\n********** Billing **********")
    print(f"Product Code: {product_code}")
    print(f"Quantity: {quantity}")
    print(f"Unit Price: ${product_price:.2f}")
    print(f"Total Price: ${total_price:.2f}")
    
    if payment_method == "cash":
        print("Payment Method: Cash")
    elif payment_method == "credit":
        print(f"Payment Method: Credit Card ending in {credit_card_number[-4:]}")

    print("Thank you for shopping with us!")
    print("********** End of Billing **********")

def process_payment(product_price):
    payment_method = input("Choose payment method (cash/credit): ").lower()

    if payment_method == "cash":
        inserted_money = float(input("Insert money: $"))
        if inserted_money == product_price:
            print("Money inserted is correct. Product will be dispensed shortly!")
        elif inserted_money < product_price:
            print("Money inserted is not enough!")
        else:
            change = inserted_money - product_price
            print(f"Money inserted is more than enough! Product and change (${change:.2f}) will be dispensed shortly!")
    elif payment_method == "credit":
        credit_card_number = input("Enter credit card number: ")
        print(f"Payment successful with credit card ending in {credit_card_number[-4:]}. Product will be dispensed shortly!")
    else:
        print("Invalid payment method. Please choose 'cash' or 'credit'.")

def display_products():
    print("\nProduct Price Code")
    print("KitKat   $2    1111")
    print("Coke     $3    2222")
    print("Sprite   $3    3333")
    print("Tea      $1    4444")
    print("Coffee   $1    5555")
    print("Sneakers $2    1234")
    print("Lays     $2    2345")
    print("Milk     $3    3456")
    print("Fanta    $3    4567")
    print("Pepsi    $3    5678")

# New function to calculate order total
def calculate_order_total(order):
    total = 0
    for product_code, quantity in order.items():
        if product_code in product_prices:
            total += product_prices[product_code] * quantity
    return total

# Rest of the code remains unchanged

product_prices = {
    1111: 2,
    2222: 3,
    3333: 3,
    4444: 1,
    5555: 1,
    1234: 2,
    2345: 2,
    3456: 3,
    4567: 3,
    5678: 3
}

order = {}

while True:
    print("Welcome to X's vending machine\n")
    display_products()

    print("\nType a product code to add to your order (or type 'checkout' to proceed to payment, or 'exit' to exit):")
    user_input = input()

    if user_input.lower() == 'exit':
        print("Exiting the vending machine.")
        break
    elif user_input.lower() == 'checkout':
        if not order:
            print("Your order is empty. Please add products before checking out.")
            continue

        total_amount = calculate_order_total(order)
        print(f"\nYour order total is: ${total_amount:.2f}")
        process_payment(total_amount)
        break
    else:
        try:
            user_code = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid product code.")
            continue

        if user_code in product_prices:
            quantity = int(input("Enter the quantity: "))
            order[user_code] = order.get(user_code, 0) + quantity
            print(f"{quantity} units of Product {user_code} added to your order.")
        else:
            print("You have entered an invalid code. Please try again.")
