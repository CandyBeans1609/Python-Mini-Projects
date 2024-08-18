import random

def decode(word):
    if len(word) > 3:
        new_word = word[3:-3]
        new_word = new_word[-1] + new_word[:-1]
    else:
        new_word = word[::-1]
    return new_word

sentence = input("Enter the encoded message: ")
words = sentence.split()

decoded_words = []
for word in words:
    decoded_words.append(decode(word))

decoded_sentence = ' '.join(decoded_words)

print(decoded_sentence)