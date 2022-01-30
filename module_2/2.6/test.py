import asyncio
import concurrent.futures
from pathlib import Path, PosixPath, WindowsPath
from random import randint
from typing import Type

import aiofiles
import aiofiles.os
import aiofiles.ospath


def get_files(path: Type[Path]):
    return [f for f in path.rglob('*') if f.is_file()]

async def run_blocking_tasks(executor, func, *args):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, func, *args)
    return result



async def main():
    _dir = Path("d:\\MOBILE\\test\\")
    _dir_docs = _dir.joinpath("documents")
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    path_files = await run_blocking_tasks(executor, get_files, _dir)
    try:
        await aiofiles.os.mkdir(_dir_docs)
    except FileExistsError:
        print(f"Dir: \"{_dir_docs}\" is exists. Skiped...")
    for path_file_name in path_files:
        new_file_name = _dir_docs.joinpath(path_file_name.name)
        file_exists = await aiofiles.ospath.exists(new_file_name)
        if file_exists:
            rnd = randint(1, 1000000)
            new_file_name = _dir_docs.joinpath(f"{path_file_name.stem}_{rnd}{path_file_name.suffix}")
        try:
            await aiofiles.os.replace(path_file_name, new_file_name)
        except (FileExistsError, OSError) as os_err:
            print(f"An error occurred: {os_err}")

if __name__ == "__main__":
    _dir = Path("d:\\MOBILE\\test\\")
    asyncio.run(main())
