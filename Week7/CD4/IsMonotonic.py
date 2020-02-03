class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc,dec=0,0
        for i in range(len(A)-1):
            if(A[i]==A[i+1]):
                continue
            else:
                diff=A[i]-A[i+1]
                if(not inc and not dec):
                    if(diff>0):
                        inc=1
                    else:
                        dec=1
                elif(inc):
                    if(diff<0):
                        return False
                elif(dec):
                    if(diff>0):
                        return False
        return True
                    
