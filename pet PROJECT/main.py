# ⚠️ Some tasks should raise ValueError, catch and log which failed.
from asyncio import log, run, sleep, create_task
import asyncio
import logging
from random import randint

logging.basicConfig(level=logging.INFO,
                    datefmt="%Y-%m-%d %H-%M-%S",
                    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
                    )

log = logging.getLogger(__name__)

def randomSym():
    s = ["*", "/", "-", "+"]
    return s[randint(0, 3)]

def randomNum():
    return randint(1, 100)

async def TrainingBrain(): #ff0000 This function simulates a training brain that asks a math question
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
        user_input = await loop.run_in_executor(None, input, "Enter your answer: ") # This line waits for user input asynchronously
        try:
            CheckNum = int(user_input) # This line converts the user input to an integer
            break # If the conversion is successful, exit the loop
        except ValueError: # If the conversion fails, print an error message and continue the loop
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



# async def run_training_loop():

#     log.info("Starting a new training session...")
#     try:
#         await TrainingBrain()
#     except ValueError as e:
#         log.warning(f"Task failed: {e}")

# if __name__ == "__main__":
#     run(run_training_loop())

#############################################################################
#🎯 Return only the successful results (filter out the tasks with exceptions).

def filter_successful_tasks(results):
    """
    Filters out exceptions from the results and returns a list of results from successful tasks.

    Args:
        results (list): List containing results and exceptions from asyncio tasks.

    Returns:
        list: List of results from successful tasks (exceptions are excluded).
    """
    successful_tasks = []
    for result in results:
        if not isinstance(result, Exception):
            successful_tasks.append(result)
    return successful_tasks

# Example usage:
async def first_training_session():
    log.info("Starting first training session...")
    await sleep(2.001)
    log.info("First training session completed.")
    return 10  # Changed to a valid return value


async def second_training_session():
    log.info("Starting second training session...")
    await sleep(2.000)
    log.info("Second training session completed.")
    return 42


async def main():

    async with asyncio.TaskGroup() as tg:
        one = tg.create_task(first_training_session())
        two = tg.create_task(second_training_session())

    results = [one.result(), two.result()]
    successful_results = filter_successful_tasks(results)
    log.info(f"Successful Results: {successful_results}")

#Example usage of the main function
if __name__ == "__main__":
    asyncio.run(main())


