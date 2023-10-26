"""
Chapter 7 Ex 4
Modify the make_shirt() function so that shirts are large by default with
a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a 
different message.
"""
def make_shirt():
    size = input("Enter the shirt size (e.g., Small, Medium, Large): ")
    message = input("Enter the message for the shirt: ")
    if size.lower() not in ["small", "medium", "large"]:
        print("Invalid shirt size. Defaulting to Large.")
    if not message:
        message = "I love Python"
    print(f"Shirt size: {size}, Message: {message}")
# Create a large shirt with the default message
make_shirt()
# Create a medium shirt with the default message
make_shirt()
# Create a custom-sized shirt with a different message
make_shirt()
"""
The make_shirt() function is defined without any parameters. Inside the function, it prompts the user to input both the shirt size and a custom message.

After taking user input, the code checks the provided shirt size. If the size is not 'Small,' 'Medium,' or 'Large' (case-insensitive), it prints an error message indicating that the size is invalid and defaults to 'Large.'

If no custom message is provided by the user (i.e., the message is an empty string), the code assigns a default message: "I love Python."

Finally, the function prints the shirt size and message, whether they are user-provided or defaulted.

The code then calls the make_shirt() function three times:

a. The first call creates a large shirt with the default message.
b. The second call creates a medium shirt with the default message.
c. The third call creates a custom-sized shirt with a different message (size and message are user-provided).
"""