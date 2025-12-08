import re
words = '''
Hello!!! My name is Asad   Hussain, and I live in Kolkata...  
I   bought 5 items yesterday: milk, bread, chips, cola, and apples!!!  
The total cost was   ₹  435.50.  
Email me at: asad_hussain@@gmail..com or contact at +91-12345-67890??  
BTW, I loooove   programming!!!!!  
    This    sentence   has    extra    spaces.
Here's a mix Of CASES, numbers123, and   weird---characters###.
'''
final = re.findall(r'\w+', words)
print(final)