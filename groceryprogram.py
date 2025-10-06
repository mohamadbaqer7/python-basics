groceries = {
    "apple": 4,
    "banana": 7,
    "milk": 5,
    "bread": 2
}
cart = {}
while True:
    product = input("what do you want to buy?")
    if product == "done":
        break
    if product not in groceries:
        print("Sorry, not availble.")
        continue

    quantity = int(input("How many do you want?"))
    if product in cart:
        cart[product] = cart[product] + quantity
    else:
        cart[product] = quantity

print("You bought:")
for name in cart:
    print(name, ":", cart[name])

print("Final list of product:")
total = 0
for name in cart:
    qty = cart[name]
    price = groceries[name] * qty
    if name == "milk" and qty >= 2:
        price = price - 2
    print(name, ":", qty, "x $", groceries[name], "=", "$" + str(price))
    total = total + price

print("Total cost: $" + str(total))

if total > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")
