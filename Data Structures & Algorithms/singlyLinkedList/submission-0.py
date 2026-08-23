class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt
class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.nxt
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.nxt
        return -1

    def insertHead(self, val: int) -> None:
        new = ListNode(val)
        new.nxt = self.head.nxt
        self.head.nxt = new
        if not new.nxt:
            self.tail = new

    def insertTail(self, val: int) -> None:
        self.tail.nxt = ListNode(val)
        self.tail = self.tail.nxt

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.nxt
        if curr and curr.nxt:
            if curr.nxt == self.tail:
                self.tail = curr
            curr.nxt = curr.nxt.nxt
            return True
        return False


    def getValues(self) -> List[int]:
        curr = self.head.nxt
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.nxt
        return res
