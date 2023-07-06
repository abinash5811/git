m=int(input())
n=int(input())
all_even=[]
for i in range(m,n+1):
    if i%2==0:
     all_even.append(i)
print("Biggest even number between m to n is:",max(all_even))