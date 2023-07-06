# number1=[1,2,3,4,5,6]
# for i in number1:
#     if i%2==0:
#         print(i,"is even & square is :",i**2)
#         print(type(i))
#     else:
#         print(i,"is odd & cube is :",i**3)        

number1=[2,3,4,5,6]
for i in number1:
    if i==4:
        continue
    elif i%2!=0:
        break
    else:
        print("number is even and the sqaure is:", i**2)
        



