from pathlib import Path


def write_employees_to_file(employee_list, path):
    fn = open(path, 'w')
    for sublst in employee_list:
        for item in sublst:
            fn.write(f'{item}\n')
    fn.close()


p = Path.cwd().joinpath('sotr.txt')
write_employees_to_file(
    [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19'], ['Robert Stivenson,128', 'Alex Denver,35']], p)
