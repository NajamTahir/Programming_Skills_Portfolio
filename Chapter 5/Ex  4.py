"""
Chapter 5 Ex 4
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.
"""
# Create a dictionary of rivers and the countries they run through
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}
# Use a loop to print a sentence about each river
for river, country in rivers.items():
    print(f'The {river} runs through {country}.')
# Use a loop to print the name of each river
print("\nList of rivers:")
for river in rivers.keys():
    print(river)
# Use a loop to print the name of each country
print("\nList of countries:")
for country in rivers.values():
    print(country)
"""
The program defines a dictionary called rivers, where the keys represent the names of rivers, and the values represent the countries through which those rivers flow.

The dictionary rivers includes three river-country pairs: 'Nile' in 'Egypt,' 'Amazon' in 'Brazil,' and 'Yangtze' in 'China.'

The code uses a for loop to iterate through the key-value pairs (river and country) in the rivers dictionary.

Inside the loop, it prints a sentence for each river using an f-string. For example, it prints "The Nile runs through Egypt."

After printing sentences about each river, the program uses a loop to print a list of river names. It iterates through the keys (river names) in the rivers dictionary and prints each river's name.

Following that, another loop is used to print a list of countries. It iterates through the values (country names) in the rivers dictionary and prints each country's name.
"""