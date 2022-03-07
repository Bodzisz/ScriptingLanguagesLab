def print_prodcut(name, amount, vat, price):
    if len(name) > 20:
        name = name[0:20] + "..."
    text = "{name:23s} {amount:>6d} {vat:7d} {price:> 12.2f}"
    print(text.format(name=name, amount=amount, vat=vat, price=price))


banner_text = "%s %22s %7s %12s"
print(banner_text % ("Product", "Amount", "Vat", "Price"))
print_prodcut("Bread", 2, 23, 3.00)
print_prodcut("Beer", 20, 0, 199.99)
print_prodcut("Pancakes", 1, 23, 3.81)
print_prodcut("Apple", 4, 23, 2.20)
print_prodcut("T-shirt", 1, 23, 10.99)
print_prodcut("Super Extra Fine Chewing Gum", 1, 23, 1.99)
