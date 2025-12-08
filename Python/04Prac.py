n = int(input("Enter a number"))
b = int(input("Enter a number"))
print("Enter '+' for addition\n Enter '-' for substraction\n Enter '*' for multiplication\n Enter '/' for division ")
operator = input()
if(len(operator) <= 0 or len(operator) > 1):
    print("DUMB ASS SHITTY HEAD")

if(operator == '+'):
    print("Answer : ",n+b)
elif(operator == '-'):
    print("Answer : ",n-b)
elif(operator == '*'):
    print("Answer : ",n*b)
elif(operator == '/'):
    print("Answer : ",n/b)
else:
    print("Error occurred in reading operator")
