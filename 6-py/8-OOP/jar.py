class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = capacity

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new):
        self._capacity = new

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new):
        if new > self.capacity:
            raise ValueError("Exceeded maximum capacity!")
        elif new < 0:
            raise ValueError("Not enought in the jar!")
        else:
            self._size = new