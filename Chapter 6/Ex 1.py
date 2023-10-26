"""
Chapter 6 Ex 1
Write a loop that prompts the user to enter a series of pizza 
toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break
    
    print(f"You'll add {topping} to your pizza.")

print("Pizza order completed!")
"""
The code uses a while loop with the condition True, which creates an infinite loop. This loop will continue until it's explicitly exited using the break statement.

Inside the loop, the program prompts the user to enter a pizza topping using the input() function. The entered topping is stored in the topping variable as a string.

The code checks whether the user input (converted to lowercase using lower()) is equal to the string 'quit'. If the user enters 'quit', it breaks out of the loop using the break statement, effectively ending the pizza order.

If the user enters any other topping, the program prints a message using an f-string indicating which topping will be added to the pizza.

The loop continues to prompt for toppings until the user decides to finish the order by entering 'quit'.

Once the user enters 'quit', the code exits the loop and prints "Pizza order completed!" to confirm that the order process has finished.
"""