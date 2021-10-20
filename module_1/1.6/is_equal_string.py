from pathlib import Path

def is_equal_string(utf8_string, utf16_string):
    utf8_string = utf8_string.decode('utf-8').casefold()
    utf16_string = utf16_string.decode('utf-16').casefold()
    return utf8_string == utf16_string


s = "Привет!"
s1 = "Привет"
print(is_equal_string(s.encode('utf-8'), s1.encode('utf-16')))
