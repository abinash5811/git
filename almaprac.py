

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#    print(number)
# for i in range(5):
#    print(i)

# x = -5
# y = 10
# if x > 0:
#   if y > 0:
#     print("x and y are both positive")
#   else:
#     print("x is positive and y is non-positive")
# else:
#   print("x is non-positive")
# words = ["apple", "banana", "cherry", "date", "elderberry"]
# for word in words:
#    if 'b' in word:
#        print(word)

# age=12
# dogs_age=0
# for dog in range(1,13):
#     while dog<3:
#         dogs_age+=10.5
#         break
        
# print(dogs_age)   
           
# human_years = int(input("Enter Murphy's age in human years: "))

# if human_years < 0:
#     print("Invalid input")
# else:
#     if human_years <= 2:
#         dog_years = human_years * 10.5
#     else:
#         dog_years = 21 + (human_years - 2) * 4
#     print("Murphy's age in dog's years is:", dog_years)

human_years = int(input("Enter Murphy's age in human years: "))

# if human_years < 0:
#     print("Invalid input")
# else:
dog_years = 0
i = 1
while i <= human_years:
    if i <= 2:
        dog_years += 10.5
    else:
        dog_years += 4
    i += 1
print("Murphy's age in dog's years is:", round(dog_years))
