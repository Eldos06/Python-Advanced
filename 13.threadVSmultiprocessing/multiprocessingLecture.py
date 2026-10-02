import logging
import multiprocessing


logging.basicConfig(
  level = logging.INFO,
  datefmt="%H:%M:%S",
  format="[%(asctime)s.%(msecs)03d] %(lineno)3d %(funcName)15s %(levelname)-8s = %(message)s",
)
timeout = 64_000_000
log = logging.getLogger(__name__)

def countdown(n):
    log.info("countdown to %s", n)
    while n:
        n -= 1
    log.info("countdown done")

def main():
    countdown(timeout)



if __name__ == '__main__':
    log.info("start main")
    process = multiprocessing.Process(
        target=countdown,
        args=(timeout,),
    )
    log.info("created process, starting")
    process.start()
    log.info("created process, joining")
    process.join()
    log.info("end main")


