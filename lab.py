'''name = input("What's your name? ")
age = int(input("How old are you? "))
grade1 = float(input("Enter your first grade: "))
grade2 = float(input("Enter your second grade: "))
grade3 = float(input("Enter your third grade: "))

average = ((grade1 + grade2 + grade3) / 3)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Your average is: {average: .2f}")
if average >= 75:
    print(f"Passed")
else:
    print(f"Failed")'''

name = input("What's your name? ")
age = int(input("How old are you? "))
grade1 = float(input("Enter your first grade: "))
grade2 = float(input("Enter your second grade: "))
grade3 = float(input("Enter your third grade: "))

average = ((grade1 + grade2 + grade3) / 3)

if average >= 75:
    remark = "Passed"
else:
    remark = "Failed"


print(f"{'Name' :<10} {'Age' :>11} {'Average' :>11} {'Remark' :>8}")
print(f"{name :<10} {age :>10} {average :>10.2f} {remark :>10}")