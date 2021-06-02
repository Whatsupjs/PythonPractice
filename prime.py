#Ask the user for a number and determine whether the number is prime or not. 
def prime(num):
    
    if num <= 1:
        return False

    for x in range(2,num):
        if num % x == 0: 
            return False
    
    return True

num = input("Enter a number to see if it is a prime number: ")
print(prime(int(num)))