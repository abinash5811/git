import numpy as np
import pandas as pd
# # arr=[]
# # for i in range (1,101):
# #     arr.append(i)
# # print(arr)
# # print() 
# arr1=np.arange(1,101)  
# print(arr1)
# print()
# x=arr1.reshape(10,10)
# # x1=arr1.reshape(1,10,10)
# print("x is :",x)
# print()
# # print("x1 is:",x1)
# final_output=np.square(x)
# print(final_output)
# urls = [
#     "https://www.example.com/market.php",
#     "https://www.google.com/search",
#     "https://www.python.org/doc",
#     "https://www.github.com/openai",
# ]
# # ending_strings = [url.split(".")[-1] for url in urls]
# ending_strings = [url.split(".") for url in urls]
# print(ending_strings)
import pandas as pd

# List of URLs
urls = [
    "https://www.example.com/market.php",
    "https://www.google.com/search",
    "https://www.python.org/doc",
    "https://www.github.com/openai",
]

# Extract domain names from URLs
domain_names = [url.split("//")[1].split("/")[0] for url in urls]

# Extract ending strings from URLs
ending_strings = [url.split(".")[-1] for url in urls]

# Create DataFrame using zip
data = list(zip(urls, domain_names, ending_strings))
df = pd.DataFrame(data, columns=["URLs", "Domain Name", "Ending String"])

print(df)
