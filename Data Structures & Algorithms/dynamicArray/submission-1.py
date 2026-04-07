class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None for _ in range(capacity)]
        self.end_of_arr = 0

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.end_of_arr == self.capacity:
            self.resize()
        self.arr[self.end_of_arr] = n
        self.end_of_arr += 1

    def popback(self) -> int:
        ret = self.arr[self.end_of_arr-1]
        self.arr[self.end_of_arr-1] = None
        self.end_of_arr -= 1
        return ret

    def resize(self) -> None:
        extension = [None for _ in range(self.capacity)]
        self.capacity = 2 * self.capacity
        self.arr.extend(extension)

    def getSize(self) -> int:
        return self.end_of_arr
        
    def getCapacity(self) -> int:
        return self.capacity