# #factorial of (n)
# def rec(n):
#     if n==0:
#         return 1
#     else:
#         return n*rec(n-1) 
# print(rec(3))           

#fibonnaci series

# def rec_fib(n):
#     if n<=1:
#         return n
#     else:
#         return rec_fib(n-1)+rec_fib(n-2)  
# print(rec_fib(7))          


# def fun(n):
#     if (n > 100):
#         return n - 5
#     return fun(fun(n+11));
 
# print(fun(45))

# def num(n):
#     if n <= 0:
#         return ["Zero!"]
#     else:
#         result = [str(n) + "*" * n]
#         return result + num(n - 2)
# print(num(10))        
    
# def print_numbers_reverse(num):
#     if num <= 0:
#         print("Zero!")
#     else:
#         print(num, end="")
#         print("*" * num)
#         print_numbers_reverse(num - 2) 
# print(print_numbers_reverse(10))  

# def print_numbers(n):
#     if n == 0:
#         return
#     else:
#         print_numbers(n-1)
#         print(n)

# print_numbers(3)        
# def a(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return a(n-1)+a(n-2)
# for i in range(0,4):
#     print(a(i),end=" ")
# lst = [1, 5, 6, 10, 2, 4]
# maximum = float('-inf')  # Initialize maximum with a very small value

# for num in lst:
#     if num > maximum:
#         maximum = num

# print(maximum)   

    


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Determine the midpoint
# mid = len(my_list) // 2

# # Print the first part
# print("First part:")
# for i in range(mid):
#     print(my_list[i])

# # Print the second part
# print("Second part:")
# for i in range(mid, len(my_list)):
#     print(my_list[i])
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))
def rec_str(word):
    if len(word)==1:
        return word
    else:
        return word[-1]+rec_str(word[0:len(word)-1])
print(rec_str("abinash")) 







 
  




