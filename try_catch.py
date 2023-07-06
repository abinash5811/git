prices = {
    'chicken': 3.50,
    'vegetable': 3.00,
    'chips': 1.50,
    'salsa': 1.00,
    'guacamole': 2.00,
    'coke': 1.00,
    'pepsi': 1.00,
    'sprite': 1.00,
    'small': 0.00,
    'medium': 1.00,
    'large': 2.00
}

# Ask the user for their order
print('Welcome to the Mexican Restaurant!')
print('Please enter your order.')

while True:
    try:
        taco=input("taco(chicken or vegetable)?")
        if taco.lower()  not in ["chicken","vegetable"]:
            raise ValueError('invalid taco option,please choose the write one')

        # sides=input("sides(chips,salsa, or guacamole)") 
        # if set(sides.lower().split(', '))- {'chips','salsa','guacamole'}:
        #     raise ValueError('invalid sides option')
        sides=input("sides(chips,salsa, or guacamole)")  
        if sides.lower() not in ["chips","salsa","guacamole"]:
            raise ValueError('invalid option')  

        drinks=input("drinks(coke,pepsi, or sprite)")   
        if drinks.lower() not in ['coke','pepsi','sprite']:
            raise ValueError('invalid coke option')

        size=input("size(small,medium, or large)")    
        if size.lower() not in ['small','medium','large']:
            raise ValueError('invalid option')
        break
    except Exception as e:
        print('Invalid input. ' + str(e))

# Calculate the total cost
total_cost = prices[taco.lower()] + sum(prices[s.lower()] for s in sides.lower().split(', ')) + prices[drinks.lower()] + prices[size.lower()]
# experiment
total_cost = prices[taco.lower()] + prices[sides.lower()] + prices[drinks.lower()] + prices[size.lower()]
# Print the order and total cost
print('\nYour order:')
print('- Taco:', taco)
print('- Sides:', sides)
print('- Drinks:', drinks)
print('- Size:', size)
print('\nTotal cost: ${:.2f}'.format(total_cost))

