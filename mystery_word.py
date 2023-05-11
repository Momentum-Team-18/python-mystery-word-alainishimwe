import random

def play_game():
    
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

        print("Instructions: Enter 1 if you want a word with 4-6 char, Enter 2 if you want a word with 6-8 chars, Enter 3 if you want a word with 8+ chars")

        # user select level of difficulty:
        pick_level = int(input("what level of difficulty do you want: "))

        # selected_word is assigned based on chosen level of diff
        if pick_level ==1:
            selected_word = select_easy_word
        elif pick_level ==2:
            selected_word = select_normal_word
        elif pick_level ==3:
            selected_word = select_hard_word

        print(selected_word)





        #working on input
        guesses = 8
        correct_guessed_letters = []
        incorrect_guessed_letters = []

        print("The random word has " + str(len(selected_word)) + " letters")

        display = []
        # selected_word_display = []
        for elem in selected_word:
            display.append("_")
        print(display)

        # for elem in selected_word:
        #     selected_word_display.append(elem)
        # print(selected_word_display)
        

        while guesses > 0:
            letter = (input("guess a letter:  ")).lower()
            # display=[]
            if letter in selected_word:
                for i in range(len(selected_word)):
                    if selected_word[i] == letter:
                        display[i] = letter
                print(''.join(display))
                
                # for elem in selected_word:
                    
                    
                #     if letter == elem:
                #         display += letter
                #         # print(display)
                        
                #     elif letter != elem:
                #          display +=  "-"
                #         # print(display)
                # print(display)            
                
            #print(guessedletters)
            
            

    



                print("good job")
            
                correct_guessed_letters.append(letter)
            # print(display)
            # print(correct_guessed_letters)
            elif letter not in selected_word and letter not in incorrect_guessed_letters:
                incorrect_guessed_letters.append(letter)
                print('nope')
                guesses -= 1
                print("you have " + str(guesses) +  " guesses left")
            else:
                print("you have already guessed that letter. Try another one")

            if selected_word == ''.join(display):
                print("Excellent!! you guessed the right word")


                
        print("The random word is " + selected_word)    
        print(incorrect_guessed_letters)
        print('The letters you guessed correctly are ' + ''.join(display))
        print(''.join(incorrect_guessed_letters))




if __name__ == "__main__":
    play_game()
