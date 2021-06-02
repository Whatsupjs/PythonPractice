#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random 

def guessing():
    answer = random.randint(1,9)

    while True:
        usr_num = input("Enter a number between 1 and 9: ")

        if int(usr_num) >= 10:
            print("Number out of range, please try again")
        elif int(usr_num) > answer:
            print("Too high")
        elif int(usr_num) < answer:
            print("Too low")
        elif int(usr_num) == answer:
            print("Correct!")
            return False    

guessing()