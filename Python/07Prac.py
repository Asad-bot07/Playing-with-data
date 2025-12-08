vowels = "aeiouAEIOU"
word = input("Enter a word : ")
count = 0
for char in word:
    if char in vowels:
        count += 1

print("Number of vowels:", count)