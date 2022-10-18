import random

def wordinit():
    #this function will select a random word from the file words.txt 
    
    with open("words.txt") as words:
        #this with code block will convert word.txt file into a list of word
        words_read = words.read()
        words_list = words_read.split(" ")
        
    # now , selecting a random word from the word list 
    random_selected_word = random.choice(words_list)
    
    return random_selected_word

#this finction will conver the list to a string
def listToString(list):
    convertedString = ""
    for item in list:
        convertedString += item
    return convertedString    

def replaceLetter(word, user_input):
    for i in word:
        if user_input == i:
            underscore_list[word.rfind(user_input)] = user_input #word.rfind(user_input) will find the index of user_input letter in the word 
        
guess = 6
underscore_list = []
random_word = wordinit()

#this for loop will convert the random word to all underscores
for letters in random_word:
    underscore_list.append("_")

convertedString = listToString(underscore_list)
print(convertedString)


while guess > 0 :
    user_guess = str(input("Enter your guess"))
    
    if user_guess in random_word:
        print("found")
        replaceLetter(random_word, user_guess)
        print(listToString(underscore_list))
        # if 
        
    else:
        guess -= 1
        
        
