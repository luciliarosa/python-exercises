# Simple program to count the number of characters in a word

def count_letters(word):
    return len(word)

text = input('Digite uma palabra: ')
print(f'A palavra {text} tem {count_letters(text)} letras')