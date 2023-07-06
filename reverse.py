# str1="ABINASH"
# print(str1[-1::-1])

# nested_list=[[1,2],[3,4]]
# for outer_element in nested_list:
#     for element in outer_element:
#         print(element)
#         if element %2 == 0: 
#             print("it is an even number")
#         else:
#             print("it is an odd number")    

str1="manisha timpa"
reverse_str1=" "
i=len(str1)-1
while i>=0:
    reverse_str1+=str1[i]
    i-=1
print(reverse_str1)


