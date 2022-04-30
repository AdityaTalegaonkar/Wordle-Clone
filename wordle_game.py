import random

word_list=['which','there','their','about','would']
word = random.choice(word_list)

def wordle_clone(str):
    for i in range(6):
        flag = True
        guess = input('What is your guess??')
        if len(guess) != len(str):
            print(f'You enter a guess with the wrong number of charactor, you should enter a guess  with {len(str)} character, and not {len(guess)} charcter like you did ')
            flag = False
        while not flag:
            guess = input('Enter another guess: ')
            if len(guess) == len(str):
                flag = True
                
        for j in range(len(str)):
            if j == 0:
                if str == guess:
                    print(f'you guess the correct word in {i+1} guessed, congratulatios yon won !!')
                    return
            if guess[j] == str[j]:
                print(guess[j],end = '')
            elif guess[j] in str and guess.count(guess[j]) <= str.count(guess[j]):
                print(guess[j].upper(), end='')
            else:
                print('_',end='')     
        print('')

wordle_clone(word)