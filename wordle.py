#### MODULES ####
import random
import os
from colorama import Fore, Style
from time import sleep
####


#### FILES ####
with open("five_letter_words.txt") as d:
    dale_list = [ entry.strip('\n').upper() for entry in d.readlines() ]

with open("wordle_solutions.txt") as dd:
    wordle_list = [ entry.strip('\n').upper() for entry in dd.readlines() ]

with open("wordle_acceptable.txt") as ddd:
    wordle_acceptable = [ entry.strip('\n').upper() for entry in ddd.readlines() ]
####


#### VARIABLES ####
word_list = []
acceptable_list = []

wrong = Fore.WHITE
right = Fore.YELLOW
perfect = Fore.GREEN

win = [perfect, perfect, perfect, perfect, perfect]
####

# Allow system settings to display colours.
os.system('color')
Style.RESET_ALL


#### FUNCTIONS
def set_game_settings():
    # Used when file is first loaded to set word_list and acceptable_list for the session.
    # returns list, list
    settings = ''
    while settings.lower() not in ('original', 'dale'):
        settings = input('Play ORIGINAL , or DALE mode? ')

    if settings == 'original':
        acceptable_words = wordle_list + wordle_acceptable
        return(wordle_list, acceptable_words)

    if settings == 'dale':
        return(dale_list, dale_list)


def get_word():
    # Used at start of each new game to randomly choose a word from word_list.
    # returns length five list of single character strings, e.g. [ 'W', 'O', 'R', 'D', 'S' ]
    return [ char for char in word_list[ random.randint(0,len(word_list)) ] ]


def play():
    # Main function to run game. Continues until restart() function closes session.
    
    ### VARIABLES ###
    word = get_word()                               # solution to current round
    colors = [wrong, wrong, wrong, wrong, wrong]    # five colours to be used for display
    turn = 1                                        # turn counter
    streak = 0                                      # win-streak counter
    display_line = ['_', '_', '_', '_', '_']        # used at start of round before first guess
    ###

    # Display solution for debugging:
    #print(word) 

    ### FUNCTIONS ###
    def display(step, line, colored):
        # Prints to screen turn number and current guess, colourised.
        # accepts   step    int
        #           line    list
        #           colored list
        # prints "{int}:, G U E S S"

        ## VARIABLES ##

        # Five characters used in guess, read from input {line}
        char0 = line[0]
        char1 = line[1]
        char2 = line[2]
        char3 = line[3]
        char4 = line[4]

        # Five colours used when displaying, read from input {colored}
        color0 = colored[0]
        color1 = colored[1]
        color2 = colored[2]
        color3 = colored[3]
        color4 = colored[4]
        ##

        # Prints using colorama modules e.g. {Fore.GREEN}{'D'}
        print(f"{step}: {color0}{char0} {color1}{char1} {color2}{char2} {color3}{char3} {color4}{char4} {Style.RESET_ALL}")

    def play_again():
        # Wrapper to receive user input. Will not continue until acceptable input is entered.
        # returns single character string, either 'Y', or 'N'
        replay = ''
        while replay.upper() not in ('Y','N'):
            replay = input("Play again? Y/N ")
        return(replay.upper())

    def restart():
        # Runs after a correct guess or a failure after six turns. Accepts user input and
        # either starts new round or closes the session.
        
        ## VARIABLES
        global turn             # takes game turn counter to reset to 0 for new game
        replay = play_again()   # takes user input either 'Y' or 'N'
        ##

        # start new round
        if replay.upper() == 'Y':
            print("Selecting new word:")
            word = get_word()
            display('', display_line, [wrong, wrong, wrong, wrong, wrong])
            turn = 0
            return(turn,word)

        # close session
        if replay.upper() == 'N':
            print("closing...")
            sleep(2)
            quit()
    ###


    # prints first blank line to screen
    display(0, display_line, colors)

    # takes user input, accepts only five letter words from acceptable_list (based on set_game_settings() )
    guess = ''
    while guess == '':
        guess = input("Your guess: ")

        if guess.upper() not in acceptable_list:
            print("Not in dictionary")
            guess = ''
        
        else:
            # breaks guess into string of five characters
            next_display = [ char.upper() for char in guess]

            # compares each character to solution and assigns colours
            for i in range(5):
                char = next_display[i]               
                if char in word:
                    colors[i] = right
                if char == word[i]:
                    colors[i] = perfect

            # prints colourised guess to screen
            display(turn, next_display, colors)

            # checks whether guess is correct answer
            # if correct, adds to win-streak counter and offers a new game
            if colors == win:
                print("Winner!")
                streak += 1
                print(f"streak = {streak}")
                turn, word = restart()

            # checks whether turn limit is exceeded
            # if so, solution is shown, win-streak counter is reset, and offers a new game
            elif turn >= 6:
                print("LOSER!  It was:")
                display('', word, [wrong, wrong, wrong, wrong, wrong])
                turn, word = restart()
                streak = 0

            # resets guess and colours for next entry, increments turn counter
            guess = ''
            colors = [wrong, wrong, wrong, wrong, wrong]
            turn += 1
####
            

# Game begins
# asks user for choice of settings to establish word list(s)
print("#### Welcome to Wordle (knock-off)! ####")
print(" ")
print("Would you like to play with the ORIGINAL Wordle word-list (a smaller selection of more common words), or with the DALE list (larger selection of less common words and no silly-americanisms)?")

word_list, acceptable_list = set_game_settings()

play()
