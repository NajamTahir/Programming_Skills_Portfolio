"""
Chapter 7 Ex 3
Write a function called make_shirt() that accepts a size and the text 
of a message that should be printed on the shirt. The function should 
print a sentence summarizing the size of the shirt and the message printed 
on it. Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.
"""
def make_shirt(size):
    message = input("Enter the message for the shirt: ")
    print(f"Shirt size: {size}, Message: {message}")
# Call the function using positional arguments to specify the size
size1 = input("Enter the shirt size (e.g., Small, Medium, Large): ")
make_shirt(size1)
# Call the function using keyword arguments to specify the size and message
size2 = input("Enter the shirt size (e.g., Small, Medium, Large): ")
message2 = input("Enter the message for the shirt: ")
make_shirt(size=size2, message=message2)
"""
The make_shirt function is defined, taking one parameter, size, which represents the size of the shirt. Inside the function, it also prompts the user to input a custom message for the shirt.

The function then prints a message that includes the specified size and the custom message entered by the user.

The code calls the make_shirt function twice, demonstrating two different ways to pass arguments:

a. In the first call, the user is prompted to enter the shirt size (size1) using the input() function, and this value is passed as a positional argument to the function. The user is also prompted to enter a custom message inside the function.

b. In the second call, the user is prompted to enter both the shirt size (size2) and a custom message (message2) using the input() function. These values are passed as keyword arguments when calling the function.

In both cases, the function displays the size and message as specified by the user.
"""