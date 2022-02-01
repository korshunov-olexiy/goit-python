import asyncio
from aiopath import AsyncPath
# from pathlib import Path


async def main():
    categories = ["pictures", "movies", "documents", "music", "archives", "video", "unknown"]
    _dir = AsyncPath("D:\\__test__\\test\\")
    _dir_parts = _dir.parts
    glob = _dir.rglob("*")
    folders = []
    async for obj in glob:
        is_dir = await obj.is_dir()
        same_level = len(obj.parts) == len(_dir_parts)
        not_in_categories = obj.name not in categories
        if is_dir and (same_level or not_in_categories):
            folders.append(obj)
    folders = sorted(folders, key=lambda f: len(f.parts), reverse=True)
    for folder in folders:
        is_empty = not [f async for f in folder.iterdir()]
        if is_empty:
            await folder.rmdir()


if __name__ == "__main__":
    asyncio.run(main())
