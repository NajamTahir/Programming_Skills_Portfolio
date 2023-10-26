"""
Chapter 4 Ex 3
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""
alien_color = str(input("Enter the color of the alien "))
if alien_color == 'green':
    print("Player earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Player earned 10 points for shooting the yellow alien.")
elif alien_color == 'red':
    print("Player earned 15 points for shooting the red alien.")
else:
    print("Player earned 0 points. Invalid alien color.")
"""
1.The program starts by prompting the user to input the color of the alien. The input is read as a string and stored in the variable alien_color.

2.It then uses a series of if, elif, and else statements to check the value of alien_color against different color options.

3.If alien_color is equal to 'green', the program prints the message: "Player earned 5 points for shooting the green alien."

4.If alien_color is equal to 'yellow', the program prints the message: "Player earned 10 points for shooting the yellow alien."

5.If alien_color is equal to 'red', the program prints the message: "Player earned 15 points for shooting the red alien."

6.If alien_color does not match any of the predefined colors, the else block is executed, and the program prints: "Player earned 0 points. Invalid alien color." This provides feedback to the player that the input was not one of the expected colors.
"""