numbers = []

for i in range(5):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

third_num = numbers[2]
square = third_num**2
print(f"The third number is: {third_num}")
print(f"The square of the third number is: {square}")