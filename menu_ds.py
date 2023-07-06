# Sample nested list of menu items
menu = [
    ["Burger", 10.99, "Entree"],
    ["Salad", 7.99, "Appetizer"],
    ["Pizza", 14.99, "Entree"],
    ["Fries", 3.99, "Side"],
    ["Ice Cream", 4.99, "Dessert"],
]
for item in menu:
    print(item[0])
search_item=input("enter a item that you are searching for:")  
found=False 
for item in menu: 
    if item[0]==search_item:
       print("item is found",item)
       found=True
       break
if not found:
    print('item is not found in the menu')