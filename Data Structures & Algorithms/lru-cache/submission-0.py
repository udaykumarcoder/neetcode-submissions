class ListNode:
    def __init__(self,prev,next,val,key):
        self.prev=prev
        self.next=next
        self.val=val
        self.key=key

class LRUCache:

    def __init__(self, capacity: int):
        self.left=ListNode(None,None,0,0)
        self.right=ListNode(self.left,None,0,0)
        self.left.next=self.right
        self.capacity=capacity
        self.d={}

    def insert(self,ListNode):
        self.right.prev.next=ListNode
        ListNode.prev=self.right.prev
        ListNode.next=self.right
        self.right.prev=ListNode
        
    def remove(self, ListNode):
        ListNode.prev.next = ListNode.next
        ListNode.next.prev = ListNode.prev

    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            self.insert(self.d[key])
            return self.d[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        self.d[key]=ListNode(None,None,value,key)
        self.insert(self.d[key])
        if len(self.d)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.d[lru.key]


