
def isPalin(word):
    if word == word[::-1]:
        return True
    return False


word = str(input("Enter a word"))
if(isPalin(word)):
    print("It is palindrome")
else:
    print("It is not palaindrome")