class Solution:
    def minSteps(self, n: int) -> int:
        lst=[True]*(n+1)
        lst[0],lst[1]=False,False
        m=int(math.sqrt(n))
        for i in range(2,m+1):
            if lst[i]:
                k=i*i
                while k<=n:
                    lst[k]=False
                    k+=i
        res=0
        for i in range(2,m+1):
            if lst[i]:
                while not n%i:
                    res+=i
                    n=n//i
        if(n!=1):
            res+=n
        return res
