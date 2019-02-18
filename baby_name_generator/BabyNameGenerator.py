import string
print(string.ascii_letters)
print(string.ascii_lowercase)

import random
print(random.choice("pull a letter from here"))
print(random.choice(string.ascii_lowercase))

# The baby name generator selects any random
# letter, or specifically a random consonant or random vowel,
# as specified by the user input. 

# User can also enter a specific letter at a desired location. 
# For instance, user could specify that they want to return 
# names that start with "R" and end with "t",
# with randomly generated vowels and consonants in the middle.
