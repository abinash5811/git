# cels = float(input("Enter a value that represents temperature in Celsius: "))

# # Check if the input is valid
# if cels == 0:
#     print("Enter a valid input")
#     # cels = float(input("Enter a value that represents temperature in Celsius: "))
# else:
# # Convert Celsius to Fahrenheit
#  farenheit = (cels * 9/5) + 32
#  print(farenheit)


# numbers=[1,4,5,7,8,9,10,11,12,13,14,15,16]
# odd_num_list=[]
# sum_of_odd=0
# for num in numbers:
#     if num%2!=0:
#         odd_num_list.append(num)
#         sum_of_odd+=num
# print(odd_num_list)        
# print(sum_of_odd)        

def sum_of_odd_numbers(numbers):
    sum=0
    for num in numbers:
        if num%2!=0:
           sum+=num
    return sum
numbers=[1,4,5,7,8,9,10,11,12,13,14,15,16]
sum_of_odds=sum_of_odd_numbers(numbers) 
print(sum_of_odds)
  

