#Ask the user for a string and print out whether this string is a palindrome or not. 
def palindrome(string):
    if string == string[::-1]:
        return True
    
    return False

print(palindrome("racecar"))