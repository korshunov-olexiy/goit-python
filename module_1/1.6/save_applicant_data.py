from pathlib import Path

vedomost_lst = [
    {"name": "Kovalchuk Oleksiy", "specialty": 301, "math": 175, "lang": 180, "eng": 155,},
    {"name": "Ivanchuk Boryslav", "specialty": 101, "math": 135, "lang": 150, "eng": 165,},
    {"name": "Karpenko Dmitro", "specialty": 201, "math": 155, "lang": 175, "eng": 185,},
]

def save_applicant_data(source, output):
    with open(output, 'w') as fw:
        for v in source:
            fw.write(f"{','.join([str(val) for val in v.values()])}\n")

p = Path.cwd().joinpath('vedomost.txt')

save_applicant_data(vedomost_lst, p)
