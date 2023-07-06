# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
# num = int(input("Enter a number: "))
# sum = 0
# order = len(str(num))
# temp=5
# digit = 10 / 2
# # print(digit)  
# # digit //= 10
# print(digit)




# arr=[1,2,3,4]
# for i in range(len(arr)):
#      arr[i] *= 2
# print(arr)    

# armstrong number

# number=int(input("enter a number"))
# temp=number
# sum=0
# order= len(str(number))
# while temp>0:
#     digit=temp%10
#     sum+=digit**order
#     temp=temp//10
# if sum==number: 
#     print("it is an arnstrong number") 
# else:
#     print("it is not an armstrong number")    

number = int(input("Enter a number: "))
temp = number
order = len(str(number))
sum = 0

while temp > 0:
   digit = temp % 10
   sum=sum+(digit ** order)
   temp //= 10

if number == sum:
   print(number, "is an Armstrong number")
else:
   print(number, "is not an Armstrong number")




    
 