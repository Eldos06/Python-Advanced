import asyncio
import aiofiles
import aiofiles.os
FILE_NAME = 'text.txt'

async def read_file():
  async with aiofiles.open(FILE_NAME, mode='w') as f:
    for i in range(1, 11):
      await f.write(f"line {i}\n")


async def read_lines_from_file():
  async with aiofiles.open(FILE_NAME, mode='r') as f:
    async for line in f:
      print(line.strip())

async def show_write_to_temp_file():
  async with aiofiles.tempfile.NamedTemporaryFile('w+') as f:
    await f.writelines([
      'foo\n',
      'bar\n',
      'baz\n',
      'qux\n',
    ])
    await f.seek(0)
    async for line in f:
      print(repr(line))
    print(f.name)

async def remove_file():
  await aiofiles.os.remove(FILE_NAME)

async def main():
  # await read_lines_from_file()
  # await show_write_to_temp_file()
  await remove_file()

if __name__ == '__main__':
  asyncio.run(main())