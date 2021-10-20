def standard_input():
    yield 'to_indexed_start.txt'
    yield 'to_indexed_end.txt'


def to_indexed(start_file, end_file):
    with open(start_file, 'r') as fr:
        res = fr.readlines()
    with open(end_file, 'w') as fw:
        for idx in range(len(res)):
            fw.write(f"{idx}: {res[idx]}")


print(to_indexed(input(), input()))
