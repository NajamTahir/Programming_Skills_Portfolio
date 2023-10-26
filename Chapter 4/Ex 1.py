"""
Chapter 4 Ex 1
Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.

•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
"""
# Version that passes the if test
alien_color = str(input("Enter the color of alien "))
if alien_color == 'green':
    print("Player just earned 5 points.")
"""
1.It starts by asking the user to input the color of the alien using the input function. The user is prompted to enter the color of the alien.

2.The program stores the user's input in the variable alien_color as a string.

3.It then uses an if statement to check if the alien_color is equal to the string 'green'. If the input matches 'green', the program proceeds to the next line.

4.Inside the if block, the program prints the message "Player just earned 5 points." This message is displayed when the condition in the if statement is true, indicating that the alien is green.

5.If the input color does not match 'green', the program does nothing further, as there is no else or additional elif statement. In this case, no points are awarded, and the program simply ends.
"""