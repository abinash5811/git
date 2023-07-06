# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# nums = [2,7,11,15]
# target=9
# result=[]
# for i in range(0,len(nums)):
#     # print(i[0])
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             result.append([i,j])
# print(result)            
        
nums=[2,7,11,15]   
T=9
my_dict={}
for index, value in enumerate(nums):
    tar=T-value
    if tar in my_dict:
      print(my_dict[tar],index) 
      break
    my_dict[value]=index 
   
      


         
                


     

