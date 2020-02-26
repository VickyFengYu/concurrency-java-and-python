# -*- coding: utf-8 -*-
"""
"""

from threading import Lock
from threading import Lock
from threading import Semaphore


class Foo_1:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        with self.firstJobDone:
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # Wait for the second job to be done.
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()


"""
Start with two closed gates represented by 0-value semaphores. 
Second and third thread are waiting behind these gates.
When the first thread prints, it opens the gate for the second thread.
When the second thread prints, it opens the gate for the third thread.
"""


class Foo_2:
    def __init__(self):
        self.gates = (Semaphore(0), Semaphore(0))

    def first(self, printFirst):
        printFirst()
        self.gates[0].release()

    def second(self, printSecond):
        with self.gates[0]:
            printSecond()
            self.gates[1].release()

    def third(self, printThird):
        with self.gates[1]:
            printThird()


"""
Start with two locked locks. First thread unlocks the first lock that the second thread is waiting on. 
Second thread unlocks the second lock that the third thread is waiting on.
"""


class Foo_3:
    def __init__(self):
        self.locks = (Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst):
        printFirst()
        self.locks[0].release()

    def second(self, printSecond):
        with self.locks[0]:
            printSecond()
            self.locks[1].release()

    def third(self, printThird):
        with self.locks[1]:
            printThird()
