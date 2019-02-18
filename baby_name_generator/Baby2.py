import random, string

letter1 = random.choice(string.ascii_lowercase)
letter2 = random.choice(string.ascii_lowercase)
letter3 = random.choice(string.ascii_lowercase)
letter4 = random.choice(string.ascii_lowercase)
letter5 = random.choice(string.ascii_lowercase)

# ask user for some input
 
letter_input1 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input2 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input3 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input4 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input5 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')

# create a condition vowels and consonants

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase

def generator():
    if letter_input1 == "v":
        letter1 = random.choice(vowels)
    elif letter_input1 == "c":
        letter1 = random.choice(consonants)
    elif letter_input1 == "l":
        letter1 = random.choice(letter)
    else: 
        letter1 = letter_input1 # allowing user to select a specific letter

    if letter_input2 == "v":
        letter2 = random.choice(vowels)
    elif letter_input2 == "c":
        letter2 = random.choice(consonants)
    elif letter_input2 == "l":
        letter2 = random.choice(letter)
    else: 
        letter2 = letter_input2

    if letter_input3 == "v":
        letter3 = random.choice(vowels)
    elif letter_input3 == "c":
        letter3 = random.choice(consonants)
    elif letter_input3 == "l":
        letter3 = random.choice(letter)
    else: 
        letter3 = letter_input3

    if letter_input4 == "v":
        letter4 = random.choice(vowels)
    elif letter_input4 == "c":
        letter4 = random.choice(consonants)
    elif letter_input4 == "l":
        letter4 = random.choice(letter)
    else: 
        letter4 = letter_input4

    if letter_input5 == "v":
        letter5 = random.choice(vowels)
    elif letter_input5 == "c":
        letter5 = random.choice(consonants)
    elif letter_input5 == "l":
        letter5 = random.choice(letter)
    else: 
        letter5 = letter_input5

    name = letter1+letter2+letter3+letter4+letter5
    return(name)

for i in range(11):
    print(generator())
