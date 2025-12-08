import re
input = "Age 20, Room 501, level 3"

ans = re.findall(r'\d+', input)

print(ans)