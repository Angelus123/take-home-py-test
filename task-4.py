# Create a function that takes in two parameters, a string and a character, and returns the number of times the character appears in the string.
def count_char_occurrences(str, char):

    count = 0
    for ch in str:
        if ch == char:
            count += 1
    return count

print (count_char_occurrences("Great to work on RevelTek test", "e")) # prints 5