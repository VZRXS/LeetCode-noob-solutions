#!/usr/bin/env python3


class MyCircularQueue:
    # 622. Design Circular Queue
    def __init__(self, k: int):
        # self.queue=[None for _ in range(k)]
        self.queue = []
        for _ in range(k):
            self.queue.append(None)
        self.head = 0
        self.tail = 0
        self.full = False
        self.empty = True

    def enQueue(self, value: int) -> bool:
        if self.full:
            return False
        elif self.empty:
            self.queue[self.tail] = value
            self.empty = False
            if len(self.queue) == 1:
                self.full = True
            return True

        if self.tail == len(self.queue) - 1:
            self.tail = 0
        else:
            self.tail += 1
        self.queue[self.tail] = value

        if (self.head == 0 and self.tail == len(self.queue) - 1) or self.tail == self.head - 1:
            self.full = True
        return True

    def deQueue(self) -> bool:
        if self.empty:
            return False
        elif self.full:
            if len(self.queue) == 1:
                self.empty = True
            self.full = False

        self.queue[self.head] = None
        if self.head == self.tail:
            self.empty = True
        elif self.head == len(self.queue) - 1:
            self.head = 0
        else:
            self.head += 1
        return True

    def Front(self) -> int:
        if self.empty:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.empty:
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.empty

    def isFull(self) -> bool:
        return self.full


class MyCircularQueue_attempt2:
    # Faster than the above one
    # Let list[0] always be null
    def __init__(self, k: int):
        # self.queue=[None for _ in range(k)]
        self.queue = []
        for _ in range(k + 1):
            self.queue.append(None)
        self.head = 0
        self.tail = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head += 1

        if self.tail < self.k:
            self.tail += 1
        else:
            self.tail = 1

        self.queue[self.tail] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.head] = None

        if self.head < self.k:
            self.head += 1
        else:
            self.head = 1

        if self.queue[self.tail] is None:
            self.head = 0
            self.tail = 0

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.head == 0 and self.tail == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.head > 0:
            if self.tail - self.head == self.k - 1 or self.head - self.tail == 1:
                return True
        return False


if __name__ == '__main__':
    obj = MyCircularQueue_attempt2(k=1)
    print(obj.enQueue(value=1))
    print(obj.enQueue(value=2))
