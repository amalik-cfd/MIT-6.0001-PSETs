# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
#secret_word = 'apple'
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word = ''.join(sorted((set(secret_word))))
    letters_guessed = ''.join((sorted(letters_guessed)))
    if secret_word in letters_guessed: return True
    else: return False

#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(is_word_guessed(secret_word, letters_guessed))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed = ['_']*len(secret_word)
    for k in range(len(secret_word)): 
        if secret_word[k] in letters_guessed:
            guessed[k] = secret_word[k]
        else:
            continue
    return ' '.join(guessed)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    k  =string.ascii_lowercase
    for i in letters_guessed:
            k = k.replace(i,'')
    return k
    
    
vowels = 'aeiou'
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    n = len(secret_word)
    print('Welcome to the game Hangman!\nI am thinking of a word',n,'letters long\n--------------')
    letters_guessed = []
    k =3
    i = 6
    print('You have 3 warnings left\nYou have 6 guesses left')
    def warnings(i,k,inp,letters_guessed):
        if not str.isalpha(inp):
            if k == 0:
                i-=1
                print('Oops! That is not a valid letter. You have',k,'warnings left\n',get_guessed_word(secret_word, letters_guessed))
            else: 
                print('Oops! That is not a valid letter. You have',k-1,'warnings left\n',get_guessed_word(secret_word, letters_guessed))
                k-=1
        elif inp in letters_guessed:
            if k == 0:
                i-=1
                print('Oops! his letter has already been guessed. You have',k,'warnings left\n',get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! This letter has already been guessed. You have',k-1,'warnings left\n',get_guessed_word(secret_word, letters_guessed))
                k-=1
        elif inp not in secret_word:
            letter_guessed = str.lower(inp)
            letters_guessed.append(letter_guessed)
            print('Oops! That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
            if inp in vowels:
                i-=2
            else:
                i-=1
        else:
            letter_guessed = str.lower(inp)
            letters_guessed.append(letter_guessed)
            print('Good guess:',get_guessed_word(secret_word, letters_guessed))
        return k,i
    while i >0:
        print('Available letters:',get_available_letters(letters_guessed))
        inp = input('Please guess a letter:')
        k,i = warnings(i,k,inp,letters_guessed)
        if i ==0:
            print ('Sorry you ran out of guesses, the word was', secret_word)
            break
        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!\nYour total score for this game is: ',i*n)
            break   
        print('You have',i,'Guesses left') 
    
    
    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ','')
    t =0
    if len(my_word) == len(other_word):
        for n in range(len(my_word)):
            if my_word[n] == other_word[n] or my_word[n]=='_':
                t+=1
            if t == len(my_word):
                return True
            
         
        


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
              Keep in mind that in hangman when a letter is guessed, all the positions
              at which that letter occurs in the secret word are revealed.
              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
              that has already been revealed.

    '''
    other_word = wordlist #['aaple','apple','aeiou']
    matches_list = []
    for k in other_word:
        if match_with_gaps(my_word, k):
            matches_list.append(k)
    if len(matches_list) == 0: print('No matches found')
    return matches_list



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    n = len(secret_word)
    print('Welcome to the game Hangman!\nI am thinking of a word',n,'letters long\n--------------')
    letters_guessed = []
    k =3
    i = 6
    print('You have 3 warnings left\nYou have 6 guesses left')
    def warnings(i,k,inp,letters_guessed):
        if inp == '*':
            print('Possible word matches are\n',show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            return k,i
        if not str.isalpha(inp):
            if k == 0:
                i-=1
                print('Oops! That is not a valid letter. You have',k,'warnings left\n',get_guessed_word(secret_word, letters_guessed))
            else: 
                print('Oops! That is not a valid letter. You have',k-1,'warnings left\n',get_guessed_word(secret_word, letters_guessed))
                k-=1
        elif inp in letters_guessed:
            if k == 0:
                i-=1
                print('Oops! his letter has already been guessed. You have',k,'warnings left\n',get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! This letter has already been guessed. You have',k-1,'warnings left\n',get_guessed_word(secret_word, letters_guessed))
                k-=1
        elif inp not in secret_word:
            letter_guessed = str.lower(inp)
            letters_guessed.append(letter_guessed)
            print('Oops! That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
            if inp in vowels:
                i-=2
            else:
                i-=1
        else:
            letter_guessed = str.lower(inp)
            letters_guessed.append(letter_guessed)
            print('Good guess:',get_guessed_word(secret_word, letters_guessed))
        return k,i
    while i >0:
        print('Available letters:',get_available_letters(letters_guessed))
        inp = input('Please guess a letter:')
        k,i = warnings(i,k,inp,letters_guessed)
        #if letter_guessed in secret_word:
            #print('Good guess:',get_guessed_word(secret_word, letters_guessed))
        if i <=0:
            break
        print('You have',i,'Guesses left')
        # elif letter_guessed in vowels:
        #     print('You have',k,'warnings left\nYou have',i,'guesses left')
        # else:
        #     print('You have',k,'warnings left\nYou have',i,'guesses left')
    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!\nYour total score for this game is: ',i*n)
    else:
        print ('Sorry you ran out of guesses, the word was', secret_word)

    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    #secret_word = 'apple'
    hangman_with_hints(secret_word)
