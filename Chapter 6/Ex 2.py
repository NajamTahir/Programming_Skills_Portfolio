"""
Chapter 6 Ex 1
A movie theater charges different ticket prices depending
on a person’s age. If a person is under the age of 3, 
the ticket is free; if they are between 3 and 12, the ticket is $10; and if they 
are over age 12, the ticket is $15. Write a loop in which 
you ask users their age, and then tell them the cost of their movie ticket
"""
while True:
    age_str = input("Please enter your age (or 'quit' to exit): ")
    if age_str.lower() == 'quit':
        break
    try:
        age = int(age_str)
        if age < 3:
            ticket_price = 0
        elif 3 >= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15
        print(f"Your movie ticket will cost ${ticket_price}.")
    except ValueError:
        print("Invalid input. Please enter a valid age or 'quit' to exit.")
print("Thank you for using the ticket pricing system!")
"""
The code uses a while loop with the condition True, creating an infinite loop. The loop continues until the user enters 'quit' to exit the system.

Inside the loop, the program prompts the user to enter their age using the input() function. The entered age is stored as a string in the variable age_str.

The code checks if the user entered 'quit' by converting the input to lowercase and comparing it to the string 'quit'. If the user enters 'quit', the loop is exited using the break statement, terminating the program.

If the user enters an age (which should be convertible to an integer), the code attempts to convert the age_str to an integer using a try-except block.

If the age is successfully converted to an integer, the code then checks the age to determine the ticket price:

If the age is less than 3, the ticket price is set to $0.
If the age is between 3 and 12 (inclusive), the ticket price is set to $10.
For ages greater than 12, the ticket price is set to $15.
After determining the ticket price, the program prints a message using an f-string to inform the user of the ticket cost.

If the user enters an age that can't be converted to an integer (e.g., non-numeric input), the code catches the ValueError exception and prints an error message, asking the user to enter a valid age or 'quit' to exit.

The loop continues to prompt for ages or 'quit' until the user decides to finish by entering 'quit'.

After exiting the loop, the program prints "Thank you for using the ticket pricing system!" to acknowledge the end of the interaction.
"""