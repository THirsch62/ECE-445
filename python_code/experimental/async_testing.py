import time
import random
from threading import Thread

def call(iter):
    time.sleep(random.randint(0, 5))
    print(iter)
    time.sleep(1)

def main():
    threads = []
    for x in range(10):
        thread = Thread(target=call, args=[x])
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print("done running main")

if __name__ == "__main__":
    main()