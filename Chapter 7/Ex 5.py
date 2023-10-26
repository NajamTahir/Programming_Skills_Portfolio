"""
Chapter 7 Ex 5
Write a function called describe_city() that accepts the name of 
a city and its country. The function should print a simple sentence, 
such as Reykjavik is in Iceland. Give the parameter for the country 
a default value. Call your function for three different cities, at 
least one of which is not in the default country.
"""
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")
# Call the function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("New York", "USA")
describe_city("Tokyo")  # This will use the default country value
"""
The describe_city function is defined with two parameters:

city: Represents the name of the city.
country (with a default value of "Unknown"): Represents the name of the country in which the city is located. If the country is not provided when calling the function, it defaults to "Unknown."
Inside the function, it prints a message that includes the city and the associated country using an f-string.

The code then calls the describe_city function three times with different arguments:

a. In the first call, it describes Reykjavik as being in Iceland.
b. In the second call, it describes New York as being in the USA.
c. In the third call for Tokyo, it uses the default country value "Unknown" because no country is provided.
"""