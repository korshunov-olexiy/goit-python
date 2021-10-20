from pathlib import Path

def get_credentials_users(path):
    lst = []
    with open(path, 'rb') as fr:
        while True:
            line = fr.readline().decode().strip()
            if line:
                lst.append(line)
            else:
                break
    return lst

p = Path.cwd().joinpath('raw_data.bin')

print(get_credentials_users(p))
