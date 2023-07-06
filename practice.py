# arr1=[1,2,3,4,5,6,7,8,9,10,11,12]
# new_arr=arr1[1:3]
# new_arr1=arr1[5:7]
# new_arr2=arr1[9:11]
# arr=new_arr + new_arr1 + new_arr2
# print(arr)

# str=input("enter a string:")
# count=0
# for char in str:
#     if char in "aeiouAEIOU":
#         count+=1
# print ("the number of vowels in a string:",count)


# arr=[[1,2,3,4],
#      [5,6,7,8,9]]
# for i in range (len(arr)):
#     print("outer loop and the value of i is =", i)
#     for j in range (len(arr[i])):
#         print(" Inner for loop value of i is =", i, " value of j is = ", j)
#         print([j])


# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#    if number == 3:
#        continue
#    print(number)


# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")    
#     print()
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# try:
#   result = num1 / num2
# except ZeroDivisionError:
#   print("can't divided by zero")
# except ValueError:
#   print('enter a integer number')  

# print("The result is: ", result)try:
words = ['apple', 'banana', 'cherry']
first_letters = [word[0] for word in words]
print(first_letters)