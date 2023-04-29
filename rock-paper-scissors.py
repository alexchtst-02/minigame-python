import random as rd

myList = ['Rock', 'Paper', 'Scissors']

def scoring(var1, var2):
    if var1 == "Rock" and var2 == "Scissors":
        score = 1
    elif var1 == "Paper" and var2 == "Rock":
        score = 1
    elif var1 == "Scissors" and var2 == "Paper":
        score = 1
    elif var1 == "R" and var2 == "Scissors":
        score = 1
    elif var1 == "P" and var2 == "Rock":
        score = 1
    elif var1 == "S" and var2 == "Paper":
        score = 1
    elif var1 == "Rock" and var2 == "S":
        score = 1
    elif var1 == "Paper" and var2 == "R":
        score = 1
    elif var1 == "Scissors" and var2 == "P":
        score = 1
    else:
        score = 0
    return(score)

user_score = 0
computer_score = 0

print("Rock/Paper/Scissors User against Computer")
print("Clue : You can type ('Rock' or R), ('Paper' or P), ('Scissors' or S) as your choice")
print("Hope you understand, let's begin")

condition = True
while condition:
    user_input = input("").capitalize()
    computer_input = myList[rd.randint(0, 2)]
    user_score += scoring(user_input, computer_input)
    computer_score += scoring(computer_input, user_input)
    if user_input == 'P':
        user_input = 'Paper'
    elif user_input == 'R':
        user_input = 'Rock'
    elif user_input == 'S':
        user_input = 'Scissors'
    else:
        pass
    print(user_input, computer_input)
    print(user_score, computer_score)
    if user_score == 3 or computer_score == 3:
        condition = False
else:
    if user_score == 3:
        print("Congrats, you just won")
    else:
        print("You just lose against a computer")