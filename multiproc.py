from multiprocessing import Process
from time import time, sleep

def print_test() -> None:
    print("start")
    sleep(1)
    print("stop")
    sleep(1)

procs = []

def main() -> None:
    for _ in range(10):
        proc = Process(target=print_test)
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    print("done")

if __name__ == "__main__":
    start_time = time()
    main()
    end_time = time()
    print(f"Process time : {round(end_time-start_time, 2)}ms")
