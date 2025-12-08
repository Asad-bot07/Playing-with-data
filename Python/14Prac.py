import re

text = "India is in South Asia, Delhi is the capital"

ans = re.findall(r'[A-Z]\w+', text)

print(ans)