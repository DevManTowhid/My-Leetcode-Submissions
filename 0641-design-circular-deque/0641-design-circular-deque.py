class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.deque = [0] * k
        self.head = -1
        self.tail = -1
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = 0
        else:
            # Move head backward circularly
            self.head = (self.head - 1) % self.capacity
        self.deque[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = 0
        else:
            # Move tail forward circularly
            self.tail = (self.tail + 1) % self.capacity
        self.deque[self.tail] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail: # Only one element
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail: # Only one element
            self.head = self.tail = -1
        else:
            self.tail = (self.tail - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.head]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity