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

import re

# Match a specific sequence '123'
s = 'foo123bar'
x = re.search('123', s)
print(x)  # Output: <re.Match object; span=(3, 6), match='123'>

# Conditional match check
if re.search('123', s):
    print('Found a match.')
else:
    print('No match.')

# Match three consecutive digits
print(re.search('[0-9][0-9][0-9]', 'foo123bar'))  # Output: <re.Match object; span=(3, 6), match='123'>
print(re.search('[0-9][0-9][0-9]', 'foo456bar'))  # Output: <re.Match object; span=(3, 6), match='456'>
print(re.search('[0-9][0-9][0-9]', '234baz'))     # Output: <re.Match object; span=(0, 3), match='234'>
print(re.search('[0-9][0-9][0-9]', 'qux678'))     # Output: <re.Match object; span=(3, 6), match='678'>
print(re.search('[0-9][0-9][0-9]', '12foo34'))    # Output: None

# Match '1' followed by any character, then '3'
s = 'foo123bar'
print(re.search('1.3', s))  # Output: <re.Match object; span=(3, 6), match='123'>

s = 'foo13bar'
print(re.search('1.3', s))  # Output: None

# Reconfirm exact match '123'
s = 'foo123bar'
print(re.search('123', s))  # Output: <re.Match object; span=(3, 6), match='123'>
