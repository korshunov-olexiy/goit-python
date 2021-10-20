# Реализуйте функцию solve_riddle(riddle, word_length, start_letter, reverse=False)
# для нахождения искомого слова в строке ребуса.
def solve_riddle(riddle, word_length, start_letter, reverse=False):
    riddle = riddle[::-1] if reverse else riddle
    begin_idx = riddle.index(start_letter)
    return riddle[begin_idx:begin_idx+word_length]


r = 'mi1powerpret'
w_len = 5
s_letter = 'p'
rev = False

print(solve_riddle(r, w_len, s_letter, rev))
