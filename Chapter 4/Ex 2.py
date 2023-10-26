"""
Chapter 4 Ex 2
Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

•If the alien’s color isn’t green, print a statement that the player just earned 10 points.

•Write one version of this program that runs the if block and another that runs the else block.
"""
# Version that runs the if block (green alien)
alien_color = str(input("Enter the color of alien "))
if alien_color == 'green':
    print("Player just earned 5 points for shooting the green alien.")
else:
    print("Player just earned 10 points.")
"""
1.The program starts by prompting the user to input the color of the alien. The input is read as a string and stored in the variable alien_color.

2.It then checks whether the value stored in alien_color is equal to the string 'green'. This is done using an if statement.

3.If the alien_color is equal to 'green', it means the player has encountered a green alien. In this case, the program prints the message: "Player just earned 5 points for shooting the green alien."

4.If the alien_color is not equal to 'green', it means the player encountered an alien of a different color. In this case, the program prints the message: "Player just earned 10 points."
"""