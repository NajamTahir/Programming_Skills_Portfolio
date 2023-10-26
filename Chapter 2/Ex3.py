"""
Chapter 2 Ex 3
Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
"""
"""
Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
"""
print("Name with whitespace: \n\n\t    Najam    \n\t")
print("\nName after lstrip():\nNajam")
print("\nName after rstrip():\n\t Najam \n\t")
print("\nName after strip():\nNajam")
"""
1.print("Name with whitespace: \n\n\t Najam \n\t"): This line prints a string with leading and trailing whitespace. The \n characters represent newlines, and the \t characters represent tabs, creating a visually spaced out name, "Najam," with extra whitespace.

2.print("\nName after lstrip():\nNajam"): This line demonstrates the lstrip() method. It removes leading whitespace from the name and prints the result. In this case, it removes the spaces and tabs from the left side of the name, leaving only "Najam."

3.print("\nName after rstrip():\n\t Najam \n\t"): This line shows the use of the rstrip() method. It removes trailing whitespace from the name and prints the result. In this example, it removes the spaces and tabs from the right side of the name, leaving "Najam" surrounded by spaces and tabs.

4.print("\nName after strip():\nNajam"): This part of the code illustrates the strip() method. It removes both leading and trailing whitespace and prints the result. In this case, it removes all the leading and trailing spaces and tabs, leaving just the name "Najam."
"""