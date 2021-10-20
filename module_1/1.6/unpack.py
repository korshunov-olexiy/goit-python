import shutil
import zipfile

# zipfile.ZipFile
def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)

p = r"/home/user1/1. COURSES/goit/ДЗ/Tech Skills/1/1.6/backup_folder.zip"
p1 = r"/home/user1/1. COURSES/goit/ДЗ/Tech Skills/1/1.6/unpack"
unpack(p, p1)
