"""Training with threads."""

import time
from threading import Thread


class Counter1(Thread):
    """Thread counting with 1s delay."""

    def start(self) -> None:
        super().start()
        print("Start counting: delay = 1s")

    def run(self) -> None:
        for i in range(10):
            print(f"Counter 1: {i}")
            time.sleep(1)


class Counter3(Thread):
    """Thread counting with 3s delay."""

    def start(self) -> None:
        super().start()
        print("Start counting: delay = 3s")

    def run(self) -> None:
        for i in range(3):
            print(f"Counter 3: {i}")
            time.sleep(3)


def main():
    counter1_thread = Counter1()
    counter3_thread = Counter3()
    print(f"{counter1_thread.is_alive() = }")

    # Start both threads: both code will run in parallel
    counter1_thread.start()
    counter3_thread.start()
    print(f"{counter1_thread.is_alive() = }")

    print("Main thread: sleeping")
    time.sleep(12)

    # Make sure each thread has finished, or wait until they are finished
    print("Main thread: waiting for all threads")
    counter1_thread.join()
    counter3_thread.join()
    print(f"{counter1_thread.is_alive() = }")


if __name__ == "__main__":
    main()
