
import random

print("Guess the word game!" + "\n"
      "You have 10 tries to guess the word by letters!" + "\n"
      "Each letter is present one time in a word." + "\n"
      "Hint! Use only lower case letters." + "\n")

questions = ["Hereditary material in humans?", "Guido van Rossum's programming language?", "A version control system?"]
answers = ["dna", "python", "git"]

q_number = random.randint(0, len(questions) - 1)  # random selection of a question from list of questions

word = [letter for letter in str(answers[int(q_number)])]  # creation of a list of letters of the answer
mask = [symbol for symbol in str("_" * len(answers[int(q_number)]))]  # creation of the answer mask

print(questions[q_number])
print(mask)

failure = 0  # failure counter
success = 0  # success counter

letter = str(input("Enter a letter "))  # first user try

try_num = 10  # number of failures before game over

while success < len(answers[int(q_number)]):  # run if guessed letters less than the word lenght
    if letter in word:  # run if guessed
        mask[int(word.index(letter))] = letter
        print(mask)
        success = success + 1
        if success == len(answers[int(q_number)]):  # run if whole word is guessed
            print("Congratulations, you are win!")
        else:  # run if part of the word is guessed
            letter = str(input("Good, enter the next letter "))
            continue
    else:  # run if NOT guessed
        failure = failure + 1
        if failure < try_num:  # run if tries number is NOT exceeded
            letter = str(input("Oops, try again "))
            continue
        else:  # run if tries number is exceeded
            print("Sorry, game over!")
            break