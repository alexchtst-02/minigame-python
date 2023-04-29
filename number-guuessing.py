import random as rd

upper = int(input(""))

number = rd.randint(0, upper+1)

print("Guessing Number bettwen zero to {}".format(upper))
guessing = int(input("Enter your answer>_ "))


while guessing != number:
    if abs(guessing-number)/upper <= 0.1:
        print("you are so close")
    elif abs(guessing-number)/upper > 0.1 and abs(guessing-number)/upper <= 0.2:
        print("you are prety close")
    elif abs(guessing-number)/upper > 0.2 and abs(guessing-number)/upper <= 0.4:
        print("you are far enough")
    else:
        print("you are so far from the number")
    guessing = int(input("Enter your answer>_ "))
else:
    print("you get it")