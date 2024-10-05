grade1 = float(input("Enter your first grade:"))
grade2 = float(input("Enter your second grade:"))
total = float((grade1 + grade2) / 2)

print(f"Your grade for this subject is {total}")
if total < 75:
    print("You failed.")
else:
    print("You passed.")