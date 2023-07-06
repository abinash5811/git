# arr=[2,4,3]
# subarrays=[]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         subarray=arr[i:j+1]
#         subarrays.append(subarray)
# print(subarrays)
        
class Solution(object):
    def numOfSubarrays(self, arr):
        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                subarray = arr[i:j]
                if len(subarray) > 1:
                    sub_sum = sum(subarray)
                    if sub_sum % 2 != 0:
                        count += 1
        return count

solution = Solution()
arr = [1,3,5]
result = solution.numOfSubarrays(arr)
print(result)





