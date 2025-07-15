from asyncio import run, sleep, create_task
import logging
from random import random, randint

logging.basicConfig(level=logging.INFO,
                    datefmt="%Y-%m-%d %H-%M-%S",
                    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
                    )

log = logging.getLogger(__name__)

###################################################################

# async def first():
#     await sleep(1.002)

# async def second():
#     await sleep(1.002)

# async def theard():
#     await sleep(1.002)

# async def fourth():
#     sleep(1.002)

# async def fiveth():
#     sleep(1.002)

# async def main():
#     log.info("Starting ... ")
#     tasks = {
#         create_task(

#         )
#     }
################################################################

import asyncio

# async def greet(name, delay):
#     log.info(f"Hello, {name}! (starting)")
#     await asyncio.sleep(delay)
#     log.info(f"Goodbye, {name}! (finished)")

# async def main():
#     # Create tasks without immediately awaiting them
#     task_alice = create_task(greet("Alice", 2))
#     task_bob = create_task(greet("Bob", 1))


#     log.info("Tasks created, continuing with main...")

#     # Await the tasks to ensure they complete
#     await task_alice
#     await task_bob

#     log.info("All tasks completed.")


##################################################################

import asyncio
from random import randint
import logging

log = logging.getLogger()
logging.basicConfig(level=logging.INFO, format="%(message)s")

products = [
    "Wireless Mouse",
    "Gaming Keyboard",
    "4K Monitor",
    "Bluetooth Speaker",
    "USB-C Hub",
    "External SSD",
    "Smartphone Stand",
    "LED Desk Lamp",
    "Noise-Canceling Headphones",
    "Portable Power Bank",
    "Smartwatch",
    "Laptop Cooling Pad",
    "Ergonomic Chair",
    "Mechanical Pencil",
    "Webcam HD",
    "Mini Projector",
    "Wireless Charger",
    "VR Headset",
    "Fitness Tracker",
    "Smart Thermostat"
]

finallyCheck = 0

async def task(product, price):
    global finallyCheck
    log.info(f"[TASK {product}] Checking a price...")
    await asyncio.sleep(1)
    log.info(f"[TASK {product}] cost {price}")
    finallyCheck += price
    return {"product": product, "price": price}





async def main():
    selected = products[:5]  # берем только 5 продуктов
    tasks = [asyncio.create_task(task(p, randint(10, 100))) for p in selected]
    results = await asyncio.gather(*tasks)
    log.info(f"\n📦 Результаты: {results}")
    log.info(f"💰 Общая сумма: {finallyCheck}")


# if __name__ == "__main__":
#     asyncio.run(main())

###################################################

# ⚠️ Some tasks should raise ValueError, catch and log which failed.
from asyncio import run, sleep, create_task
import logging
from random import random, randint

def randomSym():
    s = ["*", "/", "-", "+"]
    return s[randint(0, 3)]

def randomNum():
    return randint(1, 100)

async def TrainingBrain():
    FNum = randomNum()
    SNum = randomNum()
    symbol = randomSym()
    if FNum < SNum:
        FNum, SNum = SNum, FNum
    import asyncio
    loop = asyncio.get_running_loop()
    # Print the question before input
    print(f"{FNum} {symbol} {SNum} = ", end="")
    while True:
        user_input = await loop.run_in_executor(None, input, "Enter your answer: ")
        try:
            CheckNum = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    async def check():
        if SNum == 0:
            log.warning("Mustn't divide by Zero")
            raise ValueError("not zero %s", SNum)
        else:
            if symbol == "+":
                result = FNum + SNum
            elif symbol == "-":
                result = FNum - SNum
            elif symbol == "*":
                result = FNum * SNum
            elif symbol == "/":
                result = FNum / SNum
            else:
                log.warning("Unknown symbol")
                return "Unknown operation"

            if CheckNum == result:
                return "✅"
            else:
                return "Uncorrect ❌ try again"

    print(await check())



async def run_training_loop():
    while True:
        try:
            await TrainingBrain()
        except ValueError as e:
            log.warning(f"Task failed: {e}")

if __name__ == "__main__":
    run(run_training_loop())


###############################################################


# import asyncio

# async def main():
#     loop = asyncio.get_running_loop()
#     print("Got running loop:", loop)

# asyncio.run(main())
################################################################

# import asyncio

# async def main():
#     loop = asyncio.get_running_loop()
#     print("Running loop:", loop)

################################################################

# loop = asyncio.get_running_loop()  # ❌ This will raise RuntimeError

################################################################

# loop = asyncio.get_event_loop()
# print("Event loop outside coroutine:", loop)

# import asyncio

# # Create new loop
# new_loop = asyncio.new_event_loop()
# print("New loop created:", new_loop)

# # Set it as the current loop
# asyncio.set_event_loop(new_loop)

# # Now get it
# current_loop = asyncio.get_event_loop()
# print("Current loop is now:", current_loop)


################################################################



