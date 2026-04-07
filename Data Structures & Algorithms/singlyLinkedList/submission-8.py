class LinkedList:

    class Node:
        def __init__(self, value, next_node):
            self.value = value
            self.next_node = next_node
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if self.head == None: 
            return -1
        cur_node = self.head
        while index > 0:
            if cur_node == None:
                return -1
            cur_node = cur_node.next_node
            index -= 1
        if cur_node == None:
            return -1
        return cur_node.value
        

    def insertHead(self, val: int) -> None:
        self.head = self.Node(val, self.head)

    def insertTail(self, val: int) -> None:
        if self.head == None: 
            self.head = self.Node(val, None)
            return
        cur_node = self.head
        while cur_node.next_node: 
            cur_node = cur_node.next_node
        cur_node.next_node = self.Node(val, None)

    def remove(self, index: int) -> bool:
        if self.head == None: return False
        cur_node = self.head
        prev_node = None
        for i in range(index): 
            print(i, self.getValues())
            if cur_node == None:
                print("returning now")
                return False
            prev_node = cur_node
            cur_node = cur_node.next_node
        if prev_node == None: 
            self.head = self.head.next_node
        else:
            if cur_node == None: 
                return False
            prev_node.next_node = cur_node.next_node
        
        return True

    def getValues(self) -> List[int]:
        out = []
        cur_node = self.head
        while cur_node: 
            out.append(cur_node.value)
            cur_node = cur_node.next_node
        return out
        
