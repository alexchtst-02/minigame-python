import random as rd
import json

f = open('dataanimal.json')
animal = json.load(f)

def alphabet_count(word):
    if type(word) == str:
        count = 0
        for i in word:
            if i != ' ':
                count = count + 1
    return(count)

def word_count(word):
    if type(word) == str:
        n = 0
        index = []
        for i in word:
                if i == ' ' :
                    index.append(n)
                n = n + 1
    return(index)

def function(inputs):
    my_str = ''
    for i in inputs:
        if i == '-':
            my_str = my_str + ' '
        else:
            my_str = my_str + i
    return(my_str)

answer = animal[rd.randint(0, len(animal)-1)]
answer = answer.lower()

info = ''

for i in range(len(answer)):
    if i in word_count(answer):
        info = info + '-'
    else:
        info = info + '_'

print('Guess the animal: ')
print('The clue is there are {} word with {} alphabet'.format(len(word_count(answer))+1, alphabet_count(answer)))
print(info)

info_list = list(info)
count = 0
user_answer = ''
a = 0

while user_answer != answer:
    my_str = input('').lower()
    if len(my_str) == 1 and a <= int(alphabet_count(answer)/3):
        for i in range(len(answer)):
            if answer[i] == my_str:
                info_list[i] = my_str
    else:
        for alphabet,index in zip(my_str, range(len(my_str))):
            if answer[index] == alphabet:
                info_list[index] = alphabet
    user_answer = function(info_list)
    print(function(info_list))
    
    count = count + 1

print('number of guessing are {}'.format(count))
f.close()