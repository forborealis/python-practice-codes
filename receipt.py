item1 = "Laptop"
price1 = 15999.55
qty= 2
item2 = "RGB Keyboard"
price2 = 1599.69
sum1 = float(price1) * qty
sum2 = float(price2) * qty

print(f"{item1}: {qty} x P{price1: .2f} = P{sum1: .2f} ")
print(f"{item2}: {qty} x P{price2: .2f} = P{sum2: .2f} ")
print(f"\n----Total: P{sum1 + sum2: .2f}----")