# number_list = [2, 4, 6, 8, 10, 0, 1, 3, 5]
# new_number_list = []
# sum=0
# for num in number_list:
#     if num == 0:
#         break
#     new_number_list.append(num)
#     sum+=float(num)
# # print(new_number_list)
# print("sum of numbers=",sum,"avg of numbers=",sum/len(new_number_list))

# numbers=(input("enter numbers, separated by space:"))
# number_list=numbers.split()
# new_number_list = []
# sum=0
# for num in number_list:
#     if float(num) == 0:
#         break
#     new_number_list.append(num)
#     sum+=float(num)
# print(new_number_list)
# print("Average and Sum of the above numbers are:",sum/len(new_number_list),sum)

# year=int(input())
# day=int(input())
# next_day=0
# month=int(input())
# if day==day:
#     next_day=day+1
# print("[yyyy-mm-dd]",year,'-',month,'-',next_day)

numbers=[3,7,10,20,5,8,13,18,21]
new_number_list=[]
i=0
while i < len(numbers):
    if numbers[i]%2==0:
    #    print(i)
       new_number_list.append(numbers[i])
    i+=1   
print(max(new_number_list))



