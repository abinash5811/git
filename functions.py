# def sum(num1=10,num2=20):
#     result=num1+num2
#     return result
# print(sum())

# def count_char(word):
#     char_count={}
#     for char in word:
#         if char in char_count:
#             char_count[char]+=1
#         else:
#             char_count[char]=1
#     return char_count
    
# word = "AbinAsh"
# count_char(word)
# print(count_char(word))      

def reverse_str(word):
    reverse_word=""
    for i in word[-1::-1]:
        reverse_word+=i
    return reverse_word
word="manisha"    
reverse_str(word)
print(reverse_str(word))




        
        


