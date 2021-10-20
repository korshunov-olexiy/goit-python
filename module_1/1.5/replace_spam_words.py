import re


def replace_spam_words(text, spam_words):
    for spam in spam_words:
        text = re.sub(spam, '*'*len(spam), text, flags=re.IGNORECASE)
    return text


print(replace_spam_words(
    'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn', ['began', 'Python']))
