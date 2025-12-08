lst = list(input("Enter elements in a single line : ").split())
c = 0
print(lst)
search_element = int(input("Enter the search element : "))
for items in lst : 
    print(items)
    if search_element == int(items):
        print("Element found in the list")
        c+=1
        break

if(c == 0):
    print("Element not found")