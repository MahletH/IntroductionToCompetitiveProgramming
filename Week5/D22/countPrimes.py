class Solution:
    def countPrimes(self, n: int) -> int:
        if(n==0 or n==1):
            return 0
        prime=[True]*n
        prime[0]=False;
        prime[1]=False;
        m=int(math.sqrt(n));
        for i in range(2,m+1):
            if prime[i]:
                k=i*i
                while(k<n):
                    prime[k]=False
                    k+=i
        ctr=0
        for i in prime:
            if(i):
                ctr+=1
        return ctr
