from pathlib import Path
import shutil

def create_backup(path, file_name, employee_residence):
    full_path = Path(path).joinpath(file_name)
    with open(full_path, 'wb') as fw:
        for key,val in employee_residence.items():
            fw.write(bytes(f"{key} {val}\n".encode()))
    zip_archive = shutil.make_archive('backup_folder', 'zip', path)
    return zip_archive

p = str(Path.cwd())
f = str(Path.cwd().joinpath('out_data.bin'))
users_data = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
print(create_backup(p, f, users_data))
