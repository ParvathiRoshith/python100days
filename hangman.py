word_list=['ardvark','baboon','camel']

#STEP 1
#Exercise-1
import random
chosen_word=random.choice(word_list)
#print(chosen_word)
#Exercise-2
#guess=input("Guess a letter: ").lower()
#Exercise-3
'''
for letter in chosen_word:
    if letter==guess:
        print("Right")
    else:
        print("Wrong")
'''

#STEP 2
#Exercise-1
display=[]
for i in range(len(chosen_word)):
    display+='_'
#Exercise-2
'''
for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter==guess:
        display[position]=letter
#Exercise-3
print(display)'''

#STEP 3
while display!=list(chosen_word):
    guess=input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
print("You Won!")