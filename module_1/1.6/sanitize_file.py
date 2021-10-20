from pathlib import Path
import re

p_in = Path.cwd().joinpath('in_with_digits.txt')
p_out = Path.cwd().joinpath('out_with_digits.txt')


def sanitize_file(source, output):
    res = ''
    rx = re.compile(r'[\d]')
    with open(source, 'r') as fr:
        lines_in = fr.read().splitlines()
    for ln in lines_in:
        res += rx.sub('', ln)+'\n'
    res = res.rstrip()
    with open(output, 'w') as fw:
        fw.write(res)


print(sanitize_file(p_in, p_out))
