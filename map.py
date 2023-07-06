

# numbers = list(range(1, 11))
# result=list(filter(lambda x:x%2!=0,numbers))
# print(result)
# square_of_odd= list(map(lambda a:a**2,result))
# print(square_of_odd)
# print(sum(square_of_odd))

pizza_toppings = ['mushroom', 'olive', 'tomato', 'pepperoni', 'onion', 'garlic']
burger_toppings = ['lettuce', 'cheese', 'mayonnaise', 'baco', 'pickle', 'avocado']
new_toppings=[]

for i in pizza_toppings:
    if len(i)>5:
        new_toppings.append(i)
for j in burger_toppings:
    if len(j)>5:
        new_toppings.append(j)
                
print(new_toppings)       



