import re 
text = "My age is 22 and my brother's age is 24"
result = re.findall(r"\d+", text)
print(result)