class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size != self.capacity:
            self.size += 1
            self.arr[self.size - 1] = n
        else:
            self.resize()
            self.size += 1
            self.arr[self.size - 1] = n

    def popback(self) -> int:
        tmp = self.arr[self.size - 1]
        self.size -= 1
        return tmp

    def resize(self) -> None:
        self.arr += [0] * self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity