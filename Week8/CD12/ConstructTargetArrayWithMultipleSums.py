class Solution:
    def isPossible(self, target: List[int]) -> bool:
        max_=max(target)
        tot=sum(target)-max_
        max_ind=target.index(max_)
        while(max_>1):
            target[max_ind]=max_-tot
            if target[max_ind]<1:
                return False   
            max_=max(target)
            max_ind=target.index(max_)
            tot=sum(target)-max_
        return True
