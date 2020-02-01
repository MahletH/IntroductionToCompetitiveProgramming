class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        ctr=0
        for i in range(len(A)-1):
            if A[i]>=A[i+1]:
                ctr+=A[i]-A[i+1]+1
                A[i+1]+=A[i]-A[i+1]+1
        return ctr
                
                
