import threading
import time

'''
Python programs run sequentially by default.

Threads allow your program to do multiple tasks at once, like downloading a file while showing a loading animation.

Threads share memory and variables with the main thread.
'''

def task1():
    print("Start Task 1")
    time.sleep(3)
    print("End Task 1")

def task2():
    print("Start Task 2")
    time.sleep(2)
    print("End Task 2")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

'''
What is Blocking?
A blocking operation is one that stops the execution of further code until it finishes.

Example: time.sleep(), input(), or file/network I/O operations.

So without threading, when a blocking task runs, the whole program waits.
With threading, other tasks can keep running even while waiting.

| Term        | Meaning                                                  |
| ----------- | -------------------------------------------------------- |
| Thread      | A lightweight, parallel unit of execution                |
| Blocking    | A delay that halts further code until the task completes |
| `threading` | Python module to use threads                             |
| GIL         | Prevents true parallelism for CPU-bound threads          |

'''