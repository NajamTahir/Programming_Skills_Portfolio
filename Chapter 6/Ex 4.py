"""
Chapter 6 Ex 4
Make a list called sandwich_orders and fill it with the names of various 
sandwiches. Then make an empty list called finished_sandwiches. Loop 
through the list of sandwich orders and print a message for each order,
such as I made your tuna sandwich. As each sandwich is made, move it to 
the list of finished sandwiches. After all the sandwiches have been made, 
print a message listing each sandwich that was made.
"""
# Create a list of sandwich orders
sandwich_orders = ['tuna', 'turkey', 'club', 'vegetarian']
# Create an empty list for finished sandwiches
finished_sandwiches = []
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
The program starts with a list called sandwich_orders, which contains a list of sandwich orders, such as 'tuna,' 'turkey,' 'club,' and 'vegetarian.'

An empty list called finished_sandwiches is created to store finished sandwiches.

The code enters a while loop, and the loop continues as long as there are sandwich orders in the sandwich_orders list (i.e., sandwich_orders is not empty).

Within the loop, the first order from the sandwich_orders list is removed using .pop(0). This simulates the process of preparing the first sandwich order in the queue.

The program prints a message indicating that it has made the sandwich corresponding to the current_order (the order just removed from the list).

The current_order is then appended to the finished_sandwiches list to keep track of the finished orders.

The loop continues to process the next order until there are no more orders in the sandwich_orders list.

After all orders have been processed, the program prints a list of finished sandwiches, iterating through the finished_sandwiches list and printing each sandwich.
"""