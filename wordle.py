import random
import os
from colorama import Fore, Style
from time import sleep

os.system('color')

Style.RESET_ALL

with open("five_letter_words.txt") as d:
    word_list = [ entry.strip('\n').upper() for entry in d.readlines() ]

wrong = Fore.WHITE
right = Fore.YELLOW
perfect = Fore.GREEN

win = [perfect, perfect, perfect, perfect, perfect]

def get_word():
    return [ char for char in word_list[ random.randint(0,len(word_list)) ] ]

def play():
    word = get_word()
    colors = [wrong, wrong, wrong, wrong, wrong]
    turn = 1
    
    display_line = ['_', '_', '_', '_', '_']

    def display(step, line, colored):
        char0 = line[0]
        char1 = line[1]
        char2 = line[2]
        char3 = line[3]
        char4 = line[4]

        color0 = colored[0]
        color1 = colored[1]
        color2 = colored[2]
        color3 = colored[3]
        color4 = colored[4]
    
        print(f"{step}: {color0}{char0} {color1}{char1} {color2}{char2} {color3}{char3} {color4}{char4} {Style.RESET_ALL}")

    display(0, display_line, colors)

    guess = ''

    while guess == '':
        guess = input("Your guess: ")

        if guess.upper() not in word_list:
            print("Not in dictionary")
            guess = ''
        
        else:
            next_display = [ char.upper() for char in guess]

            for i in range(5):
                char = next_display[i]                
                if char in word:
                    colors[i] = right
                if char == word[i]:
                    colors[i] = perfect
            
            display(turn, next_display, colors)

            if colors == win:
                print("Winner!")
                replay = input("Play again? Y/N ")
                if replay.upper() not in ('Y', 'N'):
                    print("Please hit the Y key or the N key you cabbage. There's no error checking after this line.")
                    replay = input("Play again? Y/N ")
                if replay.upper() == 'N':
                    print("closing...")
                    sleep(2)
                    quit()
                if replay.upper() == 'Y':
                    print("Selecting new word:")
                    display('', display_line, [wrong, wrong, wrong, wrong, wrong])
                    word = get_word()
            elif turn >= 6:
                print("LOSER!  It was:")
                display('', word, [wrong, wrong, wrong, wrong, wrong])
                turn = 1
                print()
                print("Selecting new word:")
                display('', display_line, [wrong, wrong, wrong, wrong, wrong])
                word = get_word()
            
            guess = ''
            colors = [wrong, wrong, wrong, wrong, wrong]
            turn += 1
            

play()
