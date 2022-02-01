import asyncio
from operator import not_
from aiopath import AsyncPath, AsyncPosixPath, AsyncWindowsPath
from typing import List, Type
# from pathlib import Path, PosixPath, WindowsPath


async def del_empty_dirs(path: Type[AsyncPath], sort_dirs: List[str]):
    async for f in path.rglob('*'):
        is_dir = await f.is_dir()
        empty_dir = not [i async for i in f.iterdir()]
        not_sort_dirs = not f.name in sort_dirs
        print(f, is_dir, empty_dir, not_sort_dirs)
        if is_dir and not_sort_dirs:
            if empty_dir:
                await f.rmdir()
            else:
                return await del_empty_dirs(f, sort_dirs)
        print("exit func")
        return None

async def del_empty_folder(path: Type[AsyncPath], sort_dirs: List[str], root_dir: bool = True):
    if root_dir:
        dirs = [f async for f in path.iterdir() if f.name not in sort_dirs and await f.is_dir()]
    else:
        dirs =  [f async for f in path.rglob("*") if f.name not in sort_dirs and await f.is_dir()]
    for dir in dirs:
        if not [d async for d in dir.iterdir()]:
            await dir.rmdir()
        else:
            try:
                await del_empty_folder(dir, sort_dirs, root_dir=False)
            except FileNotFoundError:
                await del_empty_folder(path, sort_dirs)
    return None


if __name__ == "__main__":
    _dir = AsyncPath("d:\\MOBILE\\test\\")
    sort_dirs = ["pictures","documents","music","movies","archives","unknown"]
    asyncio.run(del_empty_folder(_dir, sort_dirs))
