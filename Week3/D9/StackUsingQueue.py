class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        print((self.stack))

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        front=0
        end=len(self.stack)-1
        lst=[]
        while(end>0):
            elmt=self.stack[front]
            self.stack.remove(elmt)
            end-=1
            lst.append(elmt)
        elmt=self.stack[front]
        self.stack.remove(elmt)
        self.stack=[]
        for i in lst:
            self.stack.append(i)
        lst=[]
        return elmt

    def top(self) -> int:
        """
        Get the top element.
        """
        front=0
        end=len(self.stack)-1
        lst1=[]
        while(end>0):
            elmt=self.stack[front]
            self.stack.remove(elmt)
            end-=1
            lst1.append(elmt)
        elmt=self.stack[front]
        self.stack.remove(elmt)
        lst1.append(elmt)
        for i in lst1:
            self.stack.append(i)
            
        return elmt

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if(len(self.stack)==0):
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
