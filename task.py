player_rolls = [
    [3, 5, 6, 2, 1],  # player 1's rolls
    [4, 4, 6, 3, 2],  # player 2's rolls
    [1, 5, 6, 6, 4]   # player 3's rolls
] # list of a list
# max_avg = 0
# max_index = 0
# for i in range(len(player_rolls)):
#     # print(i)
#     sublist=player_rolls[i]
#     # print(sublist)
#     sublist_avg=sum(sublist)/len(sublist)
#     print(sublist_avg)
# #     if sublist_avg > max_avg:
# #         max_avg = sublist_avg
# #         max_index = i

# # print("Max average:", max_avg)
# # print("Max index:", i)

# names = ["Alice", "Bob", "Eve", "Charlie", "Ivy", "David", "Olivia", "Peter"]
# names_vowels=" "
# names_consonants=" "
# for i in names:
#     if i[0]=="A" or [0]=='E' or i[0]=='I' or i[0]=='O' or i[0]=='U':
#         names_vowels.append(i)
#     else:
#         names_consonants.append(i)  
# print(names_vowels)        
# print(names_consonants)

# grades = {'Alice': 85,'Bob': 92,'Charlie': 88,'David': 95,'Emily': 78,'Frank': 91}
# for key,value in grades.items():
#     if value >90:
#        print(f"{key} grade is {value}")


# numbers = [ [2, 5, 11, 20, 8], 
#             [9, 4, 15, 28, 17], 
#             [1, 6, 21, 18, 3], 
#             [10, 13, 25, 33, 30], 
#             [14, 7, 16, 19, 22] ]
# even_count=0
# odd_count=0
# for num1 in numbers:
#     # print(num1)
#     for num2 in num1:
#         # print(num2)
#         if num2%2==0:
#             even_count+=1
#         else:
#             odd_count+=1  
# print("total number of even numbers are=",even_count)  
# print("total number of odd numbers are=",odd_count)            


# players = ['Alice', 'Bob', 'Charlie', 'Diana']
# for player1 in players:
#     # c
#     for player2 in players:
#         # print(player2)  
#         if player1!=player2:
#              print(player1,"vs",player2)

    
# for i in range(3):
#     # print(i)
#     for j in range(2):
#         # print(j)
#        print(i*j)
import numpy as np
my_arr=np.array([10,11,12,16,17,18,19,20,13,14,15,22,30,21,27])
my_arr_sort=np.sort(my_arr)[::-1]
print(my_arr_sort)












