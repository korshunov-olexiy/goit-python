from pathlib import Path

def save_credentials_users(path, users_info):
    with open(path, 'wb') as fw:
        for key,val in users_info.items():
            fw.write(bytes(f"{key}:{val}\n".encode()))

p = Path.cwd().joinpath('raw_data.bin')
users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
save_credentials_users(p, users_info)
