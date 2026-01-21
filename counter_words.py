# Simple program to count the number of word in a sentence

def count_words(sentence):
    words = sentence.split()
    return len(words)

text = input('Enter a sentence: ')
print(f'The sentence "{text}" has {count_words(text)} words.')