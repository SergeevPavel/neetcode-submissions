import sys

class MinStack:

    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, value: int) -> None:
        oldMin = sys.maxsize
        if self.mins:
            oldMin = self.getMin()
        newMin = min(oldMin, value)
        self.data.append(value)
        self.mins.append(newMin)

    def pop(self) -> None:
        self.data.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]