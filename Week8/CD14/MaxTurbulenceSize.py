class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        start,element=True,1
        up,down=False,False
        max_=1
        i=0
        while i<len(A)-1:
            if start:
                if A[i]<A[i+1]:
                    down=True
                elif A[i]>A[i+1]:
                    up=True
                else:
                    i+=1
                    continue
                start=False
                element+=1
            else:
                if up and A[i]<A[i+1]:
                    down,up=True,False
                    element+=1
                elif down and A[i]>A[i+1]:
                    up,down=True,False
                    element+=1
                else:
                    i-=1
                    start=True
                    up,down=False,False
                    element=1
            max_=max(max_,element)
            i+=1
        return max_
