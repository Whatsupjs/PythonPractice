#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
def fibonacci():
    num = int(input("Enter how many number of Fibonnaci sequence you want: "))
    f0 = 0
    f1 = 1
    fresult = 0
    sequence = []

    for x in range(num):
        if x < 1: 
            fresult = 1
            sequence.append(fresult)
        else:
            fresult = f0 + f1
            sequence.append(fresult)
            f0 = f1
            f1 = fresult

    return sequence

print(fibonacci())