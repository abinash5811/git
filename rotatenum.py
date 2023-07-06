# Given an array nums, write a python program to return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
# def check_rotation(nums):
#     n = len(nums)
#     is_sorted = False

#     # Find the index of the smallest element in the array
#     min_index = nums.index(min(nums))

#     # Check if the array is sorted in non-decreasing order
#     if nums == sorted(nums):
#         is_sorted = True

#     # Check if the array was rotated
#     if is_sorted:
#         return True
#     else:
#         # Rotate the array back to its original order
#         rotated_nums = nums[min_index:] + nums[:min_index]
#         if rotated_nums == sorted(nums):
#             return True
#         else:
#             return False


# # Example usage:
# nums = [4, 5, 6, 7, 0, 1, 2]
# result = check_rotation(nums)
# print(result)

# nums=[4,5,6,7,0,1,2]
# min_index=nums.index(min(nums))
# print(min_index)
# first_half=nums[min_index:]
# second_half=nums[:min_index]
# add=first_half+second_half
# print(first_half)
# print(second_half)
# print(add)
# print("sorted num is:",sorted(nums))

def check_rotation(nums):
    is_sorted=false

    # to find smallest element in the array
    min_index=nums.index(min(nums))

    if nums==sorted(nums):
        is_sorted =True

    if is_sorted:
        return True

    else:
        rotated_nums=nums[min_index:]+nums[:min_index]  
        if rotated_nums==sorted(nums):
            return True
        else:
            False
nums=[4,5,6,7,0,1,2,3]               
result=check_rotation(nums)
print(result)
