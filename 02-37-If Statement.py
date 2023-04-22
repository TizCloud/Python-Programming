# Demo 02-37

myname = input("Enter name :")
price = float(input("Enter price of %s :" %myname))

if price >= 1000:
    temp = price * 0.05
    price = price - temp

vat = price * 0.07
price = price + vat

print("The price of %s (inc VAT 7%%) is %.2f %s" %(myname, price, "Baht."))
