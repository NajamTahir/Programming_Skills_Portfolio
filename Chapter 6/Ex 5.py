"""
Chapter 6 Ex 5
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 
'pastrami' appears in the list at least three times. Add code near the 
beginning of your program to print a message saying the deli has run out 
of pastrami, and then use a while loop to remove all occurrences of 
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end 
up in finished_sandwiches.
"""
# Create a list of sandwich orders with 'pastrami' appearing multiple times
sandwich_orders = ['tuna', 'turkey', 'pastrami', 'club', 'pastrami', 'vegetarian', 'pastrami']
# Create an empty list for finished sandwiches
finished_sandwiches = []
# Print a message indicating that the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.")
# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
# Loop through the sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Take the first order from the list  
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)
# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
"""
The program starts with a list called sandwich_orders, which contains a list of sandwich orders, including 'tuna,' 'turkey,' 'pastrami,' 'club,' 'pastrami,' 'vegetarian,' and 'pastrami.' The 'pastrami' sandwich appears multiple times.

An empty list called finished_sandwiches is created to store finished sandwiches.

The program prints a message: "Sorry, the deli has run out of pastrami." This message informs the customers that the deli no longer has pastrami sandwiches.

The code uses a while loop to check if 'pastrami' is in the sandwich_orders list. As long as 'pastrami' is in the list, it uses .remove('pastrami') to remove all occurrences of 'pastrami' from the list. This simulates the deli running out of pastrami sandwiches.

After removing all occurrences of 'pastrami' from the list, the code proceeds to process the remaining sandwich orders.

The program enters another while loop to process the sandwich orders, similar to the previous example. It takes the first order from the sandwich_orders list, prints a message indicating that the sandwich has been made, and appends the order to the finished_sandwiches list.

The loop continues to process the next order until there are no more orders in the sandwich_orders list.

After all orders have been processed, the program prints a list of finished sandwiches by iterating through the finished_sandwiches list and printing each sandwich.
"""