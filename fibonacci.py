num= int(input("enter a integer number:"))
def fib(n):
  a=0
  b=1
  print(a)
  print(b)
  for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)
fib(6)

def fibonacci(n):
    if n<=0:
        print("enter an integer number")
    if n==[1] :
        return[1]
    if n==[2] :
        return[1,1]
    sequence=[1,1]    
    for i in range (2,n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)
    return sequence

n = 10
result = fibonacci(n)
print("The first {} numbers in the Fibonacci sequence are: {}".format(n, result))








# Q-count a particular from a given range

# start_num=int(input("enter a starting number:"))
# end_num=   int(input("enter the ending number:"))
# digit=int(input("enter the digit you want to count:"))
# count=0
# for i in range (start_num, end_num + 1): 
#     current_num=i
#     while current_num>0:
#         if current_num%10==digit:
#             count+=1
#         current_num//=10
# print(f"The digit {digit} appears {count} time between {start_num} to {end_num}.")




