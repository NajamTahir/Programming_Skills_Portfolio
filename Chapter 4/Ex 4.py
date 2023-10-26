"""
Chapter 4 Ex 4
Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

•If the person is less than 2 years old, print a message that the person is a baby.

•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

•If the person is at least 4 years old but less than 13, print a message that the person is a kid.

•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

•If the person is at least 20 years old but less than 65, print a message that the person is an adult.

•If the person is age 65 or older, print a message that the person is an elder.
"""
age =int(input("Enter your age ")) # 
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
"""
1.The program starts by prompting the user to input their age. The input is read as an integer and stored in the variable age.

2.It then uses a series of if, elif, and else statements to check the value of age against different age ranges to determine the person's age group.

3.If age is less than 2, the program prints the message: "The person is a baby." This is the category for infants under 2 years old.

4.If age is between 2 and 3 (exclusive), the program prints the message: "The person is a toddler." This is the category for children between 2 and 3 years old.

5.If age is between 4 and 12 (exclusive), the program prints the message: "The person is a kid." This is the category for children between 4 and 12 years old.

6.If age is between 13 and 19 (exclusive), the program prints the message: "The person is a teenager." This is the category for individuals between 13 and 19 years old.

7.If age is between 20 and 64 (exclusive), the program prints the message: "The person is an adult." This is the category for individuals between 20 and 64 years old.

8.If none of the above conditions match, the else block is executed, and the program prints: "The person is an elder." This is the default category for individuals aged 65 and older.
"""