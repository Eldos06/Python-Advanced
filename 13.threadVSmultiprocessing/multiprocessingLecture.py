import logging
import multiprocessing
import os

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


# def main():
#     log.info("start main")
#     timeouts = [timeout + i for i in range(100, 1000, 250)]
#     with multiprocessing.Pool() as pool:
#         pool.map(countdown, timeouts)
#
#     log.info("end main")



# if __name__ == '__main__':
#     log.info("start main")
#     process1 = multiprocessing.Process(
#         target=countdown,
#         args=(timeout,),
#     )
#     process2 = multiprocessing.Process(
#         target=countdown,
#         args=(timeout,),
#     )
#     process3 = multiprocessing.Process(
#         target=countdown,
#         args=(timeout,),
#     )
#     process4 = multiprocessing.Process(
#         target=countdown,
#         args=(timeout,),
#     )
#     log.info("created processes, starting")
#     procs = [process1, process2, process3, process4]
#     for p in procs:
#         p.start()
#     log.info("created processes, joining")
#     for p in procs:
#         p.join()
#     log.info("end main")


def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def main_fac():
    log.info("start main")
    nums = [10, 42, 57]
    with multiprocessing.Pool() as pool:
        factorials = pool.map(fac, nums)
    log.info("factorial %s: ", factorials)
    log.info("end main")

def show_info(caller):
    log.info("info for %s", caller)
    log.info("[%s] where am I %s", caller, __name__)
    log.info("[%s] my process id (PID) %s", caller, os.getpid())
    log.info("[%s] parent process id: (PID) %s", caller, os.getppid())



def cpu_expensive(extra_arg):
    log.info("run in func, arg = %s", extra_arg)
    show_info("cpu expensive task")



def main():
    log.info("start main")
    show_info("main")

    process = multiprocessing.Process(
        target=cpu_expensive,
        args=("hello",),
        name="qwerty",
    )
    process.start()
    process.join()

    log.info("child exit code: %s", process.exitcode)
    log.info("done main")

if __name__ == '__main__':
    main()