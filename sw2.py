'''sum = 0
number = int(input('Enter a number: '))

while number % 2 != 1:
    sum += number
    number = int(input('Enter a number: '))
print('Odd number entered, stopping the loop.')
print(f'The sum of all even numbers is {sum}.')'''

numbers = list(range(1,11))
even_numbers = list(range(2, 11, 2))

min_value = min(numbers)
max_value = max(numbers)
sum_value = sum(numbers)

print(f"Numbers: {numbers}")
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
print(f"Sum value: {sum_value}")
print(f"Even numbers: {even_numbers}")
