import re


def find_all_words(text, word):
    return re.findall(word, text, flags=re.IGNORECASE)


print(find_all_words("This is PyThOn world!", 'python'))
