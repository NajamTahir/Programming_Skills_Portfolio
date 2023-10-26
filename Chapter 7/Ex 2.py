"""
Chapter 7 Ex 2
Write a function called favorite_book() that accepts one parameter, 
title. The function should print a message, such as One of my 
favorite books is Alice in Wonderland. Call the function, making 
sure to include a book title as an argument in the function call.
"""
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
# Call the function with a book title
favorite_book("Alice in Wonderland")
"""
The code defines the favorite_book function using the def keyword. It specifies a single parameter, title, which represents the title of the favorite book.

Inside the favorite_book function, there is a print() statement that uses an f-string to generate and display a message. The message indicates that one of the favorite books is the book with the provided title.

After defining the function, the code calls the favorite_book() function with the argument "Alice in Wonderland." This means it's providing the title of one of the favorite books to the function.

When the function is called, it prints the message: "One of my favorite books is Alice in Wonderland."
"""