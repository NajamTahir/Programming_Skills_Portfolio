"""
Chapter 3 Ex 2
Start with the list you used in Exercise 1, but instead of just
printing each person’s name, print a message to them. 
The text of each message should be the same, but each message should be
personalized with the person’s name.
"""
#In this program it prints the name with a message giving to them.
names = ["Ahmed","Maaz","Danyal","Amir","Ibrahim"]
print("Message:")
for name in names:
    message = f"hello, {name}! Have a great day."
    print(message)