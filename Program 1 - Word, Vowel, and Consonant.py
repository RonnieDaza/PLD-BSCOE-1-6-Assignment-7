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

# 2. Set the wordCount variable to 0.
wordCount = 0

# 3. Create a for loop to count the words in the given sentence.
for letter in userSentence:
    # 4. Test if the letter is equal to " " to signify that the word is a true word.
    if letter == " ":
        # 5. If the word is tested as a true word, add 1 to the wordCount variable.
        wordCount = wordCount+1

# 6. Save the wordCount with +1 to the totalWords variable so that it can display the final total words.
totalWords = wordCount+1

# 7. Print the total words counted in the given sentence.
print("The word count is: ", totalWords)

# 8. Moving on, we now need to count the vowels and letters in the given sentence.
# 9. Set the vowelLettersCount variable to 0.
vowelLettersCount = 0
# 10. Set the consonantLettersCount variable to 0.
consonantLettersCount = 0

# 11. Create a for loop to count the letters in the given sentence.
for everyVowelLetters in range(0, len(userSentence)):
    # 12. Test if the letter is not equal to " " so that the " " can not be included in the count.
    if userSentence[everyVowelLetters] != " ":
        # 13. Test if the letter is a, e, i, o, or u if lowercase letters or A, E, I, O, or U if uppercase letters.
        if userSentence[everyVowelLetters] == "a" or userSentence[everyVowelLetters] == "e" or userSentence[everyVowelLetters] == "i" or userSentence[everyVowelLetters] == "o" or userSentence[everyVowelLetters] == "u" or userSentence[everyVowelLetters] == "A" or userSentence[everyVowelLetters] == "E" or userSentence[everyVowelLetters] == "I" or userSentence[everyVowelLetters] == "O" or userSentence[everyVowelLetters] == "U":
            # 14. If the letter is correct, add 1 to the vowelLettersCount variable.
            vowelLettersCount = vowelLettersCount+1
        else:
            # 15. If the nothing matches the description, then the letter is a consonant. Add 1 to the consonantLettersCount variable.
            consonantLettersCount = consonantLettersCount+1

# 16. Print the vowel letter count in the given sentence.
print("The vowel letter count is: ", vowelLettersCount)
# 17. Print the consonant letter count in the given sentence.
print("The consonant letter count is: ", consonantLettersCount)