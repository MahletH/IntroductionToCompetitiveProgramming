class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        lst=[]
        l=len(self.queue)
        for i in range(l-1):
            lst.append(self.queue.pop())
        elt=self.queue.pop()
        for i in range(l-1):
            self.queue.append(lst.pop())
            
        return elt

    def peek(self) -> int:
        """
        Get the front element.
        """
        lst=[]
        l=len(self.queue)
        for i in range(l-1):
            lst.append(self.queue.pop())
        elt=self.queue.pop()
        lst.append(elt)
        for i in range(l):
            self.queue.append(lst.pop())
            
        return elt

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if(len(self.queue)==0):
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
