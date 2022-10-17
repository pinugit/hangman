import random
import string

def wordinit():
    #this function will select a random word from the file words.txt  
    
    with open("words.txt") as words:
        #this with code block will convert word.txt file into a list od word
        words_read = words.read()
        words_list = words_read.split(" ")
        
    # now , selecting a random word from the word list 
    random_selected_word = random.choice(words_list)
    
    return random_selected_word

print(wordinit())