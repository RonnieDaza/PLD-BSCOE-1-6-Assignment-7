# Program 1 - Word, Vowel, and Consonant Counter
# Create a program that asks for a sentence as input.
# Display the number of words, vowels, and consonants in the input.
# Example:
# Input: Bahala kayo dyan
# Output:
# Words: 3
# Vowels: 6
# Consonant: 8

# Steps
# 1. Ask the user for the desired sentence.
userSentence = input("Enter your desired sentece: ")

# 2. Set the wordCount to 0.
wordCount = 0

# 3. Create a for loop to count the words in the given sentence.
for letter in userSentence:
    # 4. Test if the letter is equal to " " to signify that the word is a true word.
    if letter == " ":
        # 5. If the word is tested as a true word, add 1 to the wordCount.
        wordCount = wordCount+1

# 6. Save the wordCount with +1 to the totalWords so that it can display the total words.
totalWords = wordCount+1