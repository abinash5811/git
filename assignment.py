# import numpy as np 
# import dask.array as da
# import pandas as pd 
# arr=np.array([2,4,6,8,10])
# arr1=np.square(arr)
# print(arr1)
# def pay_calc(hourly_wage,work_hour):
#     pay=[]
#     total_payout=hourly_wage*work_hour
#     return total_payout
# hourly_wage=da.array([20,30,40,50,60,70])   
# work_hour=da.array([5,6,7,8,9,10])
# result=pay_calc(hourly_wage, work_hour)
# result=result.compute()
# print(result)

# import dask.bag as db
# def calc_payout(monthly_wage,work_hour):
#     bag= db.from_sequence(zip(monthly_wage,work_hour))
#     total_pay=bag.map(lambda x: x[0]*x[1])
#     results=total_pay.compute()
#     return results
# monthly_wage=[20,30,40,50,60,70]  
# work_hour=[5,6,7,8,9,10]
# pay_results= calc_payout(monthly_wage,work_hour)  
# print(pay_results)


# from joblib import Memory

# # create a Memory object to cache function calls
# mem = Memory(location='cache')

# # define a function to calculate the mean of a list of numbers
# @mem.cache
# def calc_mean(numbers):
#     print("Calculating mean...")
#     total = sum(numbers)
#     return total / len(numbers)

# # define a list of numbers to use for testing
# my_list = [1, 2, 3, 4, 5]

# # call the function the first time, which will calculate the mean and cache the result
# result1 = calc_mean(my_list)

# # call the function again with the same argument, which will retrieve the cached result instead of recalculating it
# result2 = calc_mean([1, 2, 3, 4, 5, 6])

# # print the results
# print(result1)  # should be 3.0
# print(result2)    
import re  # Import the re library

# Define the input text string and the search pattern
text = "My SSN is 123-45-6789"
pattern = "(\d{3})-(\d{2})-(\d{4})"

# Use the findall() method of the re library to find all occurrences of the pattern in the text
# match = re.search(pattern, text)
matches = re.findall(pattern, text)
# print(len(matches)) #start and stop of all the "the"
print(matches)

# re.findall(r'(\d{3})-(\d{2})-(\d{4})', 'My SSN is 123-45-6789')