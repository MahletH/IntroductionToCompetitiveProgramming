class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        finalSeats=[]
        finalSeats2=[]
        for i in seats:
            finalSeats.append(i)
            finalSeats2.append(i)
        i=0
        ctr=0
        while(i<len(seats)):
            if finalSeats[i]:
                ctr=1
                if i!=len(seats)-1 and not finalSeats[i+1]:
                    finalSeats[i+1]=1
                    i+=1
            elif ctr:
                finalSeats[i]=finalSeats[i-1]+1
            i+=1
        j=len(seats)-1
        ctr1=0
        while(j>=0):
            if finalSeats2[j]:
                ctr1=1
                if j!=0 and not finalSeats2[j-1]:
                    finalSeats2[j-1]=1
                    j-=1
            elif ctr1:
                finalSeats2[j]=finalSeats2[j+1]+1
            j-=1
        final=[]
        for i in range(len(seats)):
            if finalSeats[i] and finalSeats2[i]:
                final.append(min(finalSeats[i],finalSeats2[i]))
            else:
                final.append(max(finalSeats[i],finalSeats2[i]))                
        return max(final)
