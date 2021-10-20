# БОЛЬШАЯ:
# 1-я буква в строке;
# после точки, после !, после ?

def capital_text(s):
    ss, flg = list(s), True
    for idx, s in enumerate(ss):
        if flg and s != ' ':
            ss[idx] = ss[idx].upper()
            flg = False
        if s in '.?!':
            idx += 1
            while idx < len(ss):
                if ss[idx] == ' ':
                    idx += 1
                else:
                    ss[idx] = ss[idx].upper()
                    break
    return ''.join(ss)


in_str = "  hello friends.    who are you?   are you fine!       are you? "

print(f"|{capital_text(in_str)}|")
