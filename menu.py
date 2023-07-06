menu = {
    "Samosa": 20,
    "Kachori": 15,
    "Jalebi": 10,
    "Dhokla": 15,
    "Paani Puri": 30
}
order={}
print("welcome to our resturant, here is our menu")
item=""
total_price=0
while item!='done':
    item=input('enter the dish you want to order:')
    for dish,price in menu.items():
        if item==dish:
            qty = int(input('Enter the quantity you want to order: '))
            order[item]=qty
            total_price=int(total_price)+int(price)*int(qty)
print("Here is your oder summury")
print(order)
print("The total bill is:",str(total_price))            