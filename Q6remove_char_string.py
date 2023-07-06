# str=input()
# chr=input()
# rep_str=""

# for i in range(0,len(str)):
#     if str[i]==chr:
#         rep_str=rep_str+""
#     else:
#         rep_str=rep_str+str[i] 
# print(rep_str)  

str = input()
chr = input()
rep_str=""
for i in range(0,len(str)):
    if str[i]==chr:
        rep_str=rep_str+""
    else:
        rep_str=rep_str+str[i]
print(rep_str)

