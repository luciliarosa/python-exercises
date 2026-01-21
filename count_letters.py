# Simple program to count the number of characters in a word

def count_letters(word):
    return len(word)

text = input('Enter a word: ')
print(f'The Word {text} has {count_letters(text)} letters')