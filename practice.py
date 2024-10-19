'''sum = 0
numbers = int(input("Enter a number: "))

while numbers % 2 != 1:
    sum += numbers
    numbers = int(input("Enter a number: "))

print(f'Odd number entered, stopping the loop')
print(f'Sum of all even numbers: {sum}')'''
'''
numbers = list(range (1, 11))
even_numbers = list(range(2, 11, 2))

min_value = min(numbers)
max_value = max(numbers)
sum_value = sum(numbers)

print(f'Numbers: {numbers}')
print(f'Minimum Value: {min_value}')
print(f'Maximum Value: {max_value}')
print(f'Sum Value: {sum_value}')
print(f'Even Numbers: {even_numbers}')
'''

numbers = []

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

third_num = numbers[2]
square = third_num ** 2

print(f'The third number is: {third_num}')
print(f'The square of the third number is: {square}')