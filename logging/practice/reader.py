import logging
from common import configure_logging

# f = open("file.txt")
# print(f.read())

logger = logging.getLogger(__name__)


def count_lines_for_loop(filepath):
    configure_logging(level=logging.INFO)
#"""Counts the number of lines in a file using a for loop."""
    try:
        line_count = 0
        with open(filepath, 'r') as file:
            for _ in file:  # Iterate through each line
                line_count += 1
        logger.info(f"lines are {line_count}")
    except:
        raise FileNotFoundError("File doesn't exist")
    

count_lines_for_loop("file.txt")
# Example usage:
# num_lines = count_lines_for_loop("my_file.txt")
# print(f"Number of lines: {num_lines}")



# with open("file.txt") as f:
#   print(f.readline())
#   print(f.readline())


