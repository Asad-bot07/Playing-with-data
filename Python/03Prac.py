def isPrime(n):
    c = 0
    for i in range(1,int(n/2)):
        if (n % i == 0) :
            c+=1
            break
    if c:
        return False
    else : 
        return True
    
n = int(input("Enter a number : "))
if(isPrime(n)):
    print("It is a prime number")
else:
    print("It is not a prime number")