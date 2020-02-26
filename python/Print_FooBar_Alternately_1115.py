"""
Use two Semaphores just as we used two locks. The foo_gate semaphore starts with a value of 1 because we want foo to print first.
"""
from threading import Lock
from threading import Semaphore


class FooBar_1:
    def __init__(self, n):
        self.n = n
        self.foo_gate = Semaphore(1)
        self.bar_gate = Semaphore(0)

    def foo(self, printFoo):
        for i in range(self.n):
            self.foo_gate.acquire()
            printFoo()
            self.bar_gate.release()

    def bar(self, printBar):
        for i in range(self.n):
            self.bar_gate.acquire()
            printBar()
            self.foo_gate.release()


"""
Use two locks for the threads to signal to each other when the other should run. bar_lock starts in a locked state because we always want foo to print first.
"""


class FooBar_2:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo):
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

        def bar(self, printBar):

            for i in range(self.n):
                self.bar_lock.acquire()
                printBar()
                self.foo_lock.release()
