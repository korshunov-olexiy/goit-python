from pathlib import Path

p = Path.cwd().joinpath('sotr.txt')


def add_employee_to_file(record, path):
    fn = open(path, 'a')
    fn.write(f'{record}\n')
    fn.close()


add_employee_to_file("Drake Mikelsson, 191", p)
