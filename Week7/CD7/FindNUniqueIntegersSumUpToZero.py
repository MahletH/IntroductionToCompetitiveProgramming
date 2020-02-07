class Solution:
    def sumZero(self, n: int) -> List[int]:
        if(n==1):
            return [0]
        neg=(n+1)//2
        lst1=[]
        lst2=[]
        for i in range(1,neg+1):
            lst1.append(0-i)
            lst2.append(i)
        if(n%2==0):
            return lst1+lst2
        lst2.pop()
        lst2[-1]=abs(lst1[-1]+lst1[-2])
        return lst1+lst2
