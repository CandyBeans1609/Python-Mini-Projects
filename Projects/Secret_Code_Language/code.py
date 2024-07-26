import random

characters = list('qwertyuiopasdfghjklzxcvbnm')

def encode(word):
    if len(word) > 3:
        
        word = word[1:] + word[0]
        random.shuffle(characters)
        before = characters[:3]
        random.shuffle(characters)
        after = characters[:3]
        new_word = ''.join(before) + word + ''.join(after)
    else:
        new_word = word[::-1]
    return new_word

sentence = input("Enter the message: ")
words = sentence.split()

encoded_words = []
for word in words:
    encoded_words.append(encode(word))

encoded_sentence = ' '.join(encoded_words)

print(encoded_sentence)
