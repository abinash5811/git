# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):

# groceries= [('Eggs', 2.5), ('Milk', 3.0), ('Bread', 1.5), ('Apples', 0.75), ('Cheese', 5.0)]
# def sort_groc(groceries):
#     n=len(groceries)
#     for i in range (n):
#         swapped=False
#         for j in range (0,n-i-1):
#             if groceries[j][1]>groceries[j+1][1]:
#                 groceries[j],groceries[j+1]=groceries[j+1],groceries[j]
#                 swapped=True
#         if not swapped:
#             break        
#     return groceries
# # Sort the item by price
# sorted_groceries = sort_groc(groceries)

# # Print the sorted list
# for item, price in sorted_groceries:
#     print(f'{item}: {price} pounds')  

# import random

# def guess_number_game():
#     # Generate a random number between 1 and 100
#     target_number = random.randint(1, 100)
#     attempts = 0

#     while attempts < 7:
#         # Get user's guess
#         guess = int(input("Guess a number between 1 and 100: "))
        
#         # Increment the number of attempts
#         attempts += 1

#         if guess == target_number:
#             print("Congratulations! You guessed the number correctly.")
#             return
#         elif guess < target_number:
#             print("The number is lower than your guess.")
#         else:
#             print("The number is higher than your guess.")

#     print("Game over! You have used all your attempts.")
#     print(f"The target number was {target_number}.")

# # Start the game
# guess_number_game()

# print("Thank you for playing the number guessing game!")

# def bubble_sort(arr):
#     swaps = 0
#     comparisons = 0
#     n = len(arr)

#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             comparisons += 1
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swaps += 1

#     print("Sorted array is:", arr)
#     print("Number of swaps:", swaps)
#     print("Number of comparisons:", comparisons)


# # Example usage
# arr = [5, 3, 4, 2, 1, 6]
# bubble_sort(arr)

# l=[]
# def convert(b):
#     if(b==0):
#         return l
#     dig=b%2
#     l.append(dig)
#     convert(b//2)
# convert(6)
# l.reverse()
# for i in l:
#     print(i,end="")     
# s=input()
# def isValid(s):
#       for i in range(len(s)-1):
#         if s[i]=='(' and s[i+1]==')':
#             return True
#         elif s[i]=='[' and s[i+1]==']': 
#             return True
#         elif s[i]=='{' and s[i+1]=='}':
#             return True
#         else:
#             return False
#       return "paranthesis not matching"
 
# output=isValid(s)  
# print(output) 

strs = ["flower","flow","flight"]
shortest_str = strs[0]
for word in strs:ffffffffffff
#     print(len(word))
# print(strs[0])  
    if len(word)<len(shortest_str):
        shortest_str=word
        print(shortest_str)
   
   


