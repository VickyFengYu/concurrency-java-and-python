import threading
from threading import Semaphore

"""
sizelock
"""


class DiningPhilosophers:
    def __init__(self):
        self.sizelock = Semaphore(4)
        self.locks = [Semaphore(1) for _ in range(5)]

    def wantsToEat(self, index, *actions):
        left, right = index, (index - 1) % 5
        with self.sizelock:
            with self.locks[left], self.locks[right]:
                for action in actions:
                    action()


"""
"""


class DiningPhilosophers:
    def __init__(self):
        self.locks = [Semaphore(1) for _ in range(5)]

    def wantsToEat(self, index, *actions):
        left, right = index, (index - 1) % 5

        if index:
            with self.locks[left], self.locks[right]:
                for action in actions:
                    action()
        else:
            with self.locks[right], self.locks[left]:
                for action in actions:
                    action()


"""
Locks
"""


class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        first = philosopher
        second = philosopher + 1 if philosopher < 4 else 0

        if philosopher & 1:
            first, second = second, first

        with self.forks[first], self.forks[second]:
            pickLeftFork()
            pickRightFork()
            eat()
            putRightFork()
            putLeftFork()
