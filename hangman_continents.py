import random
print("Hangman")
print("Game of Continents")
fail = 0
guess = 5
continents = ("North America", "South America", "Europe", "Asia", "Antartica", "Australia")
secret_word = random.choice(continents)

while guess > fail:
    guess_word = input("\nGuess the Continent: ").title()
    guess -= 1
    if guess_word == secret_word:
        print("\nCongrats .... You WON the Game!")
        break
    elif guess_word != secret_word:
        print("Wrong Guess")
    print(f"Guesses left : {guess}")
else:
    print("\nOops, you LOST the Game!")
    print(f"The Word was {secret_word}")
