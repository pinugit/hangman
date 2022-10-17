import random
import sys

def wordinit():
    #this function will select a random word from the file words.txt 
    
    with open("words.txt") as words:
        #this with code block will convert word.txt file into a list of word
        words_read = words.read()
        words_list = words_read.split(" ")
        
    # now , selecting a random word from the word list 
    random_selected_word = random.choice(words_list)
    
    return random_selected_word


def printuserword(word, letter):
    #This function will print out the word in "_" format and if the letter is present which is given it will replace "_" with the letter
    for letters in word:
        if letter is letters:
            sys.stdout.write(letter)
        else :
            sys.stdout.write("_")

# guesses = 6

# # while guesses > 0:
# #     user_guess = chr(input("Enter your guess :"))
    
# #     if 