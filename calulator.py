# num1=int(input("enter first number="))
# num2=int(input("enter second number="))
# add=(num1+num2)
# sub=(num1-num2)
# mult=(num1*num2)
# div=(num1/num2)
# # options=['add','sub','mult','div']
# # for chose in options:
# while True:
#     chose = input("select a option from add / sub/ mult / div:")
#     if chose=='add':
#         print("sum of two numbers=",(add))
#         break
#     elif chose=='sub':
#         print("sub of two numbers=",(sub))
#         break
#     elif chose=='mult':
#         print("mult of two numbers=",(mult))  
#         break  
#     elif chose=='div':
#         print("div of two numbers=",(div))  
#         break  
#     else:
#         print("chose the write option")
#         continue   
# import random
# secret_number=random.randint(1,100)
# num_tries=3
# while num_tries>0:
#     guess=int(input("guess the secret number(between 1 to 100):"))
#     if guess==secret_number:
#         print("congratulations, you have guessed the right number")
#         break
#     if guess<secret_number:
#         print("your guess is too low")  
#     else:
#         print("your guess is too high")
#     num_tries-=1      
# if num_tries==0:
#     print("sorry,you have ran out of tries.The secret number is:",secret_number)         

def calculator(num1,num2,operation):
    if operation=="+":
      return num1+num2
    if operation=="-":
      return num1-num2
    if operation=="*": 
       return num1*num2
    if operation=="/" :
      return num1/num2
    else:
      return "Invalid operation"  
result=calculator(15,10,"+")     
print(result) 


