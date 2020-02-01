class Solution:
    def possible(self, num: int) -> int:
        if num==1:
            return 0
        elif num==2:
            return 1
        return num-1+self.possible(num-1)
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        collect={}
        ctr=0
        for i in range(len(dominoes)):
            dom=dominoes[i]
            dom.sort()
            if(not collect.get(tuple(dom))):
                collect[tuple(dom)]=[i]
            else:
                collect[tuple(dom)].append(i)        
        lst=list(collect.values())
        sums=0
        for i in lst:
            sums+=self.possible(len(i))
        return sums
        
