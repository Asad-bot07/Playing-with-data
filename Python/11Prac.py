import re
def isWord(text):
    text = re.findall(r"\w+", text)
    return text

text = "dog cat sun sky car"
print(isWord(text))