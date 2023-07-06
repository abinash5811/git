def count_odd(low,high):
    count=0
    for i in range(low,high+1):
        if i%2!=0:
            count=count+1
    return count
result=count_odd(low=2, high=10)        
print(result)
# class Solution(object):
#     def countOdds(self, low, high):
#         """
#         Count the number of odd integers within the range [low, high].
        
#         :param low: int, the lower bound of the range
#         :param high: int, the upper bound of the range
#         :return: int, the count of odd numbers within the range
#         """
#         count = 0
#         for i in range(low, high + 1):
#             if i % 2 != 0:
#                 count += 1
#         return count

# solution = Solution()
# result = solution.countOdds(low=800445804, high=979430543)
# print(result)




