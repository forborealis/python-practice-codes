total = 0
number = int(input("Enter a number: "))

while number != 0:
    total += number
    number = int(input("Enter a number: "))

print(f"You entered 0.")
print(f"The total sum is: {total}")