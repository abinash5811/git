# nums=[4, 3, 6, 8, 2, 9, 1, 7]
# Target=10
# found=False
# for i in range (len(nums)):
#     for j in range (len(nums)):
#        if Target==(nums[i]+nums[j]):
#          print((i,j))
#          found=True
#          break
#     if found:
#         break  
  

import numpy as np
def second_highest_num(list):

    up_list=np.sort(list)
    sec_hi_num=up_list[-2]
    
    return sec_hi_num

list=[12, 3, 1, 2, -6, 5, -8, 6]
result=second_highest_num(list)
print(result)

# import numpy as np

# def min_max_pair(my_list):
#     up_list = np.sort(my_list)
#     min_num = up_list[0]
#     max_num = up_list[-1]
#     min_max = (min_num, max_num)
#     return min_max

# my_list = [12, 5, 4, 6, 47, 3, 1]
# result = min_max_pair(my_list)

# print(result)





