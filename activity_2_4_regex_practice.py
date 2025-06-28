import re

# Find all occurrences of "ai" in the string
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)  # Output: ['ai', 'ai']

# Search for a string that doesn't exist
x = re.findall("Portugal", txt)
print(x)  # Output: []

# Search for the first white-space character in the string
x = re.search(r"\s", txt)
print("The first white-space character is located in position:", x.start())

# Make a search that returns no match
x = re.search("Portugal", txt)
print(x)  # Output: None

# Split at each white-space character
x = re.split(r"\s", txt)
print(x)  # Output: ['The', 'rain', 'in', 'Spain']

# Split only at the first white-space
x = re.split(r"\s", txt, maxsplit=1)
print(x)  # Output: ['The', 'rain in Spain']

# Replace every white-space character with the number 9
x = re.sub(r"\s", "9", txt)
print(x)  # Output: 'The9rain9in9Spain'

# Replace the first 2 white-space characters with 9
x = re.sub(r"\s", "9", txt, count=2)
print(x)  # Output: 'The9rain9in Spain'

# Do a search that returns a Match object
x = re.search("ai", txt)
print(x)  # Output: <re.Match object; span=(5, 7), match='ai'>

# Print the start and end position of the first match that starts with "S"
x = re.search(r"\bS\w+", txt)
print(x.span())  # Output: (12, 17)

# Print the string passed into the search function
print(x.string)  # Output: The rain in Spain

# Print the part of the string that matched
print(x.group())  # Output: Spain

