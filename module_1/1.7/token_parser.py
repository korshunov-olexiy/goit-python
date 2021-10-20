# лексемами являются: операторы ( *, /, -, + ), числа и скобки
# числа могут быть только целыми

def token_parser(s):
    ss = list(s.replace(' ', ''))
    res = []
    for s in ss:
        if len(res) == 0:
            res = [s]
        else:
            if res[-1].isdigit() and s.isdigit():
                res[-1] += s
            else:
                res.append(s)
    return res


formula = "(2+ 3) *4 - 53 * 3"
print(token_parser(formula))
