# countries = ["USA", "Canada", "Mexico", "Brazil", "UK", "France", "Germany", "China", "India"]
# sales = [2500, 300, 1200, 800, 500, 2000, 4000, 1000, 1500]
# # sales1=[]
# # for i in sales:
# #     if i>1000:
# #         sales1.append(i)
# dict1=(list(zip(countries,sales)))
# # print(sales1)        
# # print(dict1)
# sales_data={countries:sales for countries,sales in dict1 if sales>1000}
# print(sales_data)

# stocks = [
#     {'name': 'Apple Inc.', 'ticker': 'AAPL', 'price': 120.0, 'change': 0.05},
#     {'name': 'Microsoft Corporation', 'ticker': 'MSFT', 'price': 95.0, 'change': -0.02},
#     {'name': 'Amazon.com, Inc.', 'ticker': 'AMZN', 'price': 250.0, 'change': 0.1},
#     {'name': 'Alphabet Inc.', 'ticker': 'GOOGL', 'price': 110.0, 'change': 0.02},
#     {'name': 'Facebook, Inc.', 'ticker': 'FB', 'price': 80.0, 'change': 0.03}
# ]

# # filter the stocks where the price is greater than 100 and the percentage change is positive
# filtered_stocks = [stock for stock in stocks if stock['price'] > 100 and stock['change'] > 0]

# # create a new list of dictionaries where each dictionary contains only the name and price of the stock
# new_stocks = [{'name': stock['name'], 'price': stock['price']} for stock in filtered_stocks]

# print(new_stocks)

# songs = ['Bohemian Rhapsody', 'Stairway to Heaven', 'Bohemian Rhapsody', 'Hotel California', 'November Rain', 'Stairway to Heaven', 'Sweet Child O\' Mine']
# song1=[]
# for song in songs:
#     if song not in song1:
#         song1.append(song)
# for usong in song1:        
#     if usong[0]!="S" and usong[-1]!="n":
#          print(usong)        

playlist = ["Wild Thoughts", "All I Do Is Win", "No Brainer", "I'm the One"]
song_request = "All I Do Is Win"
if song_request in playlist:
    print(f'Thanks for requesting "{song_request}". It\'s in my playlist!')
else:
    print("enter one accurate name")    

