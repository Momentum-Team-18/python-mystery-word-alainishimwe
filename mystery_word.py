def play_game():
    import random

    with open('words.txt') as f:
        text = f.read()
        text_full = text.split()
        # print(text)
        # # print(text_full)

        selected_word = random.choice(text_full)
        print(selected_word)



        #working on input
        guesses = 8
        correct_guessed_letters = []
        incorrect_guessed_letters = []

        print("The random word has " + str(len(selected_word)) + " letters")

        while guesses > 0:
            
            letter = (input("guess a letter:  ")).lower()
            
            #print(guessedletters)
            
            if letter in selected_word:
                for elem in selected_word:
                    display=''
                    if letter == elem:
                        display += letter
                        print(display)
                    elif letter != elem:
                        display += "_"
                        print(display)
                    # return display

                    
                
                # for element in selected_word:
                #     if letter == element:
                #         display += element
                #         print(display)
                #     else:
                #         print(letter)
                # display = ''



                # for index in range(len(selected_word)):
                    
                #     if  letter == selected_word[index]:
                #         print(letter)
                #     else:
                #         print(letter)
                # print(new)

            # print(display)
                    # elif letter != selected_word[index]:
                    #     print(selected_word.replace(selected_word[index], '_'))



                print("good job")
            # print(display)
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

            if selected_word == ''.join(correct_guessed_letters):
                print("you got it")


                
        print("The random word is " + selected_word)    
        print(correct_guessed_letters)
        print(incorrect_guessed_letters)
        print(''.join(correct_guessed_letters))
        print(''.join(incorrect_guessed_letters))




if __name__ == "__main__":
    play_game()
