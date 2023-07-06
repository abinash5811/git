import re

# txt = "The rain in Spain"
x = re.sub(r'(\d)\1', r'\1', '11223344556677889900')
print(x)