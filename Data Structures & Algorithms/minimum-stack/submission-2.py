class MinStack:

    def __init__(self):
        self.arr = []
        self.min_item = None

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.min_item = min(self.arr)

    def pop(self) -> None:
        ret = self.arr.pop()
        if self.arr == []:
            self.min_item = None
        else: 
            self.min_item = min(self.arr)
        return ret

    def top(self) -> int:
        return self.arr[-1]
        
    def getMin(self) -> int:
        return self.min_item
