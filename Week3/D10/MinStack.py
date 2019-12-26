class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min=0
    def push(self, x: int) -> None:
        if(len(self.stack)==0):
            self.min=x
        else:
            if(self.min>x):
                self.min=x
        self.stack.append(x)
    def pop(self) -> None:
        elmt=self.stack[len(self.stack)-1]
        self.stack=self.stack[:len(self.stack)-1]
        if(elmt==self.min and len(self.stack)):
            nextMin=self.stack[0]
            for i in self.stack:
                if(i<=nextMin):
                    nextMin=i
            self.min=nextMin
        return elmt

    def top(self) -> int:
        
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        if(len(self.stack)==0):
            return "empty stack"
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
