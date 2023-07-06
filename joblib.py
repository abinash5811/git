from joblib import Memory

# create a Memory object to cache function calls
mem = Memory(location='cache')

# define a function to calculate the mean of a list of numbers
@mem.cache
def calc_mean(numbers):
    print("Calculating mean...")
    total = sum(numbers)
    return total / len(numbers)

# define a list of numbers to use for testing
my_list = [1, 2, 3, 4, 5]

# call the function the first time, which will calculate the mean and cache the result
result1 = calc_mean(my_list)

# call the function again with the same argument, which will retrieve the cached result instead of recalculating it
result2 = calc_mean([1, 2, 3, 4, 5, 6])

# print the results
print(result1)  # should be 3.0
print(result2)  # should also be 3.0, and the "Calculating mean..." message should not be printed