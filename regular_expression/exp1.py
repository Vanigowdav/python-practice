import re

text = "I am learning Python"
result = re.search("Python", text)
print(result)   #span (14, 20) means the match starts at index 15 and ends before index 21
print(result.group())