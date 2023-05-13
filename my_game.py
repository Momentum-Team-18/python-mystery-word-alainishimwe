import random

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def fun_game():
        with open('words.txt') as f:
            text = f.read()
            text_full = text.split()
            # each empty list will store words of different lengths
            easy_text =  []
            normal_text = []
            hard_text = []
            for word in text_full:
                if len(word) >=4 and len(word) < 6:
                    easy_text.append(word)
                elif len(word) >=6 and len(word) <=8:
                    normal_text.append(word)
                else:
                    hard_text.append(word)
            # each variable has a random words that meets length requiremnts because it was selected from the right list
            select_easy_word = random.choice(easy_text)
            select_normal_word = random.choice(normal_text)
            select_hard_word = random.choice(hard_text)

            print(Style.BRIGHT + Fore.CYAN + "Instructions: Enter 1 if you want a word with 4-6 char, Enter 2 if you want a word with 6-8 chars, Enter 3 if you want a word with 8+ chars.")

            # user select level of difficulty:
            pick_level = int(input(Fore.RED + "What level of difficulty do you want: "))

            # selected_word is assigned based on chosen level of diff
            if pick_level ==1:
                selected_word = select_easy_word
            elif pick_level ==2:
                selected_word = select_normal_word
            elif pick_level ==3:
                selected_word = select_hard_word
            else:
                print("Your input was invalid. Please enter 1 or 2 or 3")
                fun_game()

            
            guesses = 8   # limiting number of incorrext guesses to 8
            correct_guessed_letters = [] #empty list to store correct guessed letters
            incorrect_guessed_letters = [] #empty list to store incorrect guessed letters

            #Displaying the number of letters of the random word
            print(Fore.MAGENTA + f"The random word has {str(len(selected_word))}  letters")

            # empty list that holds partially correct guessed letters as the user plays
            display = []
            
            #This loops through the random word and replaces each char with a '-'
            for elem in selected_word:
                display.append("_")
            print(''.join(display))

            print(selected_word)


            while guesses > 0:
                letter = (input(Style.BRIGHT + "guess a letter:  ")).lower()
                """
                if the letter entered is in the random word and it's one letter
                the for loop will go iterate through each position of the random word
                and if the current position matches the letter, that letter will replace the '-'
                """
                if letter in selected_word and len(letter) ==1:
                    for i in range(len(selected_word)):
                        if selected_word[i] == letter:
                            display[i] = letter
                    print(Fore.GREEN + ''.join(display))
                    print(Fore.YELLOW + Style.BRIGHT +  "Correct guess. Proceed with your next guess!")

                # adding correct guessed letter to the list
                    correct_guessed_letters.append(letter)
    
                # if the guess is incorrect and the guessed letter is new then 
                # substract 1 from guesses remaining
                elif letter not in selected_word and letter not in incorrect_guessed_letters and len(letter) ==1:
                    incorrect_guessed_letters.append(letter)
                    print('Incorrect guess. Try again!')
                    guesses -= 1
                    print(Back.LIGHTRED_EX + Style.BRIGHT + f"you have {str(guesses)} guesses left")
                # if user enter more than one letter, warn them but don't take off #of guesses
                elif len(letter) >1:
                    print("Enter one letter at a time")
                # if user enter a previously guessed letter, let them know but don't take off # of guesses
                else:
                    print("you have already guessed that letter. Try another one")
                # if guessed letter match the random word before running out of guesses
                # let user know and ask them if they want to play again
                #if yes, then call back fun_game f(n) to start over the game
                #otherwise Thank them but leave them with option to plYay again if they
                #change their mind
                if selected_word == ''.join(display):
                    print(Style.BRIGHT + Fore.GREEN + "Excellent!! you guessed the right word")
                    print( Fore.GREEN + Style.BRIGHT + f"THE RANDOM WORD IS {selected_word.upper()}")
                    print(Style.BRIGHT + f"The letters you guessed correctly are {''.join(display)}")
                    print(Style.BRIGHT + f"The letters you guessed incorrectly are {''.join(incorrect_guessed_letters)}")
                    play_again = int(input(Style.BRIGHT + Fore.BLUE + "Do you want to play again? Enter 1 if yes or 0 if no "))
                    if play_again ==1:
                        fun_game()
                    else:
                        print("THANK YOU FOR PLAYING!!")
                        changed_mind = int(input(Style.BRIGHT + Fore.BLUE + "Enter 1 if you change your mind and want to play again: "))
                        if changed_mind ==1:
                            fun_game()
            # displaying the random word, letters guessed correctly and incorrectly
            # at the end of guesses        
            print( Fore.GREEN + Style.BRIGHT + f"THE RANDOM WORD IS {selected_word.upper()}")    
            print(Style.BRIGHT + f"The letters you guessed correctly are {''.join(display)}")
            print(Style.BRIGHT + f"The letters you guessed incorrectly are {''.join(incorrect_guessed_letters)}")
            # after player runs out of guesses, ask them if they want to play again
            # if yes, start over the game. Otherwise, give them the instructions on how to proceed if they change their mind
            while guesses == 0:
                play_again = int(input(Style.BRIGHT + Fore.BLUE + "Do you want to play again? Enter 1 if yes or 0 if no: "))
                if play_again ==1:
                    fun_game()
                else:
                    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "THANK YOU FOR PLAYING")
                    changed_mind = int(input(Style.BRIGHT + Fore.BLUE + "Enter 1 if you change your mind and want to play again: "))
                    if changed_mind == 1:
                        fun_game()

def play_game():
    fun_game()

if __name__ == "__main__":
    play_game()
