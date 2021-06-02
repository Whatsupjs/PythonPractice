#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
def divisorlist():
    num = input("Please enter a number: ")
    dlist = []

    for x in range(1, int(num)+1):
        if int(num) % x == 0:
            dlist.append(x)

    return dlist

print(divisorlist())