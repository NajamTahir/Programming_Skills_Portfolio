"""
Chapter 5 Ex 5
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

each pet
"""
# Create a list of dictionaries representing different pets
pets = [
    {
        'kind': 'Dog',
        'owner': 'Alice'
    },
    {
        'kind': 'Cat',
        'owner': 'Bob'
    },
    {
        'kind': 'Parrot',
        'owner': 'Charlie'
    }
]
# Loop through the list and print information about each pet
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}")
    print()  # Blank line to separate pet information
"""
The program defines a list called pets, where each item in the list is a dictionary representing a different pet. Each dictionary contains two key-value pairs:

'kind': representing the type of animal (e.g., 'Dog', 'Cat', 'Parrot').
'owner': representing the owner's name.
The list pets includes three dictionaries, each representing a different pet, such as a dog owned by Alice, a cat owned by Bob, and a parrot owned by Charlie.

The code uses a for loop to iterate through each dictionary in the pets list.

Inside the loop, it prints information about each pet using the dictionary's key-value pairs. Specifically, it prints:

"Kind of Animal:" followed by the animal's kind (e.g., 'Dog').
"Owner's Name:" followed by the owner's name (e.g., 'Alice').
A blank line is included to separate the information about each pet.
"""