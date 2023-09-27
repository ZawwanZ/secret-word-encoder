import random

# Define the original character set
original_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "

# Shuffle the characters to create a unique mapping
shuffled_characters = list(original_characters)
random.shuffle(shuffled_characters)

# Create the substitution cipher as a dictionary
SUBSTITUTION_CIPHER = {}
for original, substitute in zip(original_characters, shuffled_characters):
    SUBSTITUTION_CIPHER[original] = substitute

print(SUBSTITUTION_CIPHER)