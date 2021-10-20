import re


def find_all_links(text):
    result = []
    # iterator = re.finditer(r"(http|https)://w{,3}.{,1}[\w.]+", text)
    iterator = re.finditer(r"(http|https)://w{,3}\.{,1}[^.]{1,}\.\w{3}", text)
    for match in iterator:
        result.append(match.group())
    # result = [r for r in result if r.find('..') == -1]
    return result


print(find_all_links('The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com'))
