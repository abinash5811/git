
# result=[]
# for i in range (1,6):
#     if i%2==0:
#        for j in range(1,6):
#             if j%2!=0:
#                 r=(i,j)
#                 result.append(r)
# print(result)                
             
def get_result():
    result=[]
    for i in range(1,6):
        if i%2==0:
            for j in range(1,6):
                if j%2!=0:
                    r=(i,j)
                    result.append(r)
    return result
print(get_result())    

          
                 

