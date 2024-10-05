name = input("Enter your name: ")
company = input("Enter your company: ")
dept = input("Enter your department: ")
pos = input("Enter your position: ")
sss = 200
pagibig = 100
hrs = int(input("Enter hours worked: "))
match pos:
    case "M":
        position = "Messenger"
        taxRate = 0.05
        baSal = 6500
    case "E":
        position = "Encoder"
        taxRate = 0.06
        baSal = 7500
    case "T":
        position = "Technician"
        taxRate = 0.07
        baSal =8500
    case "P":
        position = "Programmer"
        taxRate = 0.08
        baSal = 10500
    case "S":
        position = "Software Engineer"
        taxRate = 0.09
        baSal = 13500
    case _:
        print(f"Invalid position")
    
if hrs < 160:
    ot = 0
    deduction = float((sss + pagibig) + (baSal / 160) * 1.5)
elif hrs > 160:
    ot = float((hrs - 160) * (baSal / 160) * 1.5)
    deduction = sss + pagibig
else:
    print(f"Invalid")

gross = baSal + ot
netPay = gross - deduction

print(f'\nName: {name}')
print(f'Company: {company}')
print(f'Department: {dept}')
print(f'Position: {position}')
print(f'Gross Pay: P{gross: .2f}')
print(f'Net Pay: P{netPay: .2f}')