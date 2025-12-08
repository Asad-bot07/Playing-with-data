import re

text = "contact me at asadhussain2408@gmail.com and gayushi32@gmail.com"

ans = re.findall(r'[a-z0-9\@]+gmail.com', text)
print(ans)