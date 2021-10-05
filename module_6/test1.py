from uuid import uuid1
from pathlib import Path
_dir = Path(r"/home/user1/1. COURSES/goit_github/1.test_/1.test (копия).txt")
#_dir.joinpath(r"/home/user1/1. COURSES/goit_github/")
_dir.replace(_dir.joinpath(r"/home/user1/1. COURSES/goit_github/", str(uuid1())+'.txt'))
