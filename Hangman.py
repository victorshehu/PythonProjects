#This an implementation for the hangman game in which a random word is given and you have to guess the word, You can only guess wrong 6 six times after which you lose and the correct answer is displayed

import random

listOfWord = ["Jesus", "is" , "best" , "so" , "thank", "God" , "today" ,"apple", "banana", "mango", "strawberry",  "orange", "grape", "pineapple", "apricot", "lemon", "coconut" ,"watermelon",
"cherry", "papaya", "berry", "peach", "lychee", "muskmelon"] # List of words

chosen_Word = listOfWord[random.randint(0, 5)] # a word is chosen at random from the list

numberOfTries = 6 # this is the number of tries a user gets
attempted_Word = [] # this list will hold the correct guesses the user make and position

for i in range(len(chosen_Word)): #This for loop place empty spaces in the attempted word array
    attempted_Word.append("_")

for i in range(len(chosen_Word)):
    print(attempted_Word[i] + " ", end='')
print()

while (True):

    if list(chosen_Word) == attempted_Word: #Checks if the two guess and the word are the same, if that is so it breaks out of the loop
            print("You Guessed the word correctly Congratulations")
            break
    elif (numberOfTries == 0 and list(chosen_Word) != attempted_Word ): #Checks the number of tries and if the guess word is completed
        print("Sorry you are out of tries")
        print(f'The correct word was "{chosen_Word}"')
        break
    else: # Prompts the user to keep guessing
        print(f'you have {numberOfTries}  guesses left')
        print("Guess the a letter in the word")

        letter = input()
        check = False
        for i in range (len(chosen_Word)): #Runs through the whole word to see if that letter is in the word
            if chosen_Word[i] == letter:
                attempted_Word[i] =letter
                check = True # I used this to kno if the guess is right of wrong

        if check:
            print("Right Guess")

        else:
            print("Wrong Guess")
            numberOfTries -= 1

        print()
        for i in range(len(chosen_Word)):
            print( attempted_Word[i] + " ", end ='')
            print()






