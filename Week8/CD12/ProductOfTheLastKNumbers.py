class ProductOfNumbers:

    def __init__(self):
        self.lst=[]
        self.max_=-1
    def add(self, num: int) -> None:
        if not len(self.lst):
            self.lst.append(num)
        else:
            prev=self.lst[-1]
            if prev:
                self.lst.append(prev*num)
            else:
                self.max_=len(self.lst)
                self.lst.append(num)
                
    def getProduct(self, k: int) -> int: 
        l=len(self.lst)
        if l-k<self.max_:
            return 0
        elif l-k==self.max_:
            return self.lst[-1]
        if l==k:
            return self.lst[-1]
        prev=self.lst[l-k-1]
        return self.lst[l-1]//prev


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
