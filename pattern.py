# n=5
# for i in range(n):
#     for j in range (i+1):
#         print("a",end=" ")
#     # for j in range (i,n):
#     #     print(" ",end=" ")
#     print()    

# class person:
#     name= "abinash"
#     occupation="analyst"
#     sal= "50k"
#     age="27"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a = person()  
# # a.name="akash"  
# # a.occupation="bdm"    
# # print(a.name,"is a",a.occupation,"whose sal is",a.sal, "and age is",a.age)
# a.info()    


# toppings=["peprroni","mushrooms","chicken"]
# for i in range (0,len(toppings)):
#     print(i,"th index",toppings[i])


# toppings=["peprroni","mushrooms","chicken"]
# for i in toppings:
#     print(i)



# num=int(input())
# for i in range(num):
#       for j in range(i+1):
#         print("1",end=" ")
#       print()    

# n = int(input())

# for i in range(1, n+1):
#     print(str(i) * i)


numbers=(input("enter numbers, separated by space:"))
number_list=numbers.split()
sum=0
for i in range(0,len(number_list)):
    num=number_list[i]
    if num==0:
     break
    else:
     sum+=float(num)
print("Average and Sum of the above numbers are:",sum/(len(number_list)-1),sum)    

# numbers = input("Enter numbers, separated by spaces and terminated by 0: ")
# num_list = [int(num) for num in numbers.split()]

# # calculate the sum and average
# sum_num = sum(num_list)
# avg_num = sum_num / len(num_list)

# # print the result
# print("Average and Sum of the above numbers are:", avg_num, sum_num)
