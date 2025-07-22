import asyncio
import aiofiles
import aiofiles.os
from common import log


fileName = 'EvenNum.txt'

async def writeFile():
  async with aiofiles.open(fileName, mode='w') as f:
    for i in range(1, 11):
      await f.write(f"Line {i}\n")

async def evenNum():
  async with aiofiles.open(fileName, mode='w') as f:
    for i in range(2, 21, 2):
      await f.write(f"{i}\n")

async def writeNewLines(someList: list):
  async with aiofiles.open(fileName, mode='a') as f:
    for i in someList:
      await f.write(f"{i}\n")


async def readFile():
  async with aiofiles.open(fileName, mode='r') as f:
    # log.info(f)
    async for line in f:
      log.info(line.strip())

async def readFileReverse():
  async with aiofiles.open(fileName, mode='r') as f:
    # log.info(f)
    lines = await f.read()
    for line in reversed(lines.splitlines()):
      log.info(line.strip())


async def readLines():
  count = 0
  async with aiofiles.open(fileName, mode='r') as f:
    async for line in f:
      count += 1
    log.info(f"Total lines: {count}")





async def tempFile():
  async with aiofiles.tempfile.NamedTemporaryFile("w+") as f:
    await f.writelines([
      'foo\n',
      'bar\n',
      'baz\n',
      'qux\n',
    ])
    await f.seek(0)
    async for line in f:
      log.info(repr(line))

myList =  ["Alice", "Bob", "Charlie"]

async def main():
  # await writeFile()

  # await tempFile()
  # await writeNewLines(myList)

  # print()
  # await readFileReverse()
  # await evenNum()
  # # await readLines()
  # await readFile()
  pass


import aiofiles
import asyncio

async def async_copy_file_line_by_line(source_file, destination_file):
    try:
        async with aiofiles.open(source_file, mode='r') as src, aiofiles.open(destination_file, mode='w') as dst:
            async for line in src:
                await dst.write(line)
            await src.delete()
        print(f"✅ Файл '{source_file}' успешно скопирован в '{destination_file}' построчно.")
    except FileNotFoundError:
        print(f"❌ Ошибка: файл '{source_file}' не найден.")
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

# Пример вызова
if __name__ == '__main__':
    asyncio.run(async_copy_file_line_by_line('text.txt', 'copy_text.txt'))


# if __name__ == '__main__':
#   logging.info("Starting the asynchronous file operations")
#   asyncio.run(main())
#   logging.info("Finished the asynchronous file operations")

