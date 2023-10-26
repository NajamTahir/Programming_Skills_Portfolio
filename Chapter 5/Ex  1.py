"""
Chapter 5 Ex 1
Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You

should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
"""
person_info = {
    'first_name': str(input("Enter your first name ")),
    'last_name': str(input("Enter your last name ")),
    'age': int(input("Enter your age ")),
    'city': str(input("Where do you live "))
}
# Print each piece of information stored in the dictionary
print("First Name:", person_info['first_name'])
print("Last Name:", person_info['last_name'])
print("Age:", person_info['age'])
print("City:", person_info['city'])
"""
The program first prompts the user to enter their personal information, including:

First name
Last name
Age (which is converted to an integer)
City where they live
The entered information is stored in a dictionary called person_info, with keys representing the different pieces of information and values provided by the user.

The program then prints each piece of information stored in the dictionary using a series of print statements.

Specifically, it prints the following information:

"First Name:" followed by the person's first name.
"Last Name:" followed by the person's last name.
"Age:" followed by the person's age.
"City:" followed by the city where the person lives.
"""