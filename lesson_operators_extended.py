# Arithmetic precedence with mixed operators
number = 1 + 2 * 3 / 4.0
print(number)  # Output: 2.5

# Modulo (remainder)
remainder = 11 % 3
print(remainder)  # Output: 2

# Exponentiation
squared = 7 ** 2
cubed = 2 ** 3
print(squared)  # Output: 49
print(cubed)    # Output: 8

# String concatenation
hello_world = "hello" + " " + "world"
print(hello_world)  # Output: "hello world"

# String repetition
lots_of_hellos = "hello" * 10
print(lots_of_hellos)  # Output: "hellohellohellohellohellohellohellohellohellohello"

# List concatenation
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)  # Output: [1, 3, 5, 7, 2, 4, 6, 8]

# List repetition
print([1, 2, 3] * 3)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Exercise: Repeated object references in lists
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# Testing output
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")