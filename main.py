import random


from Jogo_Forca_palavras import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

from logo import logo
print(logo)

lives = 6

print(f"The solution is {chosen_word}")

display = []


for _ in range(word_length):
   display += "_" 


end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()



    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position} \n Current letter: {letter} \n Guessed letter: {guess}")

        if letter == guess:
           display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    from logo import stages
    print(stages[lives])

