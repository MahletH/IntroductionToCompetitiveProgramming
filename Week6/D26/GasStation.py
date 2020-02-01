class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ind=-1
        total=sum(gas)-sum(cost)
        if(total<0):
            return -1
        tot=0
        ctr=1
        for i in range(len(gas)):
            curr=gas[i]-cost[i]
            tot+=curr
            if(curr>=0 and ctr):
                ind=i
                ctr=0
            if(tot>=0 and ind<0):
                ind=i
            elif(tot<0):
                ind=-1
                tot=0
        return ind
                
        
