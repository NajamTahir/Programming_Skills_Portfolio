"""
Chapter 5 Ex 2
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between

each word-meaning pair in your output.
"""
# Create a glossary with programming terms and their meanings
programming_glossary = {
    'variable': 'A container for storing data in a program.',
    'function': 'A reusable block of code that performs a specific task.',
    'loop': 'A control structure that repeats a block of code until a condition is met.',
    'algorithm': 'A step-by-step procedure or set of instructions for solving a specific problem.',
    'conditional': 'A control structure that allows you to execute code selectively based on a condition.'
}
# Print each word and its meaning with a blank line in between
for word, meaning in programming_glossary.items():
    print(word + ':')
    print(meaning + '\n')
"""
The program defines a dictionary called programming_glossary. In this dictionary, each key represents a programming term, and each value is the definition or meaning of that term.

Several programming terms and their meanings are provided as key-value pairs in the dictionary.

The program uses a for loop to iterate through the items (key-value pairs) in the programming_glossary dictionary.

Inside the loop, it prints the term (the key) followed by a colon and then the meaning (the value) on a new line.

After printing the meaning, it adds a blank line to separate each term and its definition.
"""