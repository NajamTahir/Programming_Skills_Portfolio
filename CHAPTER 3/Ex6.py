"""
Chapter 3 Ex 6
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
•Print a message to each of the two people still on your list, letting them know they’re still invited.
•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.  
"""

# Create a list of people to invite to dinner
guests = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci"]
# Print an invitation message to each person
print("Dinner Invitation:")
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner. Please join us at my place for a delightful evening!")
# Print a message about the limited space
print("\nI'm sorry, but we can only invite two people for dinner.")
# Remove guests one at a time until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, but we can't invite you to dinner this time.")
# Print a message to the two remaining guests
print("\nYou are still invited to dinner:")
for guest in guests:
    print(f"Dear {guest}, you are still invited. Please join us!")
# Clear the list using del
del guests[:]
# Print the empty list to confirm
print("\nList of guests after clearing:", guests)
"""
1.You start with a list called guests containing the names of three guests: Albert Einstein, Marie Curie, and Leonardo da Vinci.

2.The program then prints an invitation message for each person in the guests list using a for loop. It iterates through the list and generates a personalized invitation message for each guest.

3.After sending the invitations, the program prints a message indicating that there's limited space for the dinner party.

4.Next, it enters a while loop, which removes guests one by one using the pop() method until only two names remain in the list. It also prints a message for each removed guest to inform them that they can't be invited this time.

5.Following this, the program prints another message to the two remaining guests, confirming their invitations to the dinner party.

6.To ensure the guest list is empty, you use del to clear the guests list.

7.Finally, the program prints the empty list to confirm that the list is now cleared.
"""