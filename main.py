import random

words = [
    "elephant", "rainbow", "jazz", "ocean", "butterfly", "whisper", "mountain", "courage",
    "infinity", "harmony", "sunset", "chocolate", "laughter", "adventure", "sparkle", "guitar",
    "wonder", "serendipity", "echo", "inspiration", "zenith", "mystery", "quasar", "umbrella",
    "silhouette", "enigma", "effervescent", "cascade", "tranquility", "velvet", "labyrinth",
    "obsidian", "ethereal", "radiance", "solitude", "paradox", "cosmic", "infinity", "cathedral",
    "ripple", "synchronicity", "whimsical", "ephemeral", "enchanting", "quintessence", "melody",
    "silhouette", "ephemeral", "sonnet"]
guessed_letters = []
word_to_guess = random.choice(words)


def display_word(word):
    global guessed_letters
    console_output = ""
    for letter in word:
        if letter in guessed_letters:
            console_output += letter
        else:
            console_output += "_"
    return console_output


def hangman(max_tries):
    initial_tries = 0
    global guessed_letters

    print("Welcome to Hangman!")
    print(display_word(word_to_guess))

    while initial_tries < max_tries:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            initial_tries += 1
            print(f"Incorrect! {max_tries - initial_tries} tries remaining.")
        else:
            print("Correct!")

        current_display = display_word(word_to_guess)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You guessed the word!")
            break

    if "_" in current_display:
        print(f"You're out of tries! The  word was '{word_to_guess}'.")

# hangman(6)
