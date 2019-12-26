class Stack:
    def __init__(self):
        self.stack=[]
    def pop(self):
        if len(self.stack)==0:
            return "Empty Stack"
        top=len(self.stack)-1
        topElmt=self.stack[top]
        self.stack.remove(topElmt)
        return  topElmt
    def push(self,data):
        self.stack.append(data)
    def Length(self):
        return len(self.stack)
def operate(x,op,y):
    res=0
    if op=="+":
        res=int(y)+int(x)
    elif op=="-":
        res=int(x)-int(y)
    elif op=="*":
        res=int(y)*int(x)
    elif op=="/":
        res=int(x)//int(y)
    return res
prefix=input("Enter the prefix expression: ")
lst=prefix.split(" ")
aStack=Stack()
anotherStack=Stack()
for i in range(len(lst)):
    aStack.push(lst[len(lst)-1-i])
while(aStack.Length()>1):
    op=aStack.pop()
    x=aStack.pop()
    y=aStack.pop()
    res=0
    oper=["+","-","*","/"]
    if (x not in oper and y not in oper):
        res=operate(x,op,y)
        aStack.push(str(res))
        while(anotherStack.Length()>0):
            k=anotherStack.pop()
            if (k not in oper):
                op=anotherStack.pop()
                l=aStack.pop()
                res=operate(k,op,l)
                aStack.push(str(res))
            else:
                m=aStack.pop()
                n=aStack.pop()
                res=operate(m,k,n)
                aStack.push(str(res))                
                
    elif(x in oper):
        anotherStack.push(op)
        aStack.push(y)
        aStack.push(x)
    elif(y in oper):
        anotherStack.push(op)
        anotherStack.push(x)
        aStack.push(y)

print(aStack.pop())
