item1 = "Laptop"
price1 = 15999.55
qty= 2
item2 = "RGB Keyboard"
price2 = 1599.69
sum1 = float(price1) * qty
sum2 = float(price2) * qty

print(f"{"Product" :<11} {"Price" :>10} {"Quantity" :>10} {"Total" :>10}")
print(f"{item1 :<11} {price1 :>10.2f} {qty :>7} {sum1 :>14.2f}")
print(f"{item2 :<11} {price2 :>10.2f} {qty :>7} {sum2 :>14.2f}")  