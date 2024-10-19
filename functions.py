
docstring = """Name: Hannah Busto
Course/Section: BSIT-S-3A
Docstring, Lambda, and Map Function Seatwork"""

numbers = [1, 2, 3, 4]

squared_numbers = list(map(lambda a: a ** 2, numbers))
multiplied_by_three = list(map(lambda a: a * 3, numbers))

print(docstring)
print(f"Numbers: {numbers}")
print(f"Sqared: {squared_numbers}")
print(f"Multiplied by 3: {multiplied_by_three}")