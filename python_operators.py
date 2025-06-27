# Example 1a: Assignment operator with string (=)
greek_island = "Santorini"

# Example 1b: Assignment operator with float and addition (+=)
earth_age_bln = 4.4
universe_age_bln = 14.0
earth_age_bln += 0.1

print(earth_age_bln)  # Output: 4.5

# Example 1c: Assignment operator with list (=)
asia_wishlist = [
    "Bhutan", "Ha Long", "Laos", "Danxia", "Seoul",
    "Khao Sok", "Cebu", "Chiang Mai", "Ho Chi Minh"
]

# Example 2a: Relational (comparison) operator (==)
msg = "life is beautiful"
if msg == "I love you":
    print("propose")
else:
    print("wait xP")

# Output: wait xP

# Example 2b: Relational (comparison) operator (>=)
net_earnings = 10_000_000
if net_earnings >= 100_000_000:
    print("Large Cap")
else:
    print("Small Cap")

# Output: Small Cap

# Example 3a: Membership operator (not in)
activities = ["soccer", "swimming", "running", "skiing"]
if "rock climbing" not in activities:
    print("boo")

# Output: boo

# Example 3b: Membership operator (in)
web_data = ["techresearch and computervision"]
if any("@" in item for item in web_data):
    print("e-mail address")
elif any(char.isdigit() for item in web_data for char in item):
    print("phone number")
else:
    print("not e-mail nor phone number")

# Output: not e-mail nor phone number

# Example 4: Arithmetic operators
a = 10 + 20       # Addition
b = 100 - 1       # Subtraction
c = 50 / 7        # Division
d = 50 // 7       # Floor Division
e = 10 % 8        # Modulus
f = 5 ** 2        # Exponentiation

print(a, b, c, d, e, f, sep="\n")