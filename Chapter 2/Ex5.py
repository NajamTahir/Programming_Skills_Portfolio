"""
Chapter 2 Ex 5
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.
"""
"""
In this program it calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.
"""
budget = 50
usb_cost = 6
num_usb = budget / usb_cost
pounds_left = budget % usb_cost
print("The girl can buy", num_usb, "USB sticks.")
print("She will have £", pounds_left, "left.")