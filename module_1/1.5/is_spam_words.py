def is_spam_words(text, spam_words, space_around=False):
    text = text.split()
    for t in text:
        for spam in spam_words:
            if space_around:
                if spam == t:
                    return True
            else:
                if spam in t:
                    return True
    return False


print(is_spam_words('Молох', ['лох']))

# d = {ord('s'): "o"}
text = "see   you   sun "
my_table = text.maketrans("nus", "to1", "y ")
print(text.translate(my_table))
