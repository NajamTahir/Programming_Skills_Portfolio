"""
Chapter 3 Ex 5
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
You’ll have to think of someone else to invite.
•Start with your program from Exercise 3-4. 
Add a print() call at the end of your program 
stating the name of the guest who can’t make it.
•Modify your list, replacing the name of the 
guest who can’t make it with the name of the new person you are inviting.
•Print a second set of invitation messages, 
one for each person who is still in your list.
"""
# Initial list of guests
guests = ["Maaz", "Ahmed", "Danyal", "Anas"]

# Print the list of guests
print("Initial List of Guests:")
for guest in guests:
    print(guest)

# Guest who can't make it
guest_cant_make_it = "Charlie"
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new guest
new_guest = "Eve"
guests.remove(guest_cant_make_it)
guests.append(new_guest)

# Print the updated list of guests
print("Updated List of Guests:")
for guest in guests:
    print(guest)

# Print invitation messages for the remaining guests
print("\nNew Invitation Messages:")
for guest in guests:
    print(f"Dear {guest}, you are cordially invited to the dinner. Please join us for a great evening!")
"""
1.We start with an initial list of guests in the guests list.

2.We print the initial list of guests using a for loop.

3.We identify the guest who can't make it to the dinner and store their name in the guest_cant_make_it variable.

4.We remove the guest who can't make it from the guests list and replace them with a new guest, "Eve."

5.We then print the updated list of guests to confirm the change.

6.Finally, we print new invitation messages for the remaining guests in the list.
"""