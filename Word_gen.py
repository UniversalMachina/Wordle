import nltk

nltk.download("words")

from nltk.corpus import words

word_list = words.words()
five_letter_words = [word.lower() for word in word_list if len(word) == 5]

with open("wordlist.txt", "w") as file:
    for word in five_letter_words:
        file.write(f"{word}\n")